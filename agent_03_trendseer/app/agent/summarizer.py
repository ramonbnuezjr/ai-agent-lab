from dotenv import load_dotenv
from app.utils.prompt_loader import load_prompt
from openai import OpenAI
import os

load_dotenv()  # Loads from .env

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_article(article_text):
    prompt_template = load_prompt("prompts/summarize_prompt.txt")
    prompt = prompt_template.replace("{ARTICLE_TEXT}", article_text)

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
