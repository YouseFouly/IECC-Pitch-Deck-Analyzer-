import os
import json
import streamlit as st
import google.generativeai as genai

# ==========================
# Configure Gemini
# ==========================

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# ==========================
# Load Model
# ==========================

def load_gemini_model():
    """
    Returns the Gemini model.
    """
    return genai.GenerativeModel("gemini-2.5-flash-lite")


# ==========================
# Text Generation
# ==========================

def gemini_response(prompt):
    """
    Generates a response from Gemini using text only.
    """
    model = load_gemini_model()

    response = model.generate_content(prompt)

    return response.text


# ==========================
# Upload File
# ==========================

def upload_file(file_path):
    """
    Uploads any supported file (PPTX, PDF, DOCX, Image...)
    to Gemini Files API.
    """

    uploaded_file = genai.upload_file(path=file_path)

    return uploaded_file


# ==========================
# Evaluate Pitch Deck
# ==========================

def evaluate_pitch_deck(file_path):
    """
    Uploads a PowerPoint pitch deck and returns a detailed
    investor-style evaluation.
    """

    uploaded_file = upload_file(file_path)

    model = load_gemini_model()

    prompt = """
You are a senior Venture Capital investor.

Analyze this startup pitch deck thoroughly.

Evaluate each of the following sections:

1. Cover Slide
2. Problem
3. Solution
4. Product
5. Market Size (TAM / SAM / SOM)
6. Business Model
7. Competition
8. Competitive Advantage (Moat)
9. Traction
10. Go-To-Market Strategy
11. Financial Projections
12. Team
13. Investment Ask
14. Roadmap

For EACH section provide:

• Is this section present?
• Score (/10)
• Strengths
• Weaknesses
• Missing information
• Suggestions for improvement

Then evaluate:

- Storytelling
- Visual Design
- Slide Order
- Investor Readiness
- Clarity
- Market Opportunity
- Scalability
- Risks

Finally provide:

1. Overall Score (/100)

2. Funding Readiness
Choose one:
- Ready to Raise
- Nearly Ready
- Needs Significant Work

3. Top 10 Most Important Improvements

4. Missing Slides

5. Missing Metrics

6. Final Summary
"""

    response = model.generate_content([
        uploaded_file,
        prompt
    ])

    return response.text


# ==========================
# Generic File Analysis
# ==========================

def analyze_file(file_path, prompt):
    """
    Uploads any supported file and analyzes it
    using a custom prompt.
    """

    uploaded_file = upload_file(file_path)

    model = load_gemini_model()

    response = model.generate_content([
        uploaded_file,
        prompt
    ])

    return response.text
