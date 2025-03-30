# news_fetcher.py

import requests
from config import TAVILY_API_KEY

def is_valid_article_url(url: str) -> bool:
    """Filters out URLs that point to topic pages, categories, or generic indexes."""
    if not url:
        return False

    bad_keywords = [
        "/tag/", "/tags/", "/topics/", "/category/", "/news/",
        "/search/", "/about/", "/collections/", "/section/"
    ]

    # Reject URLs that contain known category or search paths
    if any(keyword in url.lower() for keyword in bad_keywords):
        return False

    # Reject URLs that are too short (likely homepages or index pages)
    if url.count("/") <= 3:
        return False

    return True

def fetch_news(limit=5):
    print("[NewsFetcher] Fetching AI news from Tavily...")

    try:
        response = requests.post(
            "https://api.tavily.com/search",
            headers={"Authorization": TAVILY_API_KEY},
            json={
                "query": "latest artificial intelligence news",
                "search_depth": "basic",
                "include_answer": False,
                "max_results": limit  # <- use the limit here
            }
        )
        response.raise_for_status()
        data = response.json()

        stories = []
        for item in data.get("results", []):
            url = item.get("url", "")

            if not is_valid_article_url(url):
                print(f"[NewsFetcher] Skipping invalid URL: {url}")
                continue

            stories.append({
                "title": item.get("title"),
                "url": url,
                "source": item.get("source"),
                "published": item.get("published")
            })

        print(f"[NewsFetcher] Returning {len(stories)} valid articles.")
        return stories

    except Exception as e:
        print(f"[NewsFetcher] Error fetching news: {e}")
        return []
