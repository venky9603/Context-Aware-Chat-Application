from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Local embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Persistent Chroma database
vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

def add_memory(text):
    vectorstore.add_texts([text])

def retrieve_memory(query, k=3):
    results = vectorstore.similarity_search(query, k=k)
    return "\n".join([doc.page_content for doc in results])