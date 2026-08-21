import streamlit as st
from langchain_groq import ChatGroq

def get_llm():
    # Check if the key exists in Streamlit secrets
    if "GROQ_API_KEY" not in st.secrets:
        raise ValueError("Missing GROQ_API_KEY in Streamlit secrets. Please add it in App settings → Secrets.")

    groq_api_key = st.secrets["GROQ_API_KEY"]

    # Initialize Groq LLM
    return ChatGroq(
        groq_api_key=groq_api_key,
        model_name="openai/gpt-oss-20b",
        temperature=0.7
    )
