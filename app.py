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
#groq_api_key = os.environ["GROQ_API_KEY"]
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
            Aura was designed with one goal in mind: <strong>to provide quick, intuitive, and efficient responses</strong> to your questions. 💬✨
            <br><br>
            While other models like ChatGPT offer fantastic conversational experiences, <strong>Aura</strong> focuses on delivering <em>rapid, instant answers</em> to make your interactions seamless and efficient. ⚡️💡
            <br><br>
            It's all about <strong>speed</strong> and <strong>clarity</strong>—your questions answered <em>instantly</em> for a smooth, engaging experience. 🌟
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

    # Initialize Groq Langchain chat object
    groq_chat = ChatGroq(groq_api_key=groq_api_key, model_name="mixtral-8x7b-32768")

    # Define the prompt template with additional context for conversation recall
    prompt_template = PromptTemplate(
        input_variables=["input", "history"],
        template=( 
            "You are a helpful assistant. The conversation so far is:\n{history}\n"
            "User: {input}\nAssistant:\n"
        )
    )

    # Initialize LLMChain with memory
    llm_chain = LLMChain(
        llm=groq_chat,
        prompt=prompt_template,
        memory=st.session_state.conversation_memory
    )

    # Input form for user question
    with st.form(key="chat_form", clear_on_submit=True):
        user_question = st.text_area("Ask a question:", key="user_input")
        send_button = st.form_submit_button("Send")

    # Process the question if send_button is clicked
    if send_button and user_question:
        # Check if this is the user's first question and store it
        if st.session_state.first_question is None:
            st.session_state.first_question = user_question

        # Analyze sentiment of the user's input
        sentiment = analyze_sentiment(user_question)
        sentiment_label = "neutral"
        if sentiment['compound'] >= 0.05:
            sentiment_label = "positive"
        elif sentiment['compound'] <= -0.05:
            sentiment_label = "negative"

        # Generate response using LLMChain with memory
        response_text = llm_chain.run(input=user_question)

        # Customize response based on sentiment
        if sentiment_label == "positive":
            response_text = f"😊 {response_text}"
        elif sentiment_label == "negative":
            response_text = f"😔 {response_text}"
        else:
            response_text = f"🙂 {response_text}"

        # Save conversation in session state memory for continuity
        st.session_state.conversation_memory.chat_memory.add_user_message(user_question)
        st.session_state.conversation_memory.chat_memory.add_ai_message(response_text)
        st.session_state.chat_history.insert(0, {'human': user_question, 'AI': response_text})

        # Small delay to ensure sync on mobile
        time.sleep(0.1)

    # Detect Streamlit theme setting (light/dark mode)
    theme = st.get_option("theme.base")
    user_bg, bot_bg, text_color = ("#00796b", "#333", "white") if theme == "dark" else ("#e0f7fa", "#f1f1f1", "black")

    # Display conversation in reverse order (latest message on top)
    for msg in st.session_state.chat_history:
        # Dynamically calculate width based on message length
        user_width = min(50 + len(msg["human"]) // 5, 75)
        bot_width = min(50 + len(msg["AI"]) // 5, 75)
        spacing = "20px"  # Add spacing between the user and bot messages

        # Chatbot's response aligned left with animation
        st.markdown(
            f"""
            <div class="bubble bot" style="padding: 15px; border-radius: 8px; background-color: {bot_bg}; color: {text_color}; width: {bot_width}%; margin-right: auto; text-align: left; animation: slideInLeft 0.5s ease-in-out; margin-bottom: {spacing};">
                <strong>Aura:</strong> {msg['AI']}
            </div>
            """, unsafe_allow_html=True)

        # User's message aligned right with animation
       user_width = min(50 + len(msg["human"]) // 5, 75)  

        st.markdown(
            f"""
            <div class="bubble user" style="padding: 15px; border-radius: 8px; background-color: {user_bg}; color: {text_color}; width: {user_width}%; margin-left: auto; text-align: left; animation: slideInRight 0.5s ease-in-out; margin-bottom: {spacing};">
                <strong>You:</strong> {msg['human']}
            </div>
            """, unsafe_allow_html=True)

    # CSS for user and Aura bubbles with animations
    st.markdown(
        """
        <style>
        @keyframes slideInRight {
            from { opacity: 0; transform: translateX(20px); }
            to { opacity: 1; transform: translateX(0); }
        }

        @keyframes slideInLeft {
            from { opacity: 0; transform: translateX(-20px); }
            to { opacity: 1; transform: translateX(0); }
        }
        </style>
        """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()

    # Show footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #7f8c8d; font-size: 16px;'>"
        "<p style='text-align: center;'>🔮 <strong>Brought to Life By</strong> - Harshal Kumawat 🤖</p>"  
        "</div>",
        unsafe_allow_html=True
    )
