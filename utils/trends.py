# utils/trends.py
import requests

def get_trending_topics():
    """
    Fetch top trending topics (free API version using Hacker News)
    Returns a list of dictionaries with title and URL
    """
    try:
        response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
        response.raise_for_status()
        story_ids = response.json()[:10]

        trends = []
        for sid in story_ids:
            story = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{sid}.json").json()
            if story and "title" in story:
                trends.append({
                    "title": story["title"],
                    "url": story.get("url", "")
                })

        return trends

    except Exception as e:
        return [{"title": f"Error fetching trends: {e}", "url": ""}]
