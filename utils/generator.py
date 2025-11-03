# utils/generator.py
import requests
from config import TEXT_API_KEY, TEXT_API_URL, MODEL_NAME

API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {TEXT_API_KEY}",
    "Content-Type": "application/json"
}

def generate_post(topic, profile="Professional", tone="Professional", length="Medium"):
    """
    Generates a LinkedIn-style post using OpenRouter API with contextual info.
    """
    length_map = {"Short": 40, "Medium": 70, "Long": 100}
    max_words = length_map.get(length, 70)

    prompt = f"""
    Search about "{topic}" on the internet and write a detailed, engaging LinkedIn post (~{max_words} words).
    Maintain a {tone} tone and write from a {profile} perspective.
    Include a small intro, insight, and a short CTA at the end.
    Use proper LinkedIn formatting (line breaks, emojis optional).
    """

    payload = {
        "model": "gpt-4o-mini",  # or "mistralai/mistral-7b-instruct"
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.8,
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=40)
        response.raise_for_status()
        data = response.json()

        if "choices" in data and len(data["choices"]) > 0:
            text = data["choices"][0]["message"]["content"].strip()
            return text
        else:
            return "Couldn't generate a detailed post, please try again."
    except Exception as e:
        print("Error generating post:", e)
        return "AI post generation failed. Please check your API key or try again."
