import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool # used for tools
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent # used to create react agent

load_dotenv() # loads environment variables from .env

# builds groq-based llm
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile"
)

# retrieves menu
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

tools = [get_menu] # list of available tools

# creates react agent using llm, tools, and specs
agent = create_react_agent(
    model=llm,
    tools=tools,
    prompt="""You are a friendly assistant for Café Tres Leches in Chihuahua.
    You have access to a get_menu tool.
    ONLY use the get_menu tool when the customer EXPLICITLY asks for the menu, food items, drinks, or prices.
    NEVER use the get_menu tool for greetings or general conversation.
    When you retrieve the menu, always display the complete list of items and prices.
    Respond in Spanish always."""
)

history = [] # conversation history

# runs main interface
while True:
    user_input = input("You: ")
    history.append(HumanMessage(content=user_input)) # appends human message to the conversation history
    
    response = agent.invoke({"messages": history}) # passes history to agent

    final_message = response["messages"][-1].content # retrieves last appended message
    print(f"Agent: {final_message}\n")
    
    history = response["messages"] # conversation history is updated