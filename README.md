# Cafe WhatsApp AI Agent
An AI-powered WhatsApp agent that handles customer inquiries for a small cafe business, built with Groq, LangChain, and Twilio.

## About
I wanted to learn more about building AI agents, so I taught myself the core concepts from scratch. As a practical application, I built a WhatsApp agent for a small business, a space where I saw a real opportunity. Many small businesses lack the resources to handle customer inquiries efficiently, and an AI agent trained on business-specific information can fill that gap effectively.

## Features
- Responds to customer inquiries via WhatsApp in real time
- Provides full menu with categories and prices
- Shares cafe hours, location, and contact information
- Displays weekly specials and happy hour deals
- Takes and confirms table reservations
- Cancels existing reservations
- Informs customers about reservation policies
- Persists reservation data across sessions using a local JSON database
- Maintains conversation history per user (remembers context within a conversation)
- Responds in the customer's language automatically
- Built with a modular structure (tools, reservations, and server logic are separated into independent files)

## Tech Stack
- Python
- LangChain & LangGraph
- Groq (LLaMA 3.3 70B)
- Flask
- Twilio
- WhatsApp Business API
- ngrok / VS Code Port Forwarding

## How to Run
- Clone the repository
- Create a virtual environment and activate it
- Install dependencies — pip install -r requirements.txt
- Set up environment variables — create a .env file with these keys:
    - GROQ_API_KEY
    - TWILIO_ACCOUNT_SID
    - TWILIO_AUTH_TOKEN
    - TWILIO_WHATSAPP_NUMBER
- Run the Flask server (python app.py)
- Expose the server (using VS Code port forwarding or ngrok)
- Configure Twilio (add the public URL + /webhook to the Twilio sandbox settings)
- Join the Twilio sandbox (send the join message from WhatsApp to the sandbox number)

## Project Structure
- app.py: Flask server and webhook logic (main)
- requirements.txt: project dependencies
- reservations.py: reservations database logic
- tools.py: tools logic for agent to use
- reservations.json: booked reservations database

## Future Improvements
- Perform more thorough testing
- Deploy to a cloud server so it runs 24/7 without a laptop
- Connect to a real database instead of a JSON file
- Add payment integration
- Make it a reusable template for any small business
- Switch from Groq to Anthropic's API for production reliability
- Build a simple onboarding flow where a business owner can customize the agent without touching code
