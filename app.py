import streamlit as st
from utils.generator import generate_post
from utils.hashtags import generate_hashtags

st.set_page_config(page_title="LinkedIn Content Creator", layout="centered")

st.markdown("<h1 style='text-align:center;'>💼 LinkedIn Content Creator</h1>", unsafe_allow_html=True)
st.write("Generate professional LinkedIn posts instantly — fast, free, and optionally enhanced with AI.")

with st.form("input_form"):
    topic = st.text_input("🧩 Topic", placeholder="e.g. AI startups, Team collaboration")
    profile = st.text_input("👤 Profile context", placeholder="e.g. Student, Developer, Entrepreneur")
    tone = st.selectbox("🎭 Tone", ["Professional", "Motivational", "Educational", "Friendly"])
    length = st.radio("📏 Length", ["Short", "Medium", "Long"], index=1)
    enhance = st.checkbox("⚡ Enhance with AI (optional, may be slightly slower)")
    submitted = st.form_submit_button("🚀 Generate Post")

if submitted:
    if not topic.strip():
        st.warning("Please enter a topic first!")
    else:
        with st.spinner("Generating your LinkedIn post..."):
            post = generate_post(topic, profile, tone, length, enhance)
            hashtags = generate_hashtags(post)
        st.success("✅ Post Generated Successfully!")
        st.markdown(f"### ✍️ Your Post:\n{post}")
        st.markdown("### 🔖 Hashtags:")
        st.markdown(" ".join(hashtags))
        st.download_button("⬇️ Download as .txt", data=post + "\n\n" + " ".join(hashtags), file_name="linkedin_post.txt", mime="text/plain")
