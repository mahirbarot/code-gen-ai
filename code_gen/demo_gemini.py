import streamlit as st
import google.generativeai as genai
import PIL.Image

# Replace with your actual API key
GOOGLE_API_KEY='AIzaSyDrllDFKLnI5q8dF361nvdzuL3h6O0JxmM'

default_prompt='give me suggestions, feedback or changes based on my wesbite picture:'
def generate_feedback(image, text_prompt=default_prompt):
    """Generates website feedback using the Gemini API.

    Args:
        image (bytes): The image data of the website.
        text_prompt (str): The text prompt to provide context to the API.

    Returns:
        str: The generated feedback from the Gemini API.
    """

    # Authenticate with the Gemini API
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    model2 = genai.GenerativeModel('gemini-pro-vision')

    response = model2.generate_content([text_prompt, image], stream=True)
    response.resolve()
    #print(response)
    print(response.text)


    feedback = ""
    for chunk in response.yield_text():
        feedback += chunk
    return feedback

st.title("Website Feedback Generator with Gemini API")

uploaded_file = st.file_uploader("Upload your website image:", type=["jpg", "jpeg", "png"])
text_prompt = st.text_input("Enter additional context (optional):")

if uploaded_file is not None:
    image_data = uploaded_file.read()
    image_data = PIL.Image.open(image_data)
    

    if text_prompt:
        prompt = f"{text_prompt} Here's an image of my website:"
    else:
        prompt = "Give me suggestions, feedback or changes based on my website picture:"

    st.write("Generating feedback...")

    feedback = generate_feedback(image_data, prompt)
    st.success(f"Website Feedback: {feedback}")

else:
    st.info("Please upload an image of your website.")
