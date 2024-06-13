from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import time

app = Flask(__name__)

# Configure API key (replace with your actual key)
GOOGLE_API_KEY = 'AIzaSyDj1PWHQBlW6uWfBz5dYHd7BnN5GpmecqE'
genai.configure(api_key=GOOGLE_API_KEY)

@app.route('/', methods=['GET', 'POST'])
def generate_code():
  """
  Handles GET and POST requests.
  - Renders the HTML form on GET request.
  - Generates Python code based on user prompt on POST request.

  Returns:
      - The rendered HTML template (GET).
      - JSON containing the generated Python code or an error message (POST).
  """
  if request.method == 'GET':
     return render_template('index.html')
  elif request.method == 'POST':
    if not request.form or 'prompt' not in request.form:
      return jsonify({'error': 'Missing program description'}), 400

    user_prompt = request.form['prompt']
    print(user_prompt)

    try:
      
      model = genai.GenerativeModel("gemini-pro")  # Choose the appropriate model
      start_time = time.time()
      response = model.generate_content(str(user_prompt) + " Provide a detailed forecast for the startup idea, including market analysis, competitive analysis, financial projections, and potential risks. Write the content in 2000 words, with each section's heading enclosed inside <u> tags.")
      generated_code = response.text.strip()
      generated_code = generated_code.replace('*', '')
      print(generate_code)
      end_time = time.time()
      execution_time = end_time - start_time
      print("Execution time:", execution_time, "seconds")
      return render_template('output.html',title='forecast of company',content=generated_code)
    except Exception as e:
      return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
  app.run(debug=True)
