import os

TEXT_API_URL = "https://openrouter.ai/api/v1/chat/completions"
TEXT_API_KEY = os.getenv("TEXT_API_KEY", "")
HUGGINGFACE_API = os.getenv("HUGGINGFACE_API", "")
MODEL_NAME = "mistralai/mixtral-8x7b"
