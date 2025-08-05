import streamlit as st
from crewai import Crew
from agents.info_extractor import info_extractor
from agents.comparator import comparator
from agents.recommender import recommender
from tasks.task_creator import create_tasks
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="🛍️ Product Comparison Bot", layout="wide")

st.markdown(
    "<h1 style='text-align: center;'>🛍️ Smart Product Comparison Bot</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center color:#D3F527;'>Compare two products side-by-side based on features, reviews, and more!</p>",
    unsafe_allow_html=True
)

with st.form("comparison_form"):
    col1, col2 = st.columns(2)
    with col1:
        product1 = st.text_input("🔍 Enter First Product Name", placeholder="e.g., iPhone 14 Pro")
    with col2:
        product2 = st.text_input("🔍 Enter Second Product Name", placeholder="e.g., Samsung S23 Ultra")
    
    submitted = st.form_submit_button("Compare Products 🚀")

if submitted:
    if not product1 or not product2:
        st.warning("⚠️ Please enter both product names.")
    else:
        with st.spinner("Fetching and comparing products... ⏳"):
            tasks = create_tasks(info_extractor, comparator, recommender, product1, product2)
            crew = Crew(
                agents=[info_extractor, comparator, recommender],
                tasks=tasks,
                verbose=True
            )
            result = crew.kickoff()
        st.success("✅ Comparison Complete!")
        st.markdown("### 🧠 Recommendation:")
        st.markdown(
            f"<div style='background-color: #F54927; padding: 10px; border-radius: 5px;'>{result}</div>", 
            unsafe_allow_html=True
        )
