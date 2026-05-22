import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile"
)

@tool
def get_menu() -> str:
    """Returns the cafe menu with items and prices."""
    return """
    - Americano: $45
    - Cappuccino: $55
    - Latte: $55
    - Oat milk latte: $65
    - Croissant: $35
    - Avocado toast: $75
    """

tools = [get_menu]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are a friendly assistant for Café Tres Leches in Chihuahua. Only use tools when necessary."
)

history = []

while True:
    user_input = input("You: ")
    history.append(HumanMessage(content=user_input))
    
    response = agent.invoke({"messages": history})
    
    final_message = response["messages"][-1].content
    print(f"Agent: {final_message}\n")
    
    history = response["messages"]