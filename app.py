import streamlit as st
import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load environment variables
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize the ChatGroq model
groq_chat = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="mixtral-8x7b-32768"
)

# Initialize the LLM prompt template
prompt_template = PromptTemplate(
    input_variables=["input"],
    template="You are a helpful assistant. Respond to the following question: {input}"
)

# Initialize the LLMChain
llm_chain = LLMChain(
    llm=groq_chat,
    prompt=prompt_template
)

# Analyze sentiment of a given text
def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(text)

# Main function
def main():
    st.title("Talk to Aura: The Smart Assistant That Understands You! 🤖💬")

    # Initialize session state variables
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    if 'user_name' not in st.session_state:
        st.session_state['user_name'] = None

    # Input form with "Send" button
    with st.form("chat_form", clear_on_submit=True):
        user_question = st.text_area("Ask a question:", key="user_input")
        send_button = st.form_submit_button("Send")

    # Process the question when "Send" is clicked
    if send_button and user_question:
        # Sentiment analysis
        sentiment = analyze_sentiment(user_question)
        sentiment_label = (
            "😊" if sentiment['compound'] >= 0.05 else
            "😔" if sentiment['compound'] <= -0.05 else
            "🙂"
        )

        # Personalization if user introduces their name
        if "my name is" in user_question.lower():
            name_start = user_question.lower().find("my name is") + len("my name is")
            user_name = user_question[name_start:].strip()
            st.session_state.user_name = user_name
            response_text = f"Nice to meet you, {user_name}!"
        elif "name" in user_question.lower() and st.session_state.user_name:
            response_text = f"Your name is {st.session_state.user_name}."
        else:
            # Generate response using the AI model
            response_text = llm_chain.run(input=user_question)
            response_text = f"{sentiment_label} {response_text}"

        # Add the new conversation to chat history
        st.session_state.chat_history.insert(0, {'human': user_question, 'AI': response_text})

    # Display the chat history in reverse (newest message at the top)
    for msg in st.session_state.chat_history:
        user_bubble = f"<div style='background:#e0f7fa; border-radius:10px; padding:10px; text-align:right; margin:10px 0;'>{msg['human']}</div>"
        bot_bubble = f"<div style='background:#f1f1f1; border-radius:10px; padding:10px; text-align:left; margin:10px 0;'>{msg['AI']}</div>"
        
        st.markdown(bot_bubble, unsafe_allow_html=True)
        st.markdown(user_bubble, unsafe_allow_html=True)

    # Add custom CSS for a modern text box
    st.markdown(
        """
        <style>
        textarea { border-radius: 8px; border: 2px solid #ccc; padding: 10px; }
        textarea:focus { border-color: #00796b; }
        </style>
        """, unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
