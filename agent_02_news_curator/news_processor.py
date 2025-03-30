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

def should_summarize(title, url):
    """Uses GPT to decide if this URL is likely a real article."""
    check_prompt = f"""
You're an AI assistant evaluating whether this page is likely a standalone news article.

Title: {title}
URL: {url}

If this page appears to be a category, topic, homepage, or a collection page, reply with "NO".
If it appears to be a valid standalone news article with substantive content, reply with "YES".
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": check_prompt}],
            temperature=0
        )
        result = response.choices[0].message.content.strip().lower()
        return result.startswith("yes")

    except Exception as e:
        print(f"[NewsProcessor] Error in should_summarize(): {e}")
        return False

def process_story(story):
    try:
        context = {
            "title": story["title"],
            "url": story["url"]
        }

        # Step 0 – GPT check for valid article type
        if not should_summarize(context["title"], context["url"]):
            print(f"[NewsProcessor] Skipping non-article: {context['url']}")
            return None

        # Step 1 – Summarization first (before significance)
        summarize_prompt = load_prompt("summarize_prompt.txt", **context)
        summary_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": summarize_prompt}],
            temperature=0.7
        )
        summary = summary_response.choices[0].message.content.strip()

        # 🚨 HARD CHECK – Don't proceed if summary is invalid
        if summary.lower().startswith("not a valid article"):
            print(f"[NewsProcessor] Skipping fake summary for: {story['url']}")
            return None

        # Step 2 – Significance scoring
        significance_prompt = load_prompt("significance_prompt.txt", **context)
        sig_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": significance_prompt}],
            temperature=0
        )
        score_str = sig_response.choices[0].message.content.strip()
        significance_score = float(score_str)

        if significance_score < 6:
            print(f"[NewsProcessor] Skipping low-significance story: {context['title']} ({significance_score})")
            return None

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
