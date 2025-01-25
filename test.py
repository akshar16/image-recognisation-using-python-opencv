#this code is used to get the names of availabe models to use 


import google.generativeai as genai

from main import API_KEY

# Configure your API key (replace with your actual API key)
API_KEY = 'AIzaSyBrkleDujkZTPEtWmZIxWIGljE1UKSRcF4'

# List available models
models = genai.list_models()

# Print models and supported methods
for model in models:
    print(f"Model Name: {model.name}")
    print(f"Supported Methods: {model.supported_generation_methods}")
    print("-" * 20)

# Example (use a valid model name returned by list_models)
try:
    vision_model = genai.GenerativeModel(model_name="gemini-1.5-pro-vision") # Or a valid model
    response = vision_model.generate_content("Tell me about the weather today.")
    print(response.text)

except Exception as e:
    print(f"Error using model: {e}")
