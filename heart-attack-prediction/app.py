import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import openpyxl


row1 = st.columns([1, 2, 3])
age = row1[0].slider('Age', 20, 100, 50)
gender = row1[0].slider('Gender (1 = Male, 0 = Female)',0, 1, 0)
cp = row1[0].slider('Chest Pain Type', 0, 3, 1)
trestbps = row1[0].slider('Resting blood pressure (in mm Hg)', 0, 200, 94)
chol = row1[0].slider('Serum cholesterol (in mg/dl)', 100, 600, 240)

fbs = row1[1].slider('Fasting blood sugar\n' '\n(1 = fasting blood sugar > 120 mg/dl,\n' '\n0 = otherwise)', 0, 1, 0)
restecg = row1[1].slider('Resting electrocardiographic results', 0, 2, 1)
thalach = row1[1].slider('Maximum heart rate achieved', 0, 250, 71)
exang = row1[1].slider('Exercise-induced angina (1 = yes, 0 = no)', 0, 1, 0)

oldpeak = row1[2].slider('ST depression induced by exercise relative to rest', 0, 7, 3)
slope = row1[2].slider('Slope of the peak exercise ST segment\n' '\n(0 = upsloping, 1 = flat, 2 = downsloping)', 0, 2, 1)
ca = row1[2].slider('Number of major vessels (0-3) colored by fluoroscopy', 0, 3, 1)
thal = row1[2].slider('Thalassemia (3 = normal, 6 = fixed defect, 7= reversible defect)', 0, 7, 3)

model = pickle.load(open('model.pkl', 'rb'))

input_data = (age, gender, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)

def fetch(inputs):
    input_data_array = np.asarray(inputs)
    reshaped_data = input_data_array.reshape(1,-1)
    prediction = model.predict(reshaped_data)
    if prediction[0] == 0:
        st.write("Patient might not have Heart-Attack Risk.")
    else:
        st.write("Patient might have Heart-Attack Risk.")

st.button("Submit", on_click= fetch(input_data))