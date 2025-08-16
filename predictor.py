import joblib
import os
import numpy as np

# Load model, label encoder, and feature names
MODEL_PATH = os.path.join("models", "disease_model.joblib")
ENCODER_PATH = os.path.join("models", "label_encoder.joblib")
FEATURES_PATH = os.path.join("models", "feature_names.joblib")

clf = joblib.load(MODEL_PATH)
le = joblib.load(ENCODER_PATH)
feature_names = joblib.load(FEATURES_PATH)

def symptoms_to_vector(symptom_text):
    # Accepts comma-separated symptoms, returns a feature vector
    symptoms = [s.strip().lower() for s in symptom_text.split(",")]
    x = np.zeros(len(feature_names))
    for i, feat in enumerate(feature_names):
        if feat.lower() in symptoms:
            x[i] = 1
    return x.reshape(1, -1)

def predict_disease(symptom_text):
    X = symptoms_to_vector(symptom_text)
    pred = clf.predict(X)
    disease = le.inverse_transform(pred)[0]
    return disease