import argparse
import json
import streamlit as st
import openai
from datetime import datetime  # Import datetime for timestamp

# Initialize argparse
parser = argparse.ArgumentParser(description="Load chat history.")
parser.add_argument("--load_chat", type=str, help="File to load chat history from.")
args = parser.parse_args()

# Function to load chat history from a file
def load_chat_history_from_file(filename):
    with open(filename, "r") as f:
        return json.loads(f.read())

# Function to update chat history to a file
def update_chat_history_to_file(filename):
    with open(filename, "w") as f:
        f.write(json.dumps(st.session_state.messages))

# Initialize chat history and filename
if "messages" not in st.session_state or "filename" not in st.session_state:
    if args.load_chat:
        try:
            st.session_state.messages = load_chat_history_from_file(args.load_chat)
            st.session_state.filename = args.load_chat
        except FileNotFoundError:
            st.warning(f"Could not find file {args.load_chat}. Initializing with default message.")
            st.session_state.messages = [{"role": "assistant", "content": "Hello. How can I help you today."}]
            st.session_state.filename = None
    else:
        st.session_state.messages = [{"role": "assistant", "content": "Hello. How can I help you today."}]
        timestamp = datetime.now().strftime("%b%d_%I_%M_%S%p")  # Get current time
        timestamp = timestamp.replace('AM', 'am').replace('PM', 'pm') # lowercase the am/pm
        st.session_state.filename = f"./chats/convo_{timestamp}"  # Create filename with timestamp

# Read OpenAI API key from local file
with open(".OAI_KEY", "r") as f:
    openai.api_key = f.read().strip()

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize full_response
full_response = ""

# Function to update chat history to a file
def update_chat_history_to_file(filename):
    with open(filename, "w") as f:
        f.write(json.dumps(st.session_state.messages))  # Serialize messages object to string and write to file

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("How can I help today?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
        
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
    for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    
    # Update chat history to text file
    if st.session_state.filename:
        update_chat_history_to_file(st.session_state.filename)
