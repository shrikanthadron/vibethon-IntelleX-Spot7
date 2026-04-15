# File: IntelleX/simulations/spam_detection.py

import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def spam_detection_page():
    st.title("📩 Spam Detection Simulator")

    data = {
        "text": [
            "Win money now",
            "Claim your free prize",
            "Urgent offer click now",
            "Meeting at 5 pm",
            "Project submission tomorrow",
            "Let's have lunch",
            "Free recharge available",
            "Call me when free"
        ],
        "label": [1,1,1,0,0,0,1,0]
    }

    df = pd.DataFrame(data)

    X = df["text"]
    y = df["label"]

    vectorizer = CountVectorizer()
    X_vec = vectorizer.fit_transform(X)

    model = MultinomialNB()
    model.fit(X_vec, y)

    st.write("Enter a message to classify whether it is spam or not.")

    msg = st.text_area("Message", "Congratulations! You won free money")

    if st.button("Predict Spam"):
        msg_vec = vectorizer.transform([msg])
        pred = model.predict(msg_vec)[0]
        prob = model.predict_proba(msg_vec)[0]

        if pred == 1:
            st.error(f"Prediction: Spam ({prob[1]*100:.1f}%)")
        else:
            st.success(f"Prediction: Not Spam ({prob[0]*100:.1f}%)")

    st.caption("Model: Naive Bayes + Bag of Words")