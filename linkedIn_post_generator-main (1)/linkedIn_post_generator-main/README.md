🧠 AI-Powered LinkedIn Post Generator
A Streamlit-based web app that analyzes previously written LinkedIn posts to generate new, personalized, and engaging content tailored to specific topics, tones, and audience preferences.

This project uses LLMs (Groq + LLaMA 3 via LangChain), few-shot learning, and content metadata analysis to deliver context-aware post generation in multiple languages and styles.

🚀 Features
🔍 Post Analysis Engine
Processes raw LinkedIn post data (JSON format)

Cleans text (removes Unicode errors, emojis)

Extracts metadata:

Number of lines

Language (English or Hinglish)

Tags (topics inferred from content)

Unifies and categorizes similar tags for consistent filtering

💬 Post Generator
Generates custom LinkedIn posts based on:

✅ Selected topic/tag

🌐 Preferred language (English, Hindi, Hinglish)

📏 Desired length (Short, Medium, Long)

Uses few-shot prompting from real-world examples to match tone and style

🧪 LLM Integration
Powered by Groq LLaMA 3 through LangChain

Uses prompt templates and JSON parsers for robust content generation and tag normalization

🖥️ Frontend Interface
Built with Streamlit

Intuitive UI for selecting post options

One-click generation experience

🧰 Tech Stack
Technology	Purpose
Streamlit	UI/UX for post generation
LangChain	LLM framework for chaining prompts/responses
Groq + LLaMA 3	Large Language Model for text generation
Python	Core logic and data processing
Pandas	Filtering and metadata enrichment
JSON	Data storage and formatting
dotenv	Environment variable management
