# Import the Agent class from pydantic_ai library
# Pydantic AI is a framework for building AI agents with type safety
from pydantic_ai import Agent
# Import os to access environment variables for API key
import os
# Import dotenv to load environment variables from .env file
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Google API key from environment variables
# Make sure to set GOOGLE_API_KEY in your .env file
api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables. Please check your .env file.")

# Create an AI agent instance with specific configuration
agent = Agent(  
    # Specify the model to use - Google's Gemini 2.5 Flash Lite model
    'google-gla:gemini-2.5-flash-lite',
    # Set a system prompt that instructs the AI on how to behave
    # This tells the AI to be concise and reply with only one sentence
    system_prompt='Be concise, reply with one sentence.',  
)

# Run the agent synchronously with a specific question
# This sends the question to the AI model and waits for a response
result = agent.run_sync('am i a bot')  

# Print the AI's response/output
print(result.output)
