
# **Aura Smart Assistant 🤖**

![Aura Logo](https://github.com/user-attachments/assets/8c9825be-d9de-4488-a770-24431601b571)

## Overview

**Aura Smart Assistant** is an AI-powered conversational assistant designed to engage in meaningful, context-aware interactions with users. Built using **LangChain**, **VaderSentiment**, and **GroQ**, Aura can respond to text-based queries and provide insightful answers in real-time. 

Whether you're seeking **quick information**, **exploring ideas**, or having a **casual chat**, **Aura** understands and generates **context-aware** responses tailored to your needs. It uses **sentiment analysis** for emotionally intelligent replies and leverages **GroQ's powerful backend** for fast, reliable, and rich responses. 



## Live Demo

Explore Aura in action! 👉🏻 [![Experience Aura! 🌟](https://img.shields.io/badge/Experience%20Aura!-blue)](https://ask-aura.streamlit.app/)

<br>

_Aura, your friendly assistant, is here to chat and answer your questions!_

<p align="center">
  <img src="https://github.com/user-attachments/assets/0fdd7c08-9426-45a6-8cf0-e30c4ea263e6" alt="Aura Assistant Demo">
</p>

<br>

## Table of Contents

1. [Features](#features)
2. [How It Works](#how-it-works)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Technologies Used](#technologies-used)
6. [Results](#results)
7. [Conclusion](#conclusion)
8. [Future Enhancements](#future-enhancements)
9. [License](#license)
10. [Contact](#contact)

<br>

## Features🌟

- **Context-Aware Conversations**: Responds to a wide range of questions with personalized, instant answers.
- **Sentiment Analysis**: Analyzes the sentiment of user inputs using **VaderSentiment** to provide tone-appropriate responses.
- **Real-time Responses**: Powered by **GroQ API**, ensuring a fast response time.
- **Streamlit Interface**: Interactive and user-friendly interface for seamless interaction with Aura.
- **Temporary Memory**: **Remembers** user inputs (such as name or preferences) temporarily during a session, so Aura can provide more personalized responses. Once the tab is refreshed, all memory is cleared to protect privacy.

<br>

## How It Works🧠

1. **User Input**: The user types a message or question into the chat interface.
2. **Sentiment Analysis**: The text is processed by **VaderSentiment** to detect the sentiment and adjust the tone of Aura's response accordingly.
3. **GroQ API**: The input is sent to the **GroQ API**, which handles intelligent query answering and provides a context-aware response.
4. **Response**: Aura generates an instant response, displayed to the user through the Streamlit interface.

<br>

## Installation🛠

1. **Clone the repository**:
   ```bash
   git clone https://github.com/hk-kumawat/Aura-Smart-Assistant.git
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup environment variables**:
   - Create a `.env` file in the root directory and add the following:
     ```env
     GROQ_API_KEY=your_groq_api_key
     ```
   - Replace `your_groq_api_key` with your actual **GroQ API Key**.

<br>

## Usage🚀

1. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

2. **Interact with Aura**: Type any question or statement, and Aura will respond instantly, offering insights based on its contextual knowledge.

<br>

## Technologies Used💻

- **Programming Language**: Python
- **Libraries**:
  - `streamlit` — For creating the user interface.
  - `langchain` — For managing the chain of conversation and data processing.
  - `vaderSentiment` — Sentiment analysis for tone detection.
  - `groq` — For intelligent query answering.
  - `python-dotenv` — To manage environment variables.
  
- **API**:
  - **GroQ API** — Powers contextual and intelligent responses.

<br>

## Results🏆

The **Aura Smart Assistant** is able to provide meaningful, real-time answers to various types of questions. It successfully understands and responds in a contextually relevant manner based on sentiment analysis and intelligent querying through the **GroQ API**.

<p align="center">
  <img src="https://github.com/user-attachments/assets/65916371-7928-44bd-bb3c-03286f40e19f" alt="Aura Conversation Example" width="600"/>
</p>

In the example above, Aura correctly analyzes the input, adjusts its tone based on sentiment, and generates an appropriate response.

<br>

## Conclusion📚

The **Aura Smart Assistant** project demonstrates how deep learning, natural language processing, and intelligent APIs can be combined to create a powerful and interactive virtual assistant. It showcases the use of **GroQ**, **VaderSentiment**, and **LangChain** in a real-world application, offering a practical solution for engaging, context-aware conversations.

Real-world applications of Aura include **customer support**, where it provides real-time solutions to user queries; as a **personal assistant** for task management; offering **mental health support** with emotionally intelligent conversations; serving as an **educational tool** for interactive learning; and enhancing **business productivity** by facilitating quick information retrieval and team collaboration. This makes Aura a versatile assistant for both personal and professional use.

<br>

## Future Enhancements🚀

1. **Multi-turn Conversation**: Enhance the assistant to remember the context over multiple interactions for deeper conversations.
2. **Emotionally Intelligent Responses**: Expand sentiment analysis to detect a broader range of emotions (e.g., joy, anger, surprise).
3. **Real-world Integration**: Integrate with external services (e.g., calendars, reminders, news, etc.) to make Aura more functional.
4. **Voice Integration**: Enable Aura to understand and respond via voice, making it more interactive.

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

---

## **Thanks for exploring Aura's world! 🌍🤖 We hope you had a great time! 🎉💫**

> "An assistant's true power is in its ability to make your life easier, one conversation at a time." - Harshal Kumawat
