from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def summarize_text(text):
    prompt = f"Summarize this news in 2-3 sentences:\n\n{text}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    summary = response.choices[0].message.content
    return summary.strip()

