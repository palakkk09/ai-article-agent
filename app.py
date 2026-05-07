

import time
import streamlit as st

from agents.article_agent import ArticleAgent

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Content Generator",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ----------------

hide_streamlit_style = """
<style>
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

[data-testid="stToolbar"] {
    display: none;
}

.block-container {
    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}

.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    font-size: 16px;
}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.title("AI Content Generation Agent")

st.markdown(
    "Generate articles, summaries, LinkedIn posts, Twitter threads, and Instagram Posts using AI agents."
)

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.header("Agent Activity")

    status_box = st.empty()

# ---------------- AGENT ----------------

agent = ArticleAgent()

# ---------------- INPUT ----------------

topic = st.text_input(
    "Enter Topic",
    placeholder="Example: Future of AI Agents"
)

# ---------------- OUTPUT TYPE ----------------

output_type = st.selectbox(
    "Select Output Type",
    [
        "Full Article",
        "Short Summary",
        "Executive Summary",
        "LinkedIn Post",
        "Twitter Thread",
        "Instagram Post"
    ]
)

# ---------------- BUTTON ----------------

if st.button("Generate Content"):

    if topic:

        status_box.info("Agent Started...")
        time.sleep(1)

        status_box.info("Searching Internet...")
        time.sleep(1)

        status_box.info("Reading Articles...")
        time.sleep(1)

        status_box.info("Generating Content...")

        result = agent.generate_content(topic, output_type)

        status_box.success("Content Generated Successfully")

        st.markdown("---")

        st.markdown(result)

    else:

        st.warning("Please enter a topic.")
