<a id="readme-top"></a>

# **Aura Smart Assistant 🤖**

![Aura Logo](https://github.com/user-attachments/assets/8c9825be-d9de-4488-a770-24431601b571)

## Overview

**Aura Smart Assistant** is an AI-powered conversational assistant designed to engage in meaningful, context-aware interactions with users. Built using **LangChain**, **VaderSentiment**, and **GroQ**, Aura can respond to text-based queries and provide insightful answers in real-time. 

Whether you're seeking **quick information**, **exploring ideas**, or having a **casual chat**, **Aura** understands and generates **context-aware** responses tailored to your needs. It uses **sentiment analysis** for emotionally intelligent replies and leverages **GroQ's powerful backend** for fast, reliable, and rich responses. 

<br>

## Live Demo

Explore Aura in action! 👉🏻 [![Experience Aura! 🌟](https://img.shields.io/badge/Experience%20Aura!-blue)](https://ask-aura.streamlit.app/)

<br>

_Aura, your friendly assistant, is here to chat and answer your questions! 👇🏻_

<p align="center">
  <img src="https://github.com/user-attachments/assets/0fdd7c08-9426-45a6-8cf0-e30c4ea263e6" alt="Aura Assistant Demo">
</p>


<br>


## Learning Journey 🗺️

I developed Aura to merge my passion for conversational AI with my desire to create highly responsive applications. Here’s a snapshot of my journey:

- **Inspiration:**  
  Inspired by the need for smarter, faster AI assistants, I wanted to create an assistant that not only responds accurately but also adapts its tone based on your sentiment.

- **Why I Made It:**  
  Aura was built to provide instant answers with a personalized touch. By integrating Groq Chat with LangChain and using sentiment analysis, I aimed to deliver fast responses that feel both human and efficient.

- **Challenges Faced:**  
  - **API & Environment Management:** Handling API keys securely with Streamlit’s secrets management and dotenv.
  - **Conversational Memory:** Implementing session-based conversation history for continuous dialogue.
  - **Dynamic UI:** Creating an engaging UI with animations and custom CSS for a smooth chat experience.

- **What I Learned:**  
  - Mastery of **Streamlit** for interactive web apps.
  - Leveraging **LangChain** and **Groq Chat** for building conversational agents.
  - Integrating sentiment analysis using **VADER** to tailor responses.
  - Best practices for session management and responsive design.

Every step of this project has enriched my understanding of AI-powered conversations and reinforced my commitment to creating user-friendly solutions.

<br>


## Table of Contents

1. [Features](#features)
2. [How It Works](#how-it-works)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Technologies Used](#technologies-used)
6. [Results](#results)
7. [Directory Structure](#directory-structure)
8. [Future Enhancements](#future-enhancements)
9. [Contributing](#contributing)
10. [License](#license)
11. [Contact](#contact)

<br>

## Features🌟

- **Context-Aware Conversations**:
  Responds to a wide range of questions with personalized, instant answers.
  
- **Sentiment Analysis**:
  Analyzes the sentiment of user inputs using **VaderSentiment** to provide tone-appropriate responses.
  
- **Real-time Responses**:
  Powered by **GroQ API**, ensuring a fast response time.
  
- **Streamlit Interface**:
  Interactive and user-friendly interface for seamless interaction with Aura.
  
- **Temporary Memory**:
  Remembers user inputs (such as name or preferences) temporarily during a session, so Aura can provide more personalized responses. Once the tab is refreshed, all memory is cleared to protect privacy.

<br>

## How It Works🧠

1. **User Input**: The user types a message or question into the chat interface.
   
2. **Sentiment Analysis**: The text is processed by **VaderSentiment** to detect the sentiment and adjust the tone of Aura's response accordingly.
 
3. **GroQ API**: The input is sent to the **GroQ API**, which handles intelligent query answering and provides a context-aware response.
 
4. **Response**: Aura generates an instant response, displayed to the user through the Streamlit interface.

<br>


## Installation🛠

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hk-kumawat/Aura-Smart-Assistant.git
   cd Aura-Smart-Assistant
   ```

2. **Create & Activate a Virtual Environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate       # On Windows: venv\Scripts\activate
   ```

3. **Install Required Packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Your API Key:**
   - Create a `.env` file or use Streamlit's secrets management.
   - For Streamlit, create a `.streamlit/secrets.toml` file and add:
     ```toml
     [GROQ]
     GROQ_API_KEY = "your_groq_api_key_here"
     ```
   - Alternatively, set the environment variable as needed.

<br>


## Usage🚀

### Running the Aura Smart Assistant

Start the smart assistant with:
```bash
Streamlight run app.py
```
**Features include:**
- **Conversational Interface:** Chat with Aura by typing your questions.
- **Sentiment-Based Responses:** Aura adjusts its replies based on your emotional tone.
- **Dynamic Conversation Memory:** Enjoy continuous and coherent interactions.

<br>

## Technologies Used💻

- **Programming Language:**  
  - `Python`

- **Web Framework:**  
  - `Streamlit`

- **Conversational AI:**  
  - `LangChain`
  - `ChatGroq` (for LLM-based chat)

- **Sentiment Analysis:**  
  - `VADER SentimentIntensityAnalyzer`

- **Environment Management:**  
  - `python-dotenv`

- **Other:**  
  - Standard libraries like `os`, `time`
    

<br>


## Results🏆

The **Aura Smart Assistant** is able to provide meaningful, real-time answers to various types of questions. It successfully understands and responds in a contextually relevant manner based on sentiment analysis and intelligent querying through the **GroQ API**.

<p align="center">
  <img src="https://github.com/user-attachments/assets/65916371-7928-44bd-bb3c-03286f40e19f" alt="Aura Conversation Example" width="600"/>
</p>

In the example above, Aura correctly analyzes the input, adjusts its tone based on sentiment, and generates an appropriate response.


<br>


## Directory Structure📁

```plaintext
hk-kumawat-aura-smart-assistant/
├── README.md           # Project documentation
├── LICENSE             # License information
├── app.py              # Streamlit application for Aura Smart Assistant
└── requirements.txt    # List of dependencies
```

<br>


## Future Enhancements🚀

1. **Multi-turn Conversation**: Enhance the assistant to remember the context over multiple interactions for deeper conversations.
 
2. **Emotionally Intelligent Responses**: Expand sentiment analysis to detect a broader range of emotions (e.g., joy, anger, surprise).

3. **Real-world Integration**: Integrate with external services (e.g., calendars, reminders, news, etc.) to make Aura more functional.

4. **Voice Integration**: Enable Aura to understand and respond via voice, making it more interactive.

<br> 


## Contributing🤝
Contributions make the open source community such an amazing place to learn, inspire, and create. 🙌 Any contributions you make are greatly appreciated! 😊

Have an idea to improve this project? Go ahead and fork the repo to create a pull request, or open an issue with the tag **"enhancement"**. Don't forget to give the project a star! ⭐ Thanks again! 🙏

<br>

1. **Fork** the repository.

2. **Create** a new branch:
   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Commit** your changes with a descriptive message.

4. **Push** to your branch:
   ```bash
   git push origin feature/YourFeatureName
   ```

5. **Open** a Pull Request detailing your enhancements or bug fixes.

<br> 


## License📝

This project is licensed under the **MIT License** — see the [LICENSE](./LICENSE) file for details.

<br>


## Contact

### 📬 Get in Touch!
Feel free to reach out for collaborations or questions:

- [![GitHub](https://img.shields.io/badge/GitHub-hk--kumawat-blue?logo=github)](https://github.com/hk-kumawat) 💻 — Explore my projects and contributions.
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-Harshal%20Kumawat-blue?logo=linkedin)](https://www.linkedin.com/in/harshal-kumawat/) 🌐 — Let's connect professionally.
- [![Email](https://img.shields.io/badge/Email-harshalkumawat100@gmail.com-blue?logo=gmail)](mailto:harshalkumawat100@gmail.com) 📧 — Send me an email for discussions and queries.

<br>


## Thanks for chatting—enjoy your conversation with Aura! 🤖💬

> "Smart conversations start with a single question." – Anonymous

<p align="right">
  (<a href="#readme-top">back to top</a>)
</p>
