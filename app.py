import streamlit as st
from llm import get_llm
from memory import save_memory, get_memory_context

st.set_page_config(page_title="Chatbot with Memory", page_icon="🧠")

st.title("🧠 Chatbot with Long-Term Memory (ChromaDB)")

llm = get_llm()

# Session state for UI chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Ask something...")

if user_input:

    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # 🔍 Retrieve memory
    memory_context = get_memory_context(user_input)

    # 🧠 Build prompt with memory
    prompt = f"""
You are a helpful AI assistant with long-term memory.

Use relevant past memory if useful:
{memory_context}

User: {user_input}
Assistant:
"""

    # 🤖 Get response
    response = llm.invoke(prompt).content

    # 💾 Save memory
    save_memory(f"User: {user_input}")
    save_memory(f"Assistant: {response}")

    # Show assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)