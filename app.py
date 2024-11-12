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
groq_api_key = os.environ['GROQ_API_KEY']

# Function to analyze sentiment (Emotion Recognition)
def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(text)
    return sentiment_score

def main():
    # Title text with fade-in animation and theme-based color changes
    st.markdown(
        """
        <h1 id="aura-title" style="text-align: center; font-size: 40px; margin-bottom: 0px; animation: fadeIn 2s ease-in-out;">
            Talk to Aura: The Smart Assistant That Understands You! 🤖💬
        </h1>
        <p style='text-align: center; color: #00796b; font-size: 18px; margin-top: 0px;'>
            Dive into Aura’s world—ask anything, enjoy a unique conversation every time, with instant responses!
        </p>
        <style>
        /* Fade-in animation definition */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Apply animation to the title */
        #aura-title {
            animation: fadeIn 2s ease-in-out;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # JavaScript to change title color based on theme
    st.markdown(
        """
        <script>
            const auraTitle = document.getElementById("aura-title");
            function applyTheme() {
                if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
                    auraTitle.style.color = "white";
                } else {
                    auraTitle.style.color = "black";
                }
            }
            applyTheme();
            window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', applyTheme);
        </script>
        """,
        unsafe_allow_html=True
    )

    # Initialize memory to remember full conversation history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'user_name' not in st.session_state:
        st.session_state.user_name = None

    # Initialize conversation memory
    conversation_memory = ConversationBufferMemory(memory_key="history")

    # Initialize Groq Langchain chat object
    groq_chat = ChatGroq(
        groq_api_key=groq_api_key,
        model_name="mixtral-8x7b-32768"
    )

    # Define the prompt template for the LLM chain
    prompt_template = PromptTemplate(
        input_variables=["input", "history"],
        template="You are a helpful assistant. The conversation so far is:\n{history}\nUser: {input}\nAssistant:"
    )

    # Initialize LLMChain with the prompt, Groq model, and memory
    llm_chain = LLMChain(
        llm=groq_chat,
        prompt=prompt_template,
        memory=conversation_memory
    )

    # Input form with "Send" button
    with st.form(key="chat_form", clear_on_submit=True):
        user_question = st.text_area("Ask a question:", key="user_input")
        send_button = st.form_submit_button("Send")

    # Process the question if send_button is clicked
    if send_button and user_question:
        # Analyze sentiment of the user's input
        sentiment = analyze_sentiment(user_question)
        sentiment_label = "neutral"
        if sentiment['compound'] >= 0.05:
            sentiment_label = "positive"
        elif sentiment['compound'] <= -0.05:
            sentiment_label = "negative"
        
        # Respond based on sentiment
        if "name" in user_question.lower() and st.session_state.user_name:
            response_text = f"Your name is {st.session_state.user_name}."
        elif "my name is" in user_question.lower():
            name_start = user_question.lower().find("my name is") + len("my name is")
            user_name = user_question[name_start:].strip()
            st.session_state.user_name = user_name
            response_text = f"Nice to meet you, {user_name}!"
        else:
            # Generate response using LLMChain with memory for conversation context
            response_text = llm_chain.run(input=user_question)

            # Customize response based on sentiment
            if sentiment_label == "positive":
                response_text = f"😊 {response_text}"
            elif sentiment_label == "negative":
                response_text = f"😔 {response_text}"
            else:
                response_text = f"🙂 {response_text}"

        # Small delay to ensure sync on mobile
        time.sleep(0.1)

        # Save the conversation in session state
        st.session_state.chat_history.insert(0, {'human': user_question, 'AI': response_text})

    # Detect Streamlit theme setting (light/dark mode)
    theme = st.get_option("theme.base")

    # Define color schemes based on theme
    if theme == "dark":
        user_bg = "#00796b"
        bot_bg = "#333"
        text_color = "white"
    else:
        user_bg = "#e0f7fa"
        bot_bg = "#f1f1f1"
        text_color = "black"

    # Display conversation in reverse order (latest message on top)
    for msg in st.session_state.chat_history:
        user_width = min(50 + len(msg["human"]) // 5, 75)
        bot_width = min(50 + len(msg["AI"]) // 5, 75)

        # Chatbot's response aligned left with animation
        st.markdown(
            f"""
            <div class="bubble bot" style="padding: 15px; border-radius: 8px; background-color: {bot_bg}; color: {text_color}; width: {bot_width}%; margin-right: auto; text-align: left; margin-top: 15px;">
                <strong>Aura:</strong> {msg["AI"]}
            </div>
            """, unsafe_allow_html=True)

        # User's message aligned right with animation
        st.markdown(
            f"""
            <div class="bubble user" style="padding: 15px; border-radius: 8px; background-color: {user_bg}; color: {text_color}; width: {user_width}%; margin-left: auto; text-align: right; margin-top: 15px;">
                <strong>You:</strong> {msg["human"]}
            </div>
            """, unsafe_allow_html=True)

    # Add smooth scrolling to the page
    st.markdown('<script>window.scrollTo(0, document.body.scrollHeight);</script>', unsafe_allow_html=True)

    # CSS for chat bubbles with side-specific animations
    st.markdown(
        """
        <style>
        /* Animation for user message sliding from the right */
        @keyframes slideInRight {
            from { opacity: 0; transform: translateX(20px); }
            to { opacity: 1; transform: translateX(0); }
        }

        /* Animation for Aura’s response sliding from the left */
        @keyframes slideInLeft {
            from { opacity: 0; transform: translateX(-20px); }
            to { opacity: 1; transform: translateX(0); }
        }

        /* Apply animations to user and bot bubbles */
        .bubble.user {
            animation: slideInRight 0.5s ease-in-out;
        }
        .bubble.bot {
            animation: slideInLeft 0.5s ease-in-out;
        }

        /* Adjust colors for the textarea and send button */
        textarea {
            border-radius: 8px;
            border: 2px solid #ccc;
            padding: 10px;
            font-size: 16px;
            transition: border-color 0.3s ease;
        }
        textarea:focus {
            border-color: #00796b;
        }
        .css-1gw3tw1.edgvbvh3 {
            transition: background-color 0.3s ease;
        }
        .css-1gw3tw1.edgvbvh3:hover {
            background-color: #00796b;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()


# Footer section
st.markdown("---")  
st.markdown(
    "<div style='text-align: center; color: #7f8c8d; font-size: 16px;'>"
    "<p style='text-align: center;'>🔮 <strong>Brought to Life By</strong> - Harshal Kumawat 🤖</p>"
    "</div>",
    unsafe_allow_html=True
)
