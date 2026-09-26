import streamlit as st
import joblib

model = joblib.load('Ai_camp.pkl')

st.title("🍔 What Category Is It?")

calories = st.slider("Calories", 0, 1000, 300)

if st.button("Predict"):
    result = model.predict([[calories]])
    st.write("The AI thinks this is:", result[0])
from google.colab import files
files.download('app.py')
