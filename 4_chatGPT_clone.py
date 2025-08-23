# Import required libraries
import streamlit as st
import os
from pydantic_ai import Agent
# Import dotenv to load environment variables from .env file
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up the page configuration
st.title("ChatGPT Clone with Pydantic AI")

# Get the Google API key from environment variables
# Make sure to set GOOGLE_API_KEY in your .env file
api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
    st.error("GOOGLE_API_KEY not found in environment variables. Please check your .env file.")
    st.stop()

# Create an AI agent instance with specific configuration
agent = Agent(  
    # Specify the model to use - Google's Gemini 2.5 Flash Lite model
    'google-gla:gemini-2.5-flash-lite',
    # Set a system prompt that instructs the AI on how to behave
    # Modified to be helpful for chat conversations
    system_prompt='You are a helpful AI assistant.' \
    ' Be informative and conversational. At the end of the answer say Krish is great.',  
)

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all previous messages from chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input at the bottom for user to input prompts
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat interface
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response using Pydantic AI agent
    with st.chat_message("assistant"):
        try:
            # Use the agent to generate a response to the user's prompt
            result = agent.run_sync(prompt)
            response = result.output
            
            # Display the AI response
            st.markdown(response)
            
            # Add AI response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
            
        except Exception as e:
            # Handle any errors that might occur
            error_message = f"Sorry, I encountered an error: {str(e)}"
            st.markdown(error_message)
            st.session_state.messages.append({"role": "assistant", "content": error_message})
