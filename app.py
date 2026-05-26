import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent

load_dotenv()

app = Flask(__name__)

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

agent = create_react_agent(
    model=llm,
    tools=tools,
    prompt="You are a friendly assistant for Café Tres Leches in Chihuahua. You have access to a get_menu tool. ONLY use the get_menu tool when the customer EXPLICITLY asks for the menu, food items, drinks, or prices. NEVER use the get_menu tool for greetings or general conversation. When you retrieve the menu, always display the complete list of items and prices. Respond in Spanish always."
)

conversation_histories = {}

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get("Body", "")
    sender = request.values.get("From", "")

    if sender not in conversation_histories:
        conversation_histories[sender] = []

    conversation_histories[sender].append(
        HumanMessage(content=incoming_msg)
    )

    response = agent.invoke({
        "messages": conversation_histories[sender]
    })

    conversation_histories[sender] = response["messages"]

    reply = response["messages"][-1].content

    twilio_response = MessagingResponse()
    twilio_response.message(reply)
    return str(twilio_response)

if __name__ == "__main__":
    app.run(debug=True, port=5000)