import streamlit as st
import nltk
print("NLTK version:", nltk.__version__)
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')  # Download the punkt tokenizer
print(word_tokenize("This is a test."))  # Test the tokenizer

from predictor import predict_disease
from suggestions import get_suggestions

st.set_page_config(page_title="AI HealthMate", layout="centered", page_icon="🩺")

# Sidebar
with st.sidebar:
    st.title("🩺 AI HealthMate")
    st.markdown("""
    **Your AI-powered health assistant**
    
    1. Enter your symptoms in the main area.
    2. Click **Analyze** to get predictions and suggestions.
    3. For urgent symptoms, always consult a real doctor.
    """)
    st.info("All data is processed locally. No information is sent to the cloud.")

st.markdown("<h1 style='text-align: center; color: #1976d2;'>AI HealthMate</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Describe your symptoms and get instant health insights.</p>", unsafe_allow_html=True)
st.write("")

col1, col2, col3 = st.columns([1,2,1])
with col2:
    symptoms = st.text_area("📝 Enter your symptoms (e.g., 'cough, fatigue, sore throat')", height=100)
    analyze = st.button("🔍 Analyze", use_container_width=True)

if 'analyze' not in locals():
    analyze = False

if analyze:
    if symptoms:
        prediction = predict_disease(symptoms)
        suggestions, specialties = get_suggestions(prediction)
        st.markdown("---")
        st.subheader("🦠 Possible Diseases")
        st.success(prediction)
        st.subheader("💡 Medical Suggestions")
        st.info(suggestions)
        st.subheader("👨‍⚕️ Relevant Doctor Specialties")
        st.warning(specialties)
    else:
        st.warning("Please enter your symptoms.")

# Footer disclaimer
st.markdown("""
---
<p style='text-align: center; color: gray; font-size: 0.9em;'>
    <b>Disclaimer:</b> AI HealthMate is for informational purposes only and does not provide medical advice. Always consult a healthcare professional for serious or urgent symptoms.
</p>
""", unsafe_allow_html=True)