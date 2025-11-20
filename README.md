<a id="readme-top"></a>

<div align="center">

# 🤖 Aura Smart Assistant

### AI-Powered Conversational Assistant with Sentiment Intelligence

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-121212?style=for-the-badge&logo=chainlink&logoColor=white)](https://www.langchain.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

[Live Demo](https://ask-aura.streamlit.app/) • [Report Bug](https://github.com/hk-kumawat/Aura-Smart-Assistant/issues) • [Request Feature](https://github.com/hk-kumawat/Aura-Smart-Assistant/issues)

![Aura Logo](https://github.com/user-attachments/assets/8c9825be-d9de-4488-a770-24431601b571)

</div>

---

## 📋 Table of Contents

- [About The Project](#about-the-project)
- [Key Features](#key-features)
- [Live Demo](#live-demo)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🎯 About The Project

<p align="center">
  <img src="https://github.com/user-attachments/assets/0fdd7c08-9426-45a6-8cf0-e30c4ea263e6" alt="Aura Assistant Demo">
</p>

**Aura Smart Assistant** is an intelligent, emotionally-aware chatbot built to provide **instant, context-aware responses** to user queries. Unlike traditional chatbots, Aura analyzes the sentiment of your messages and adapts its tone accordingly, creating a more human-like conversational experience.

Powered by **Groq's high-performance LLM infrastructure**, **LangChain** for conversation orchestration, and **VADER** for sentiment analysis, Aura delivers lightning-fast responses while maintaining conversation context across multiple exchanges.

### 🌟 Why Aura?

- **⚡ Speed-Focused**: Leverages Groq's optimized inference for near-instantaneous responses
- **🧠 Context-Aware**: Remembers conversation history for coherent, multi-turn dialogues
- **😊 Emotionally Intelligent**: Adjusts response tone based on detected sentiment
- **🎨 Beautiful UI**: Clean, animated interface with dynamic message bubbles
- **🔒 Privacy-First**: Session-based memory that clears on refresh

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| **💬 Natural Conversations** | Powered by Mixtral-8x7B model for human-like interactions |
| **🎭 Sentiment Analysis** | Real-time emotion detection using VADER (positive/negative/neutral) |
| **🧵 Conversation Memory** | Maintains context throughout your session using LangChain's memory system |
| **🎨 Dynamic UI** | Responsive chat bubbles with smooth animations and theme support |
| **🌓 Dark/Light Mode** | Automatic theme detection and adaptation |
| **📊 First Question Tracking** | Stores initial query for enhanced context understanding |
| **🚀 High Performance** | Sub-second response times via Groq's LPU inference |

---

## 🌐 Live Demo

Experience Aura in action! 👉 [![Try Aura Now!](https://img.shields.io/badge/Try%20Aura%20Now!-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://ask-aura.streamlit.app/)

---

## 🏗️ Architecture

```
┌─────────────┐
│    User     │
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────┐
│   Streamlit Frontend (app.py)   │
│  ┌──────────────────────────┐   │
│  │  Input Processing Layer   │   │
│  └────────────┬──────────────┘   │
│               │                  │
│       ┌───────┴────────┐         │
│       ▼                ▼         │
│  ┌─────────┐    ┌──────────┐    │
│  │ VADER   │    │LangChain │    │
│  │Sentiment│    │  Memory  │    │
│  └────┬────┘    └─────┬────┘    │
│       │               │          │
│       └───────┬───────┘          │
│               ▼                  │
│     ┌──────────────────┐         │
│     │   LLMChain       │         │
│     │   (ChatGroq)     │         │
│     └────────┬─────────┘         │
└──────────────┼──────────────────┘
               │
               ▼
       ┌──────────────┐
       │  Groq API    │
       │  (Mixtral)   │
       └──────┬───────┘
               │
               ▼
       Response + Sentiment
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8+** installed on your system
- **Groq API Key** (get one at [console.groq.com](https://console.groq.com))
- Basic knowledge of Python and virtual environments

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/hk-kumawat/Aura-Smart-Assistant.git
   cd Aura-Smart-Assistant
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

#### Option 1: Using Streamlit Secrets (Recommended for Deployment)

1. Create a `.streamlit` directory in the project root:
   ```bash
   mkdir .streamlit
   ```

2. Create a `secrets.toml` file inside `.streamlit/`:
   ```bash
   touch .streamlit/secrets.toml
   ```

3. Add your API key:
   ```toml
   GROQ_API_KEY = "your_groq_api_key_here"
   ```

#### Option 2: Using Environment Variables (For Local Development)

1. Create a `.env` file in the project root:
   ```bash
   touch .env
   ```

2. Add your API key:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

3. Update `app.py` line 14 to use the `.env` file:
   ```python
   groq_api_key = os.environ["GROQ_API_KEY"]
   ```

---

## 💻 Usage

### Running the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### Using Aura

1. **Type your question** in the text area
2. **Click Send** or press `Ctrl+Enter`
3. **Watch Aura respond** with sentiment-aware emojis:
   - 😊 Positive sentiment detected
   - 😔 Negative sentiment detected
   - 🙂 Neutral sentiment

### Example Conversations

```
You: I'm so excited about learning AI! Can you help me?
Aura: 😊 Absolutely! I'd be delighted to help you learn about AI...

You: I'm having trouble understanding neural networks
Aura: 😔 I understand it can be challenging. Let me break it down...

You: What is machine learning?
Aura: 🙂 Machine learning is a subset of artificial intelligence...
```

---

## 🛠️ Technologies Used

| Technology | Purpose | Version |
|------------|---------|---------|
| **Python** | Core programming language | 3.8+ |
| **Streamlit** | Web framework for UI | Latest |
| **LangChain** | LLM orchestration and memory | Latest |
| **LangChain-Groq** | Groq integration for LangChain | Latest |
| **Groq API** | High-performance LLM inference (Mixtral-8x7B) | API |
| **VADER Sentiment** | Sentiment analysis engine | Latest |
| **python-dotenv** | Environment variable management | Latest |

### Dependencies

```
streamlit
langchain
langchain-groq
python-dotenv
vaderSentiment
```

---

## 📁 Project Structure

```
Aura-Smart-Assistant/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── LICENSE               # MIT License
│
├── .streamlit/           # Streamlit configuration (not in repo)
│   └── secrets.toml      # API keys (gitignored)
│
└── .env                  # Environment variables (gitignored)
```

---

## 🧠 How It Works

### 1. User Input Processing
```python
user_question = st.text_area("Ask a question:", key="user_input")
```
User types a message in the Streamlit text area.

### 2. Sentiment Analysis
```python
sentiment = analyze_sentiment(user_question)
# Returns: {'neg': 0.0, 'neu': 0.5, 'pos': 0.5, 'compound': 0.6}
```
VADER analyzes the emotional tone of the input.

### 3. LLM Processing with Memory
```python
response_text = llm_chain.run(input=user_question)
```
The question is sent to Groq's Mixtral model via LangChain, with conversation history included.

### 4. Response Enhancement
```python
if sentiment_label == "positive":
    response_text = f"😊 {response_text}"
```
Response is prefixed with appropriate emoji based on sentiment.

### 5. Memory Update
```python
st.session_state.conversation_memory.chat_memory.add_user_message(user_question)
st.session_state.conversation_memory.chat_memory.add_ai_message(response_text)
```
Conversation history is updated for context in future exchanges.

---

## 🔧 Troubleshooting

### Common Issues

#### ❌ API Key Error
```
Error: GROQ_API_KEY not found
```
**Solution**: Ensure your API key is correctly set in `.streamlit/secrets.toml` or `.env`

#### ❌ Module Not Found
```
ModuleNotFoundError: No module named 'langchain_groq'
```
**Solution**:
```bash
pip install --upgrade -r requirements.txt
```

#### ❌ Port Already in Use
```
Error: Address already in use
```
**Solution**:
```bash
streamlit run app.py --server.port 8502
```

#### ❌ Slow Responses
**Solution**: Check your internet connection or Groq API status at [status.groq.com](https://status.groq.com)

---

## 🚀 Future Enhancements

- [ ] **Voice Integration** - Add speech-to-text and text-to-speech capabilities
- [ ] **Multi-Language Support** - Expand to support conversations in multiple languages
- [ ] **Persistent Memory** - Optional database storage for long-term conversation history
- [ ] **Custom Personality Modes** - Allow users to select different assistant personalities
- [ ] **Advanced Analytics** - Dashboard showing conversation statistics and sentiment trends
- [ ] **Export Conversations** - Download chat history as PDF or text
- [ ] **Plugin System** - Integration with calendars, weather, news APIs, etc.
- [ ] **Model Selection** - Allow users to choose between different LLM models
- [ ] **Conversation Branching** - Explore alternative conversation paths

---

## 🤝 Contributing

Contributions are what make the open-source community amazing! Any contributions you make are **greatly appreciated**.

### How to Contribute

1. **Fork** the repository
2. **Create** a feature branch
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit** your changes
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push** to the branch
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open** a Pull Request

### Contribution Guidelines

- Follow PEP 8 style guidelines for Python code
- Add comments to explain complex logic
- Update documentation for any new features
- Test thoroughly before submitting

---

## 📝 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

---

## 👤 Contact

**Harshal Kumawat** - AI/ML Enthusiast & Developer

[![GitHub](https://img.shields.io/badge/GitHub-hk--kumawat-181717?style=for-the-badge&logo=github)](https://github.com/hk-kumawat)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Harshal%20Kumawat-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/harshal-kumawat/)
[![Email](https://img.shields.io/badge/Email-harshalkumawat100@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:harshalkumawat100@gmail.com)

**Project Link**: [https://github.com/hk-kumawat/Aura-Smart-Assistant](https://github.com/hk-kumawat/Aura-Smart-Assistant)

---

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Groq](https://groq.com/) for blazing-fast LLM inference
- [LangChain](https://www.langchain.com/) for conversation management
- [VADER Sentiment](https://github.com/cjhutto/vaderSentiment) for sentiment analysis
- All contributors and users of Aura!

---

<div align="center">

### ⭐ Don't forget to star this repo if you find it useful!

**"Smart conversations start with a single question."**

Made with ❤️ by [Harshal Kumawat](https://github.com/hk-kumawat)

<p align="right">
  <a href="#readme-top">⬆️ Back to top</a>
</p>

</div>
