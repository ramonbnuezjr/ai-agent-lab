import os
import json
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Imports from your app structure
from app.agent.fetcher import search_news
from app.agent.summarizer import summarize_article
from app.agent.tagger import extract_tags
from app.agent.significance import assess_significance
from app.db.database import connect_db

# Connect to SQLite DB
conn = connect_db()
cursor = conn.cursor()

# Load topics from JSON
try:
    with open("data/topics.json", "r") as f:
        topics = json.load(f)
        print(f"🔎 Loaded topics: {list(topics.keys())}")
except Exception as e:
    print(f"❌ Failed to load topics.json: {e}")
    exit(1)

# Define main processing function
def process_domain(domain, query):
    print(f"[{datetime.now()}] 🔍 Processing domain: {domain}")

    articles = search_news(query)
    if not articles:
        print(f"⚠️  No articles returned for domain: {domain}")
        return

    for article in articles:
        title = article.get("title", "Untitled")
        url = article.get("url")

        # Fallback logic to get usable content
        content = (
            article.get("content") or
            article.get("body") or
            article.get("snippet") or
            article.get("meta_description") or
            title  # fallback to title if nothing else
        )

        if not content or len(content.strip()) < 40:
            print(f"⚠️  Skipped (Too little content): '{title}'")
            continue

        try:
            summary = summarize_article(content)
            tags = extract_tags(summary)
            significance = assess_significance(summary)

            # Save to database
            cursor.execute("""
                INSERT INTO summaries (date, domain, title, summary, tags, raw_json)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                datetime.utcnow().isoformat(),
                domain,
                title,
                summary,
                ", ".join(tags),
                json.dumps({
                    "url": url,
                    "significance": significance,
                    "original": article
                })
            ))
            conn.commit()

            # Save to logs
            date_str = datetime.now().strftime("%Y-%m-%d")
            log_file = f"logs/{domain}_{date_str}.json"
            with open(log_file, "a") as f:
                f.write(json.dumps({
                    "title": title,
                    "summary": summary,
                    "tags": tags,
                    "significance": significance,
                    "url": url
                }) + "\n")

            print(f"✅ Saved: {title[:60]}... → Tags: {tags}")

        except Exception as e:
            print(f"❌ Error processing article '{title}': {e}")

# 🧠 Main loop
if __name__ == "__main__":
    print("🚀 Agent_03 starting...")
    print("📅 Timestamp:", datetime.utcnow().isoformat())
    print("📁 Current working directory:", os.getcwd())

    for domain, query in topics.items():
        process_domain(domain, query)

    print("✅ Agent_03 run complete.")
