import os
import google.generativeai as genai

def run(model_name, prompt):
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    model = genai.GenerativeModel(model_name)
    response = model.generate_content(prompt)

    return response.text
