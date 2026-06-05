import os
from flask import Flask, request # used for Flask web server
from twilio.twiml.messaging_response import MessagingResponse # used for Twilio's response format
from dotenv import load_dotenv # used to load environment variables
from langchain_groq import ChatGroq
from langchain_core.tools import tool # used for tools
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent # used to create react agent
from tools import all_tools

load_dotenv() # loads environment variables from .env

app = Flask(__name__) # creates Flask web application

# builds groq-based llm
llm = ChatGroq(
    api_key = os.getenv("GROQ_API_KEY"),
    model = "llama-3.3-70b-versatile"
)

tools = all_tools # list of available tools

# creates react agent using llm, tools, and specs
agent = create_react_agent(
    model = llm,
    tools = tools,
    prompt = """
    You are a friendly assistant for Café Tres Leches in El Paso. You have access to many tools that can help you retrieve information
    about the cafe or make and cancel reservations. You must display the strings that are returned from these tools when you think
    appropriate.
    """
)

conversation_histories = {} # stores conversation history per user

# run after post request
@app.route("/webhook", methods=["POST"])
def webhook():
    # extracts sender's message and phone number
    incoming_msg = request.values.get("Body", "")
    sender = request.values.get("From", "")

    if sender not in conversation_histories:
        conversation_histories[sender] = []

    conversation_histories[sender].append(
        HumanMessage(content=incoming_msg)
    )

    # pass history to agent
    response = agent.invoke({
        "messages": conversation_histories[sender]
    })

    conversation_histories[sender] = response["messages"] # update conversation history

    reply = response["messages"][-1].content # retrieves last appended message

    # wraps Twilio's response and returns it
    twilio_response = MessagingResponse()
    twilio_response.message(reply)
    return str(twilio_response)

# starts Flask server
if __name__ == "__main__":
    app.run(debug=True, port=5000)