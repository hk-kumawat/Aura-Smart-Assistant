import streamlit as st
import os
import time
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load API keys from .env file
load_dotenv()
groq_api_key = st.secrets["GROQ_API_KEY"]

# Function to analyze sentiment (Emotion Recognition)
def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(text)
    return sentiment_score

# Initialize session state memory and question tracking
if 'conversation_memory' not in st.session_state:
    st.session_state.conversation_memory = ConversationBufferMemory(memory_key="history")
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'first_question' not in st.session_state:
    st.session_state.first_question = None  # Store first question

# Define main function
def main():
    # Display Aura's goal in a dropdown (expandable section)
    with st.expander("🚀 **Aura's Goal: Instant, Intuitive, and Efficient Responses** 🤖"):
        st.write(
            """
            Aura was designed with one goal in mind: **to provide quick, intuitive, and efficient responses** to your questions. 💬✨
            <br><br>
            While other models like ChatGPT offer fantastic conversational experiences, **Aura** focuses on delivering *rapid, instant answers* to make your interactions seamless and efficient. ⚡️💡
            <br><br>
            It's all about **speed** and **clarity**—your questions answered *instantly* for a smooth, engaging experience. 🌟
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <h1 id="aura-title" style="text-align: center; font-size: 40px; animation: fadeIn 2s ease-in-out;">Talk to Aura: The Smart Assistant That Understands You! 🤖💬</h1>
        <p style='text-align: center; color: #00796b; font-size: 18px; margin-top: 0px; animation: fadeIn 2s ease-in-out;'>Dive into Aura’s world—ask anything, enjoy a unique conversation every time!</p>
        <style>
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    groq_chat = ChatGroq(groq_api_key=groq_api_key, model_name="mixtral-8x7b-32768")

    prompt_template = PromptTemplate(
        input_variables=["input", "history"],
        template=( 
            "You are a helpful assistant. The conversation so far is:\n{history}\n"
            "User: {input}\nAssistant:\n"
        )
    )

    llm_chain = LLMChain(
        llm=groq_chat,
        prompt=prompt_template,
        memory=st.session_state.conversation_memory
    )

    with st.form(key="chat_form", clear_on_submit=True):
        user_question = st.text_area("Ask a question:", key="user_input")
        send_button = st.form_submit_button("Send")

    if send_button and user_question:
        if st.session_state.first_question is None:
            st.session_state.first_question = user_question

        sentiment = analyze_sentiment(user_question)
        sentiment_label = "neutral"
        if sentiment['compound'] >= 0.05:
            sentiment_label = "positive"
        elif sentiment['compound'] <= -0.05:
            sentiment_label = "negative"

        response_text = llm_chain.run(input=user_question)

        if sentiment_label == "positive":
            response_text = f"😊 {response_text}"
        elif sentiment_label == "negative":
            response_text = f"😔 {response_text}"
        else:
            response_text = f"🙂 {response_text}"

        st.session_state.conversation_memory.chat_memory.add_user_message(user_question)
        st.session_state.conversation_memory.chat_memory.add_ai_message(response_text)
        st.session_state.chat_history.insert(0, {'human': user_question, 'AI': response_text})

        time.sleep(0.1)

    theme = st.get_option("theme.base")
    user_bg, bot_bg, text_color = ("#00796b", "#333", "white") if theme == "dark" else ("#e0f7fa", "#f1f1f1", "black")

    for msg in st.session_state.chat_history:
        user_width = "100%"
        bot_width = "100%"
        spacing = "20px"

        st.markdown(
            f"""
            <div class="bubble bot" style="padding: 15px; border-radius: 8px; background-color: {bot_bg}; color: {text_color}; width: {bot_width}; margin: auto; text-align: justify; animation: fadeIn 0.5s ease-in-out; margin-bottom: {spacing};">
                <strong>Aura:</strong> {msg['AI']}
            </div>
            """, unsafe_allow_html=True)

        st.markdown(
            f"""
            <div class="bubble user" style="padding: 15px; border-radius: 8px; background-color: {user_bg}; color: {text_color}; width: {user_width}; margin: auto; text-align: justify; animation: fadeIn 0.5s ease-in-out; margin-bottom: {spacing};">
                <strong>You:</strong> {msg['human']}
            </div>
            """, unsafe_allow_html=True)

    st.markdown(
        """
        <style>
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        </style>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #7f8c8d; font-size: 16px;'>"
        "<p style='text-align: center;'>🔮 <strong>Brought to Life By</strong> - Harshal Kumawat 🤖</p>"  
        "</div>",
        unsafe_allow_html=True
    )
