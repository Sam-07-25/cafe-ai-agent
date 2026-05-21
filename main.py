import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly assistant for a cafe called {cafe_name} in {city}."),
    ("human", "{question}")
])

chain = prompt | llm

response = chain.invoke({
    "cafe_name": "Café Tres Leches",
    "city": "Chihuahua",
    "question": "What are your opening hours?"
})

print(response.content)