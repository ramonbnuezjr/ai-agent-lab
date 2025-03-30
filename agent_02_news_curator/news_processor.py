# news_processor.py

from config import client
import openai

def load_prompt(filename, **kwargs):
    try:
        with open(f"prompts/{filename}", "r", encoding="utf-8") as f:
            prompt = f.read()
        return prompt.format(**kwargs)
    except Exception as e:
        print(f"[NewsProcessor] Failed to load prompt '{filename}': {e}")
        return ""

def process_story(story):
    try:
        context = {
            "title": story["title"],
            "url": story["url"]
        }

        # Step 1 – Significance
        significance_prompt = load_prompt("significance_prompt.txt", **context)
        sig_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": significance_prompt}],
            temperature=0
        )
        score_str = sig_response.choices[0].message.content.strip()
        significance_score = float(score_str)

        if significance_score < 6:
            return None

        # Step 2 – Summarization
        summarize_prompt = load_prompt("summarize_prompt.txt", **context)
        summary_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": summarize_prompt}],
            temperature=0.7
        )
        summary = summary_response.choices[0].message.content.strip()

        # Step 3 – Tagging
        tagging_prompt = load_prompt("tagging_prompt.txt", **context)
        tags_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": tagging_prompt}],
            temperature=0.5
        )
        tags_raw = tags_response.choices[0].message.content.strip()
        tags = [t.strip("# ").strip() for t in tags_raw.split(",")]

        return {
            "title": story["title"],
            "url": story["url"],
            "source": story.get("source"),
            "published": story.get("published"),
            "summary": summary,
            "significance_score": significance_score,
            "tags": tags
        }

    except Exception as e:
        print(f"[NewsProcessor] Error processing story: {e}")
        return None
