# utils/prompt_templates.py
"""
Defines reusable prompt templates for generating LinkedIn-style posts.
You can easily extend this dictionary with custom tones, formats, or styles.
"""

TEMPLATES = {
    "default": (
        "Write a concise, engaging LinkedIn post about '{topic}'. "
        "The post should match the tone: {tone}, and reflect the personality of a {profile}. "
        "Avoid hashtags or emojis. Keep it natural and authentic."
    ),

    "motivational": (
        "Create a motivational LinkedIn post about {topic}. "
        "The tone should be inspiring and personal, written from the perspective of a {profile}. "
        "Encourage others to take action or reflect."
    ),

    "educational": (
        "Write an educational and informative LinkedIn post explaining {topic}. "
        "The tone should be professional yet approachable, suitable for a {profile}. "
        "Keep it structured with clear takeaways."
    ),

    "storytelling": (
        "Write a short storytelling-style LinkedIn post about {topic}. "
        "The tone should be emotional and reflective, showing the personal journey of a {profile}. "
        "Make it relatable and end with a simple call to action."
    ),

    "announcement": (
        "Write a LinkedIn announcement post for a {profile} sharing news about {topic}. "
        "The tone should be confident, professional, and positive. "
        "Highlight key points briefly and clearly."
    ),
}
