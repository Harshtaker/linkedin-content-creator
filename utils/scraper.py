# utils/scraper.py
import requests
from bs4 import BeautifulSoup
import time
import json
import os

CACHE_FILE = "data/trends.json"
os.makedirs("data", exist_ok=True)

def fetch_reddit_top(subreddit="technology", limit=10):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit={limit}"
    headers = {"User-Agent": "Mozilla/5.0 (compatible; LCC/1.0)"}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        data = r.json()
        titles = [child['data']['title'] for child in data['data']['children']]
        return titles
    except Exception as e:
        print("Reddit fetch failed:", e)
        return []

def fetch_google_news_topics(query="technology", count=10):
    # Simple Google News scraping via the "news" search results (may be fragile)
    url = f"https://news.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0 (compatible; LCC/1.0)"}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        items = soup.select("article h3")
        titles = [it.get_text().strip() for it in items][:count]
        return titles
    except Exception as e:
        print("Google News fetch failed:", e)
        return []

def fetch_trending_topics(keyword="technology"):
    # Combine sources and cache
    reddit = fetch_reddit_top(subreddit="technology", limit=8)
    news = fetch_google_news_topics(query=keyword, count=8)
    topics = list(dict.fromkeys(reddit + news))  # unique preserving order
    # Save cache
    payload = {"fetched_at": int(time.time()), "topics": topics}
    try:
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
    except:
        pass
    return topics

if __name__ == "__main__":
    print(fetch_trending_topics("AI"))
