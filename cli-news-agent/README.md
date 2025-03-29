# 🧠 CLI News Agent

An AI-powered command-line assistant that fetches and summarizes the latest news on Artificial Intelligence using the **Tavily API** and **OpenAI GPT-3.5**.

This agent is designed to run on a Raspberry Pi 5 in a headless environment and serve as a simple, modular foundation for more advanced autonomous agents.

---

## �� Features

- Fetches top 5 AI-related news articles
- Summarizes articles in 2–3 sentences using GPT
- CLI-based interaction
- Modular code for easy expansion
- Environment-based API key security

---

## 🧱 Project Structure

cli-news-agent/ ├── main.py ├── news_fetcher.py ├── summarizer.py ├── config.py ├── .env.example ├── requirements.txt |── README.md


---

## ⚙️ Setup Instructions

1. **Clone the repo**
2. **Navigate into the project**
3. **Create virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Set up your .env
cp .env.example .env
nano .env  # Add your OpenAI and Tavily API keys

## Run the Agent
python main.py

## Example Usage
🤖 Welcome to AI News Assistant!

[1] AI transforming chip design at Intel
    https://example.com

🔹 Summarize this? (y/n): y

📝 Summary: Intel is using AI to speed up chip development by 40%...

```bash

## Environment Variables
Key	        Purpose
OPENAI_API_KEY	Access GPT models
TAVILY_API_KEY	Fetch real-time news

## Dependencies
openai
requests
python-dotenv
