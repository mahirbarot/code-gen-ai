import google.generativeai as genai

# Configure API key (replace with your actual key)
genai.configure(api_key="AIzaSyDj1PWHQBlW6uWfBz5dYHd7BnN5GpmecqE")

def generate_python_code(prompt):
  """
  Generates Python code based on a user prompt with argument context.

  Args:
      prompt: A string describing the desired Python code functionality,
              including information about arguments.

  Returns:
      A string containing the generated Python code.
  """
  model = genai.GenerativeModel("gemini-pro")  # Choose the appropriate model
  response = model.generate_content(prompt)
  return response.text.strip()

# Example usage with argument context in prompt
user_prompt = "Write a Python function named 'add' that takes two numbers as arguments and returns their sum."
generated_code = generate_python_code(user_prompt)
print("Generated Python code:")
print(generated_code)

