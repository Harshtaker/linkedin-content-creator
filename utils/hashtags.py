# utils/hashtags.py
import yake

def generate_hashtags(text, max_hashtags=5):
    kw_extractor = yake.KeywordExtractor(lan="en", n=1, dedupLim=0.9, top=max_hashtags)
    keywords = kw_extractor.extract_keywords(text)
    tags = []
    for kw, score in keywords:
        tag = "".join(ch for ch in kw.strip().lower() if ch.isalnum())
        if tag:
            tags.append("#" + tag)
    return tags if tags else ["#insight", "#learning"]
