from dotenv import load_dotenv
import os
from openai import OpenAI
from app.utils.prompt_loader import load_prompt

load_dotenv()  # Loads from .env

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_tags(summary_text: str) -> list:
    prompt_template = load_prompt("prompts/tag_extraction_prompt.txt")
    prompt = prompt_template.replace("{SUMMARY_TEXT}", summary_text)

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    # Basic processing: split by comma, strip whitespace
    tags = response.choices[0].message.content.strip().split(',')
    return [tag.strip() for tag in tags if tag.strip()]
