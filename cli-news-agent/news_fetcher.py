import requests
from config import TAVILY_API_KEY

def get_ai_news():
    url = "https://api.tavily.com/search"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "api_key": TAVILY_API_KEY,
        "query": "latest news on artificial intelligence",
        "search_depth": "basic",  # or "advanced" (uses more credits)
        "include_answer": False,
        "include_images": False,
        "max_results": 5
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    news_list = []
    for result in data.get("results", []):
        news_list.append({
            "title": result["title"],
            "url": result["url"],
            "description": result.get("content", "")
        })

    return news_list

