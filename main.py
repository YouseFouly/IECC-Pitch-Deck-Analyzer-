import os
import streamlit as st
from streamlit_option_menu import option_menu

from gemini_utility import (
    evaluate_pitch_deck,
    analyze_file
)

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Pitch Deck Evaluator",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    selected = option_menu(
        menu_title="Pitch Deck AI",
        options=[
            "Evaluate Deck",
            "Custom Analysis",
            "About"
        ],
        icons=[
            "bar-chart",
            "file-earmark-text",
            "info-circle"
        ],
        menu_icon="rocket-takeoff",
        default_index=0
    )

# ==========================================
# Evaluate Pitch Deck
# ==========================================

if selected == "Evaluate Deck":

    st.title("🚀 AI Pitch Deck Evaluator")

    st.markdown("""
Upload your **PowerPoint (.pptx)** pitch deck and receive professional
VC-style feedback powered by **Gemini 2.5 Pro**.

### The evaluation includes

- ✅ Problem
- ✅ Solution
- ✅ Product
- ✅ Market Opportunity
- ✅ Business Model
- ✅ Competition
- ✅ Traction
- ✅ Team
- ✅ Financials
- ✅ Investment Ask
- ✅ Missing Slides
- ✅ Overall Score
- ✅ Top Improvements
""")

    uploaded_file = st.file_uploader(
        "Upload your Pitch Deck",
        type=["pptx", "pdf"]
    )

    if uploaded_file:

        save_path = os.path.join("uploads", uploaded_file.name)

        os.makedirs("uploads", exist_ok=True)

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success("Pitch deck uploaded successfully.")

        if st.button("Evaluate Pitch Deck", use_container_width=True):

            with st.spinner("Analyzing your pitch deck..."):

                result = evaluate_pitch_deck(save_path)

            st.success("Analysis Complete!")

            st.markdown(result)

# ==========================================
# Custom Analysis
# ==========================================

elif selected == "Custom Analysis":

    st.title("📝 Custom File Analysis")

    uploaded_file = st.file_uploader(
        "Upload a file",
        type=["pptx", "pdf", "docx"]
    )

    prompt = st.text_area(
        "Custom Prompt",
        height=200,
        placeholder="Example:\nEvaluate this deck as if you were a Y Combinator partner."
    )

    if uploaded_file and prompt:

        save_path = os.path.join("uploads", uploaded_file.name)

        os.makedirs("uploads", exist_ok=True)

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        if st.button("Analyze", use_container_width=True):

            with st.spinner("Analyzing..."):

                result = analyze_file(save_path, prompt)

            st.markdown(result)

# ==========================================
# About
# ==========================================

elif selected == "About":

    st.title("ℹ️ About")

    st.markdown("""
# AI Pitch Deck Evaluator

This application uses **Google Gemini 2.5 Pro** and the **Gemini Files API**
to analyze startup pitch decks.

## Features

- 📊 Investor-style evaluation
- 💡 Identify missing slides
- 🎯 Business model feedback
- 📈 Market analysis
- 💰 Funding readiness score
- 📝 Storytelling evaluation
- 🎨 Design feedback

Designed for:

- Startup founders
- Accelerators
- Incubators
- Investors
- Entrepreneurship competitions
""")