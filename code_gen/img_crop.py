import streamlit as st

from streamlit_cropperjs import st_cropperjs

pic = st.file_uploader("Upload a picture", key="uploaded_pic")
if pic:
    pic = pic.read()
    cropped_pic = st_cropperjs(pic=pic, btn_text="Detect!", key="foo")
    if cropped_pic:
        st.image(cropped_pic, output_format="PNG")