from news_fetcher import get_ai_news
from summarizer import summarize_text

def run_chatbot():
    print("🤖 Welcome to AI News Assistant!")
    articles = get_ai_news()

    for idx, article in enumerate(articles, start=1):
        print(f"\n[{idx}] {article['title']}")
        print(f"    {article['url']}")
        user_input = input("🔹 Summarize this? (y/n): ").strip().lower()

        if user_input == "y":
            print("🧠 Summarizing...")
            summary = summarize_text(article['description'] or article['title'])
            print(f"📝 Summary: {summary}")

if __name__ == "__main__":
    run_chatbot()
