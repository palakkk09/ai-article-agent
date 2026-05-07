
import time
import streamlit as st
from agents.article_agent import ArticleAgent

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Article Generator",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- HIDE STREAMLIT DEFAULT UI ----------------

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

[data-testid="stDecoration"] {
    display: none;
}

[data-testid="stStatusWidget"] {
    visibility: hidden;
}

[data-testid="stDeployButton"] {
    display: none;
}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.title("AI Article Generation Agent")

st.markdown(
    "Turn a topic into a polished, publication-ready article with AI-driven research"
)

# ---------------- SIDEBAR ----------------

with st.sidebar:
    st.header("Agent Activity")

    status_box = st.empty()

# ---------------- AGENT ----------------

agent = ArticleAgent()

# ---------------- INPUT ----------------

topic = st.text_input(
    "Article Topic",
    placeholder="Example: Future of AI Agents"
)

# ---------------- BUTTON ----------------

if st.button("Generate Article"):

    if topic:

        # STEP 1
        status_box.info("Agent Started...")
        time.sleep(1)

        # STEP 2
        status_box.info("Searching Internet...")
        time.sleep(1)

        # STEP 3
        status_box.info("Reading Articles...")
        time.sleep(1)

        # STEP 4
        status_box.info("Generating Article...")
        
        result = agent.generate_article(topic)

        # STEP 5
        status_box.success("Article Generated Successfully")

        # ---------------- OUTPUT ----------------

        st.markdown("---")

        st.markdown(result)