# main.py

from news_fetcher import fetch_news
from news_processor import process_story
from storage import save_stories
from datetime import date

def main():
    print("[Agent 02] Starting News Curator...")

    news_items = fetch_news(limit=5)
    curated_stories = []

    for story in news_items:
        result = process_story(story)
        if result:  # Only save stories deemed significant
            curated_stories.append(result)

    if curated_stories:
        save_stories(curated_stories, date.today())
        print(f"[Agent 02] Saved {len(curated_stories)} stories.")
    else:
        print("[Agent 02] No significant stories today.")

if __name__ == "__main__":
    main()
