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
    You are a friendly and welcoming assistant for Café Tres Leches, located in El Paso, TX.
    You have access to the following tools and should use them accordingly:

    - get_menu: Use ONLY when the customer explicitly asks about the menu, food, drinks, or prices. Always display the complete list when retrieved.
    - get_hours: Use when the customer asks about opening hours, closing times, or when the cafe is open.
    - get_location: Use when the customer asks about the address, location, directions, or parking.
    - get_contact: Use when the customer asks for a phone number, email, website, or social media.
    - get_specials: Use when the customer asks about specials, deals, happy hour, or featured items.
    - get_reservation_policy: Use when the customer asks about reservation rules, cancellation policy, or party size limits.
    - make_reservation: Use when the customer wants to book a table. Collect name, date, time, and party size before calling the tool.
    - cancel_reservation: Use when the customer wants to cancel an existing reservation. Collect name and date before calling the tool.

    GENERAL RULES:
    - NEVER use a tool for greetings or general conversation.
    - Always respond in the same language the customer uses.
    - Be warm, friendly, and concise.
    - If a customer asks something you don't have information about, politely let them know and suggest they call or DM us on Instagram.
    - Never make up information that isn't provided by your tools.
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