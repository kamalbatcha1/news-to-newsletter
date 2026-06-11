import streamlit as st
from pipeline import run_pipeline

st.set_page_config(page_title="News Intelligence System", layout="wide")

st.title("📰 AI News Intelligence Dashboard")

articles = run_pipeline()

st.success(f"Loaded {len(articles)} articles")

for a in articles:

    st.subheader(f"[{a['category']}] {a['title']}")
    st.write("**Score:**", a["score"])
    st.write("**Summary:**", a["summary"])
    st.write(f"[Read more]({a['link']})")
    st.markdown("---")