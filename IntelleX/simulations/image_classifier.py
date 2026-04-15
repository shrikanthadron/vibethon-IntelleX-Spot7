# File: IntelleX/simulations/image_classifier.py

import streamlit as st
from PIL import Image
import numpy as np

def image_classifier_page():
    st.title("🖼️ Image Classification Demo")

    st.write("Upload an image and classify based on brightness demo logic.")

    file = st.file_uploader(
        "Upload Image",
        type=["png", "jpg", "jpeg"]
    )

    if file:
        img = Image.open(file)
        st.image(img, caption="Uploaded Image", use_container_width=True)

        arr = np.array(img)

        brightness = arr.mean()

        if brightness > 140:
            label = "Bright Object / Day Scene"
        elif brightness > 80:
            label = "Normal Scene"
        else:
            label = "Dark Object / Night Scene"

        st.success(f"Predicted Class: {label}")
        st.info(f"Average Brightness Score: {brightness:.2f}")

    st.caption("Demo Classifier: Image pixel statistics")