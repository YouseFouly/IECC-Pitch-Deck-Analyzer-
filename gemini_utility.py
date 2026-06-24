import streamlit as st 
import google.generativeai as genai

#we should configure gemini
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

#load the model 
@st.cache_resource
def load_gemini_model():
    return genai.GenerativeModel("gemini-2.5-flash-lite")

model = load_gemini_model()

#text generation
def gemini_response(prompt):
    response = model.generate_content(prompt)
    return response.text

#Upload File
def upload_file(file_path):
    uploaded_file = genai.upload_file(path=file_path)
    return uploaded_file 

#evaluate pitch deck 
def evaluate_pitch_deck(file_path):
    uploaded_file = upload_file(file_path)
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
    response = model.generate_content([prompt, uploaded_file])
    return response.text

#Generic File Analysis
def analyze_file(file_path, prompt):
    uploaded_file = upload_file(file_path)
    response = model.generate_content([prompt, uploaded_file])
    return response.text
