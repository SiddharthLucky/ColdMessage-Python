import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

with open('msg-instructions.md', 'r') as file:
    instructions = file.read()

model = genai.GenerativeModel('gemini-2.0-flash-exp')
response = model.generate_content(f"{instructions}\ncan you give me a cold email to jane for a job reference")
print(response.text)
