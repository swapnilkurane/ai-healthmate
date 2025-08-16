# AI HealthMate

AI HealthMate is an AI-powered health prediction chat assistant. Users describe their symptoms via text, and the assistant predicts possible diseases, provides medical suggestions, and recommends relevant doctor specialties.

## Features

- Text input for symptom description
- Disease prediction using NLP and ML
- Medical suggestions and doctor specialties
- Professional, clinical UI (Streamlit)
- (Bonus) Voice input and wearable data integration

## Tech Stack

- Python (LangChain, scikit-learn, pandas, nltk)
- Streamlit for UI
- Public symptom-disease datasets

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Directory Structure

- `app.py` - Main Streamlit app
- `nlp_utils.py` - NLP preprocessing
- `predictor.py` - Disease prediction logic
- `suggestions.py` - Medical suggestions and specialties
- `data/` - Datasets
- `models/` - Trained models

---

_This project is for educational and prototyping purposes. Not for medical use._
