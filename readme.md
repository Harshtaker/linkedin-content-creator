# 💼 LinkedIn Content Creator

A **fast, free, and hybrid LinkedIn post generator** built with Streamlit.  
Generates professional, motivational, or educational LinkedIn posts **instantly**, with optional AI enhancement for better text quality. Hashtags are generated automatically.  

---

## **Features**

- **Fast Offline Generation:** Uses template-based text for instant post creation.  
- **Optional AI Enhancement:** Enhance your post using lightweight AI (DistilGPT-2 via Hugging Face API) for more natural output.  
- **Word Length Control:**  
  - Short → ~30 words  
  - Medium → ~50 words  
  - Long → ~80 words  
- **Automatic Hashtags:** Extracts relevant hashtags from your post.  
- **Download Button:** Export post + hashtags as `.txt`.  
- **Clean UI:** Streamlit app, user-friendly, and fully responsive.

---

## **Installation**

1. Clone this repository:

```bash
git clone https://github.com/yourusername/linkedin-content-creator.git
cd linkedin-content-creator

2.Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3.Install dependencies:
pip install -r requirements.txt

Usage

Run the Streamlit app:
streamlit run app.py

Enter Topic, Profile, Tone, Length.
Optional: Check Enhance with AI for AI-paraphrased posts.
Click Generate Post → see post + hashtags.
Download as .txt using the download button

Testing Data (Examples)
| Topic                    | Profile               | Tone         | Length |
| ------------------------ | --------------------- | ------------ | ------ |
| AI in startups           | Student, Entrepreneur | Motivational | Short  |
| Team collaboration       | Developer, Manager    | Professional | Medium |
| Personal growth lessons  | Student               | Motivational | Long   |
| Remote work productivity | Professional          | Educational  | Medium |
| Learning from failure    | Entrepreneur          | Motivational | Short  |

Project Structure
linkedin-content-creator/
│
├── app.py                 # Streamlit main app
├── requirements.txt       # Python dependencies
├── utils/
│   ├── generator.py       # Post generator (offline + optional API)
│   ├── hashtags.py        # Hashtag extractor
│   └── prompt_templates.py# Post templates
├── README.md
└── LICENSE
