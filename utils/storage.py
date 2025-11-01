# utils/storage.py
import json
import os
from datetime import datetime

DATA_FILE = "data/posts.json"
EXPORT_DIR = "exports"

os.makedirs("data", exist_ok=True)
os.makedirs(EXPORT_DIR, exist_ok=True)

def load_posts():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_post(text, topic=None, tone=None, hashtags=None):
    posts = load_posts()
    entry = {
        "id": int(datetime.utcnow().timestamp()*1000),
        "text": text,
        "topic": topic,
        "tone": tone,
        "hashtags": hashtags or [],
        "created_at": datetime.utcnow().isoformat() + "Z"
    }
    posts.append(entry)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)
    return entry

def export_post_txt(text, filename=None):
    if not filename:
        filename = f"post_{int(datetime.utcnow().timestamp())}.txt"
    path = os.path.join(EXPORT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path
