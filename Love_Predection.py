import streamlit as st
import pandas as pd
import numpy as np
import pickle


#load model 
model = pickle.load(open(r"C:\AI&DS\best_love_model.pkl","rb"))

st.title("💖 AI Girlfriend/Boyfriend Predictor")
st.markdown("###Will You Be Their Perfect Match?")

#user Input
looks = st.slider("Looks(1-10)",1, 10, 5)
humor = st.slider("Sense Of Humor(1-10)",1, 10, 5)
kindness = st.slider("Kindness(1-10)",1, 10, 5) 
confidence = st.slider("Confidence(1-10)",1, 10, 5) 
intelligence = st.slider("Intelligence(1-10)",1, 10, 5)
user_input = np.array([[looks,humor,kindness,confidence,intelligence]])
if st.button ("💌Predict love Compatibility "):
    prediction = model.predict(user_input)
    if prediction[0] == 1:
        st.success("🪄It's a Match! Your love story begins....")

    else:
        st.error("❤Oops! Better luck next time")

st.markdown("(This app uses Machine Learning ,not Astrology😊)")