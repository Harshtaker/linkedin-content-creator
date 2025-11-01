import re

def generate_hashtags(text, max_hashtags=5):
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    common = ["the", "this", "that", "have", "from", "about", "with", "what", "when"]
    keywords = [w for w in words if w not in common]
    hashtags = list(dict.fromkeys(["#" + w for w in keywords]))[:max_hashtags]
    if not hashtags:
        hashtags = ["#motivation", "#learning", "#growth"]
    return hashtags
