# Import the Agent class from pydantic_ai library
# Pydantic AI is a framework for building AI agents with type safety
from pydantic_ai import Agent
# Import os to access environment variables for API key
import os

# Set up the Google API key for Gemini model
# You can set this as an environment variable: GOOGLE_API_KEY
# Or replace "your-google-api-key-here" with your actual API key
os.environ['GOOGLE_API_KEY'] = "AIzaSyAT-xzR1hSHM4IG5HUlVRk8wgRYXJFUCR8"

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
