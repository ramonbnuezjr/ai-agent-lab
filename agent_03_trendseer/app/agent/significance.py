from dotenv import load_dotenv
import os
from openai import OpenAI
from app.utils.prompt_loader import load_prompt

load_dotenv()  # Loads from .env

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def assess_significance(summary_text: str) -> str:
    prompt_template = load_prompt("prompts/significance_prompt.txt")
    prompt = prompt_template.replace("{SUMMARY_TEXT}", summary_text)

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
