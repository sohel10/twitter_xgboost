#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from PIL import Image

# Load the saved model
try:
    with open("xgboost_model.pkl", "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Model file not found. Please make sure 'xgboost_model.pkl' is in the same directory.")
    st.stop()

# Load the saved TfidfVectorizer
try:
    with open("tfidf_vectorizer1.pkl", "rb") as file:
        vectorizer1 = pickle.load(file)
except FileNotFoundError:
    st.error("Vectorizer file not found. Please make sure 'tfidf_vectorizer1.pkl' is in the same directory.")
    st.stop()

# Streamlit app code
st.title("Twitter Speech Analysis App")
st.markdown("<span style='font-size: 20px;'><strong>By Sohel Ahmed</strong></span>", unsafe_allow_html=True)
image = Image.open("t.png")
st.image(image, use_column_width=True)

st.subheader("Enter your text here:")
user_input = st.text_area("")

# Create a predict button
if st.button("Predict"):
    # Preprocess the input text
    text_vectorized = vectorizer1.transform([user_input])
    # Make predictions
    prediction = model.predict(text_vectorized)[0]
    st.header("Prediction:")
    # Display the predicted sentiment
    if prediction == 'Harm':
        st.subheader("The sentiment of the given text is: Harm")
    elif prediction == 'Not Harm':
        st.subheader("The sentiment of the given text is: Not Harm")
