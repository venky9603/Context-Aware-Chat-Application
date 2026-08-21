import streamlit as st
from langchain_groq import ChatGroq

def get_llm():
    # Read the Groq API key securely from Streamlit Secrets
    groq_api_key = st.secrets["GROQ_API_KEY"]

    # Initialize the Groq LLM
    return ChatGroq(
        groq_api_key=groq_api_key,
        model_name="llama-3.3-70b-versatile",
        temperature=0.7
    )
