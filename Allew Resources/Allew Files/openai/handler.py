import os
from openai import OpenAI

def run(model_name, prompt):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message["content"]
