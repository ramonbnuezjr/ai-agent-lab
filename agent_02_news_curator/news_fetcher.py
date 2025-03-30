# news_fetcher.py

import requests
from config import TAVILY_API_KEY

TAVILY_API_URL = "https://api.tavily.com/search"

def fetch_news(limit=5):
    params = {
        "api_key": TAVILY_API_KEY,
        "query": "latest AI news",
        "search_depth": "basic",
        "include_answer": False,
        "include_images": False,
        "num_results": limit,
    }

    try:
        response = requests.post(TAVILY_API_URL, json=params)
        response.raise_for_status()
        results = response.json().get("results", [])

        articles = []
        for item in results:
            articles.append({
                "title": item.get("title"),
                "url": item.get("url"),
                "source": item.get("source"),
                "published": item.get("published"),
            })

        return articles

    except Exception as e:
        print(f"[NewsFetcher] Error fetching news: {e}")
        return []
