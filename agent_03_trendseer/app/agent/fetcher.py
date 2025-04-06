from dotenv import load_dotenv
from tavily import TavilyClient
import os

load_dotenv()  # Loads from .env

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_news(query):
    results = client.search(query=query, search_depth="advanced", include_answer=False)
    return results['results']
