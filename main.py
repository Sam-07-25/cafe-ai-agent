import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langchain_core.tools import tool

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile"
)

@tool
def get_menu() -> str:
    """Returns the cafe menu."""
    return """
    - Americano: $45
    - Cappuccino: $55
    - Latte: $55
    - Oat milk latte: $65
    - Croissant: $35
    - Avocado toast: $75
    """

tools = [get_menu]
llm_with_tools = llm.bind_tools(tools)

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a friendly assistant for Café Tres Leches in Chihuahua. 
    Only use the get_menu tool when the customer specifically asks about the menu, food, drinks, or prices.
    For greetings or general questions, just respond normally without using any tools."""),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}")
])

history = []

while True:
    user_input = input("You: ")
    
    # Step 1: get response from AI
    response = llm_with_tools.invoke(
        prompt.invoke({
            "history": history,
            "question": user_input
        }).to_messages()
    )
    
    # Step 2: check if AI wants to use a tool
    if response.tool_calls:
        history.append(HumanMessage(content=user_input))
        history.append(response)
        
        # Step 3: execute the tool and pass result back
        for tool_call in response.tool_calls:
            if tool_call["name"] == "get_menu":
                tool_result = get_menu.invoke({})
                print(f"DEBUG tool result: {tool_result}")
                history.append(ToolMessage(
                    content=tool_result,
                    tool_call_id=tool_call["id"]
                ))
        
        # Step 4: get final response with tool result
        print(f"DEBUG history: {history}")
        final_response = llm_with_tools.invoke(history)
        print(f"Agent: {final_response.content}\n")
        history.append(AIMessage(content=final_response.content))
    
    else:
        content = response.content
        if content:
            print(f"Agent: {content}\n")
            history.append(HumanMessage(content=user_input))
            history.append(AIMessage(content=content))
        else:
            print(f"Agent: Lo siento, no entendí tu pregunta.\n")