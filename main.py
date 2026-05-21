import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile"
)

messages = [
    SystemMessage(content="You are a friendly assistant for a small cafe in Mexico."),
    HumanMessage(content="What are 3 common problems cafe owners face?")
]

response = llm.invoke(messages)
print(response.content)