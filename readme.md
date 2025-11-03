# 💼 LinkedIn Content Creator

An AI-powered **LinkedIn post generator and scheduler** built with **Streamlit**, designed to help professionals, students, and creators generate high-quality LinkedIn posts, hashtags, and weekly content plans effortlessly.

---

## 🚀 Features

### 🧠 AI Post Generator
- Generate professional, friendly, motivational, or educational LinkedIn posts.
- Supports multiple profiles (Professional, Student, Entrepreneur, Marketer, Developer).
- Automatically suggests trending hashtags.
- Fetches a relevant image for your topic using **Stable Diffusion (via Hugging Face Diffusers)**.

### 📅 Content Planner
- Enter up to 7 topics and get a **weekly LinkedIn posting plan**.
- Suggests best posting times based on your profile type.
- Easy-to-read weekly schedule displayed directly in the app.

### 🗓️ Post Scheduler
- Schedule and manage your LinkedIn posts.
- Optionally auto-generate post content + hashtags.
- Download your schedule as **CSV** or **DOCX** files for offline access.

---

## 🧩 Tech Stack

| Category | Technology |
|-----------|-------------|
| Frontend | [Streamlit](https://streamlit.io) |
| Backend | Python |
| AI Model | [OpenRouter](https://openrouter.ai) (Mixtral 8x7B) |
| Image Generation | Hugging Face Diffusers (Stable Diffusion) |
| File Export | Python-docx, Pandas |
| Environment Management | Virtualenv / venv |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone this repository
```bash
git clone https://github.com/Harshtaker/linkedin-content-creator.git
cd linkedin-content-creator

2️⃣ Create a virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On Mac/Linux

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set up environment variables
Create a .env file in the project root and add your keys (example below):
OPENROUTER_API_KEY=your_openrouter_api_key
HUGGINGFACE_TOKEN=your_huggingface_token


🔒 These keys are kept safe and not pushed to GitHub (listed in .gitignore).

5️⃣ Run the app
streamlit run app.py

Then open the provided local URL (e.g. http://localhost:8501) in your browser.

📁 Project Structure
linkedin-content-creator/
│
├── app.py                    # Main Streamlit app
├── config.py                 # Configuration (reads from .env)
├── requirements.txt          # Dependencies
│
├── utils/
│   ├── generator.py          # OpenRouter-based text generation
│   ├── hashtags.py           # Hashtag generator logic
│   ├── image_fetch.py        # Hugging Face Diffusers image fetch
│   └── calendar.py           # Weekly scheduler & best time logic
│
└── data/                     # (Optional) local cache or post data

🧾 Example Usage

Enter your topic (e.g. “Power of Networking”).
Choose tone, profile type, and length.
Click Generate Post → AI creates your post, hashtags, and image.
Plan your week under 📅 Content Planner tab.
Download your post plan in CSV/DOCX format.

🤝 Contributing
Feel free to fork, improve, and create pull requests!
If you find bugs or want new features, open an Issue.

🧑‍💻 Author

Harsh Shukla
Built with ❤️ using OpenRouter + Streamlit
📧 https://github.com/Harshtaker
