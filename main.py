import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly assistant for a cafe called Café Tres Leches in Chihuahua."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}")
])

parser = StrOutputParser()
chain = prompt | llm | parser

history = []

while True:
    user_input = input("You: ")
    
    response = chain.invoke({
        "history": history,
        "question": user_input
    })
    
    print(f"\nAgent: {response}\n")
    
    history.append(HumanMessage(content=user_input))
    history.append(AIMessage(content=response))