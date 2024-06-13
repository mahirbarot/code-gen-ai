import google.generativeai as genai
import PIL.Image

img = PIL.Image.open('website.png')

GOOGLE_API_KEY='AIzaSyDrllDFKLnI5q8dF361nvdzuL3h6O0JxmM'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')
model2 = genai.GenerativeModel('gemini-pro-vision')
response = model2.generate_content(["give me suggestions, feedback or changes based on my wesbite picture:", img], stream=True)
response.resolve()
print(response.text)
