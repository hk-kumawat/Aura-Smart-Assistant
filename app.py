import streamlit as st
import os
from dotenv import load_dotenv
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq  # Using ChatGroq or replace with other model
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load API keys from .env file
load_dotenv()

# Function to analyze sentiment (Emotion Recognition)
def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(text)
    return sentiment_score

def main():
    st.title("Talk to Aura: The Smart Assistant That Understands You! 🤖💬")
    st.markdown("*Dive into Aura’s world—ask anything, enjoy a unique conversation every time, with instant responses!*")

    # Initialize memory to remember full conversation history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'user_name' not in st.session_state:
        st.session_state.user_name = None  # Initialize to None if not set

    # Initialize ChatGroq language model (you can replace it with other compatible models)
    llm = ChatGroq()  # Ensure you initialize it properly based on the library's doc

    # Define the prompt template for the LLM chain
    prompt_template = PromptTemplate(
        input_variables=["input", "history"],  # Adding history here as part of the input
        template="You are a helpful assistant. Respond to the following question in context of previous conversation history: {history} {input}"
    )

    # Initialize ConversationChain with the LLM and prompt
    conversation_chain = ConversationChain(
        llm=llm,
        prompt=prompt_template
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
            # Store the user's name if they introduce themselves
            name_start = user_question.lower().find("my name is") + len("my name is")
            user_name = user_question[name_start:].strip()
            st.session_state.user_name = user_name
            response_text = f"Nice to meet you, {user_name}!"
        else:
            # Generate response using ConversationChain
            response = conversation_chain.run(input=user_question, history=st.session_state.chat_history)
            response_text = response

            # Customize response based on sentiment
            if sentiment_label == "positive":
                response_text = f"😊 {response_text}"
            elif sentiment_label == "negative":
                response_text = f"😔 {response_text}"
            else:
                response_text = f"🙂 {response_text}"

        # Save the conversation in session state
        message = {'human': user_question, 'AI': response_text}
        st.session_state.chat_history.insert(0, message)  # Insert at the top (append upwards)

    # Hide sidebar and toolbar
    st.write("<style>div.css-1kyxreq {display: none;} div[data-testid='stToolbar'] {display: none;}</style>", unsafe_allow_html=True)

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
        # Adjust the width of the bubbles based on message length
        user_width = min(55 + len(msg["human"]) // 10, 80)  # Limit width of user messages
        bot_width = min(55 + len(msg["AI"]) // 10, 80)  # Limit width of bot messages

        # Chatbot's response aligned left
        st.markdown(
            f"""
            <div style="padding: 15px; border-radius: 8px; background-color: {bot_bg}; color: {text_color}; width: {bot_width}%; margin-right: auto; text-align: left; margin-top: 15px;">
                <strong>Aura:</strong> {msg["AI"]}
            </div>
            """, unsafe_allow_html=True)

        # User's message aligned right
        st.markdown(
            f"""
            <div style="padding: 15px; border-radius: 8px; background-color: {user_bg}; color: {text_color}; width: {user_width}%; margin-left: auto; text-align: right; margin-top: 15px;">
                <strong>User:</strong> {msg["human"]}
            </div>
            """, unsafe_allow_html=True)

    # Add smooth scrolling to the page for a better experience
    st.markdown('<script>window.scrollTo(0, document.body.scrollHeight);</script>', unsafe_allow_html=True)

    # Add hover effect for the send button (for better interactivity)
    st.markdown(
        """
        <style>
        .css-1gw3tw1.edgvbvh3 {
            transition: background-color 0.3s ease;
        }
        .css-1gw3tw1.edgvbvh3:hover {
            background-color: #00796b;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)

    # CSS for text box (optional for a more modern style)
    st.markdown(
        """
        <style>
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
