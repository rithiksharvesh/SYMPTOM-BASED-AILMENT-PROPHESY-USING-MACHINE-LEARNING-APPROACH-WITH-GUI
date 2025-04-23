# model_building.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Load data
df = pd.read_csv('Training.csv')
X = df.drop(['prognosis'], axis=1)
y = df['prognosis']

# Train/test split
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_val)
print("Accuracy:", accuracy_score(y_val, y_pred))
print(classification_report(y_val, y_pred))

# Save model
with open('rf_disease_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved to rf_disease_model.pkl")
