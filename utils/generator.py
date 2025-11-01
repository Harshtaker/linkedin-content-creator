import random
import requests
from .prompt_templates import TEMPLATES

# -------------------------
# Offline Template Generator
# -------------------------
def _expand_text(base, length):
    extra_phrases = [
        "It’s amazing how small steps can lead to big results.",
        "Every experience brings new insights and opportunities.",
        "Curiosity and consistency always pay off in the long run.",
        "Collaboration and learning are key to success.",
        "Growth happens when you challenge yourself and adapt."
    ]
    if length == "Short":
        return base
    elif length == "Medium":
        return base + " " + " ".join(random.sample(extra_phrases, 2))
    elif length == "Long":
        return base + " " + " ".join(random.sample(extra_phrases, 4))
    return base

def simple_template_generator(topic, profile, tone, length):
    hooks = [
        "Here's a quick thought:",
        "Reflecting today:",
        "Sharing a small insight:",
        "A learning from recent work:"
    ]
    bodies = [
        f"While working on {topic}, I realized small consistent actions lead to big results.",
        f"{topic} taught me that adaptability matters more than perfect planning.",
        f"Exploring {topic} reminded me that persistence and curiosity always pay off."
    ]
    ctas = [
        "Would love to hear your thoughts!",
        "What are your experiences?",
        "Share your perspective below."
    ]
    text = f"{random.choice(hooks)} {random.choice(bodies)} {random.choice(ctas)}"
    text = _expand_text(text, length)
    # Ensure precise word count
    words = text.split()
    target = {"Short": 30, "Medium": 50, "Long": 80}.get(length, 50)
    if len(words) < target:
        text += " " + " ".join(random.choices(words, k=target - len(words)))
    elif len(words) > target + 10:
        text = " ".join(words[:target])
    return text.strip()

# -------------------------
# Optional API Enhancer
# -------------------------
HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/distilgpt2"
HUGGINGFACE_TOKEN = ""  # Optional: your Hugging Face token

def enhance_with_api(text):
    if not HUGGINGFACE_TOKEN:
        return text  # skip enhancement if no token
    headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}
    data = {"inputs": text, "parameters": {"max_new_tokens": 50}}
    try:
        response = requests.post(HUGGINGFACE_API_URL, headers=headers, json=data, timeout=5)
        result = response.json()
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]
        return text
    except Exception as e:
        print("API enhancement failed:", e)
        return text

# -------------------------
# Public Generator Function
# -------------------------
def generate_post(topic, profile="Professional", tone="Motivational", length="Medium", enhance=False):
    # 1️⃣ Offline template generation (fast)
    text = simple_template_generator(topic, profile, tone, length)
    
    # 2️⃣ Optional API enhancement
    if enhance:
        text = enhance_with_api(text)
    return text
