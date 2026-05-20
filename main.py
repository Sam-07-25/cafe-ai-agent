import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv() # loads API key from .env file

client = Groq(api_key=os.getenv("GROQ_API_KEY")) # connection to Groq's servers

user_input = input("Ask something: ")

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile", # which model to use
    messages=[
        {"role": "user", "content": user_input},
    ] # conversation (one user message)
) # POST request to Groq's servers

print(response.choices[0].message.content) # response is a JSON onject full with metadata, so we access the text only