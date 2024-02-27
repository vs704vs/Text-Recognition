import pytesseract as tess

tess.pytesseract.tesseract_cmd = r"tesseract\tesseract.exe"
from PIL import Image
import streamlit as st

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    img = Image.open(uploaded_image)
    text = tess.image_to_string(img)

    st.write("Data:")
    st.write(text)
