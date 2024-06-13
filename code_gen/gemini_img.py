import streamlit as st
from PIL import Image
import google.generativeai as genai
import io

GOOGLE_API_KEY='AIzaSyDrllDFKLnI5q8dF361nvdzuL3h6O0JxmM'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro-vision')


def main():
    st.title("Image Input and Conversion Example")
    
    # Allow the user to upload an image file
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Display the uploaded image
        #st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        pil_image = Image.open(uploaded_file)
        
        # Convert PIL Image to byte stream
        img_byte_array = io.BytesIO()
        pil_image.save(img_byte_array, format='PNG')
        response = model.generate_content(["give me suggestions, feedback or changes based on my wesbite picture:", uploaded_file])
        response.resolve()
        print(response.text)

        
        # Convert the uploaded image to a PIL Image object
#        pil_image = Image.open(uploaded_file)
        
        # Perform any PIL operations on the image (if required)
        # For example, you can resize the image
        #resized_image = pil_image.resize((200, 200))
        
        # Display the converted image
        #st.image(resized_image, caption='Converted Image (Resized)', use_column_width=True)

if __name__ == "__main__":
    main()
