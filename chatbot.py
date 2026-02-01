from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

# load the env variables
load_dotenv()

# streamlit page setup
st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
    layout="centered",
)
st.title("🤖 Generative AI Chatbot")

llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.0
    )

# initialize the chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask chatbot...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    response = llm.invoke(
        input = [{"role": "system", "content": "You are a helpful assistant."}, *st.session_state.chat_history]
    )

    assistant_response = response.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)
