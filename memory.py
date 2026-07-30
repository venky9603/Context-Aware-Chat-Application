from vectorstore import add_memory, retrieve_memory

def save_memory(text: str):
    add_memory(text)

def get_memory_context(query: str):
    return retrieve_memory(query)