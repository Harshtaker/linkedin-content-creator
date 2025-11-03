# utils/image_fetch.py
import requests
import urllib.parse

def fetch_image_url(query):
    """
    Generates an AI image using Pollinations API based on the topic.
    Free and no API key required.
    """
    try:
        encoded_query = urllib.parse.quote(query)
        # Pollinations image URL
        url = f"https://image.pollinations.ai/prompt/{encoded_query}?width=1024&height=768"

        # Verify the image exists
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return url
        else:
            print("Pollinations returned status:", response.status_code)
            return None
    except Exception as e:
        print("Error fetching image:", e)
        return None
