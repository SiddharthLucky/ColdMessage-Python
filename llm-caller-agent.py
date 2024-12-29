import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-2.0-flash-exp')
response = model.generate_content("can you give me a cold email to jane for a job reference")
print(response.text)