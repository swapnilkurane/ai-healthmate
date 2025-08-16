import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Load data
df = pd.read_csv("data/Disease_and_symptoms_dataset.csv")
df = df.sample(20000, random_state=42)  # Use a random sample for faster training

# Features and label
X = df.drop('diseases', axis=1)
y = df['diseases']

# Encode labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Train model
clf = LogisticRegression(max_iter=300, solver='saga', n_jobs=-1, verbose=1)
clf.fit(X_train, y_train)

# Save model, label encoder, and feature names
os.makedirs("models", exist_ok=True)
joblib.dump(clf, "models/disease_model.joblib")
joblib.dump(le, "models/label_encoder.joblib")
joblib.dump(list(X.columns), "models/feature_names.joblib")

print("Model, label encoder, and feature names saved in models/")
print("Test accuracy:", clf.score(X_test, y_test))