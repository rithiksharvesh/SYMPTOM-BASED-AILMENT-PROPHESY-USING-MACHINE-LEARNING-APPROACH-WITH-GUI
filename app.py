# app.py

import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
model = pickle.load(open('rf_disease_model.pkl', 'rb'))

# Load symptom list
df = pd.read_csv('Training.csv')
symptoms = df.columns[:-1].tolist()

# Streamlit UI
st.title("🩺 Symptom-Based Disease Prediction")
st.write("Select symptoms from the list below:")

selected_symptoms = st.multiselect("Choose Symptoms", symptoms)

input_data = np.zeros(len(symptoms))
for symptom in selected_symptoms:
    input_data[symptoms.index(symptom)] = 1

if st.button("Predict Disease"):
    prediction = model.predict([input_data])[0]
    st.success(f"Predicted Disease: {prediction}")
