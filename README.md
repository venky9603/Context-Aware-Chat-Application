# Context-Aware Chat Application

An LLM-powered chatbot with long-term memory that retrieves relevant historical conversations using semantic search and generates context-aware responses using Large Language Models.

The application combines **LangChain**, **ChromaDB**, **HuggingFace Embeddings**, and **Groq Llama-3.3-70B** to build a persistent conversational AI system with memory capabilities.

---

## Project Overview

Traditional chatbots only respond based on the current conversation and lose previous interactions.

This project solves that limitation by implementing a **long-term memory pipeline** where previous user and assistant conversations are converted into embeddings, stored in a vector database, and retrieved whenever relevant context is needed.

The retrieved memory is injected into the prompt before sending it to the LLM, enabling more personalized and context-aware responses.

---

## Key Features

* **Long-Term Conversation Memory**

  * Stores previous user and assistant interactions.
  * Maintains memory across application restarts using persistent vector storage.

* **Semantic Memory Retrieval**

  * Uses HuggingFace sentence-transformer embeddings.
  * Retrieves top-k relevant historical conversations using ChromaDB similarity search.

* **Context-Aware Response Generation**

  * Combines retrieved memory with current user queries.
  * Generates responses using Groq's Llama-3.3-70B language model.

* **Interactive Chat Interface**

  * Built using Streamlit.
  * Provides a conversational UI for interacting with the AI system.

* **Secure API Management**

  * Uses environment variables to securely manage API keys.

---

## System Architecture

```
User Query
     |
     v
Streamlit Chat Interface
     |
     v
Memory Retrieval Layer
     |
     v
ChromaDB Vector Database
     |
     v
HuggingFace Embedding Model
     |
     v
Context + User Query
     |
     v
Groq Llama-3.3-70B LLM
     |
     v
Generated Response
     |
     v
Store Conversation Memory
```

---

## Technology Stack

### Programming Language

* Python

### Generative AI & LLM

* Groq API
* Llama-3.3-70B Versatile

### LLM Framework

* LangChain

### Vector Database

* ChromaDB

### Embedding Model

* HuggingFace Sentence Transformers
* sentence-transformers/all-MiniLM-L6-v2

### Application Framework

* Streamlit

### Environment Management

* Python-dotenv

---

## Project Structure

```
Context-Aware-Chat-Application/

│
├── app.py
│   └── Streamlit application and chat workflow
│
├── llm.py
│   └── Groq LLM configuration and initialization
│
├── memory.py
│   └── Memory management abstraction layer
│
├── vectorstore.py
│   └── ChromaDB setup and semantic retrieval pipeline
│
├── requirements.txt
│   └── Project dependencies
│
├── .env.example
│   └── Environment variable template
│
├── .gitignore
│   └── Ignored files and secrets
│
└── README.md
```

---

## How It Works

1. User enters a query through the Streamlit interface.

2. The application searches previous conversations stored in ChromaDB.

3. HuggingFace embeddings convert the query into vectors and perform similarity search.

4. Relevant memories are retrieved using top-k similarity matching.

5. Retrieved context is combined with the user's current query.

6. Groq Llama-3.3-70B generates a context-aware response.

7. The new conversation is stored back into the vector database for future retrieval.

---

## Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/<your-username>/<repository-name>.git

cd <repository-name>
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the project directory:

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit your `.env` file containing sensitive credentials.

---

### 5. Run Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## Future Improvements

* Add user authentication for multi-user memory management.
* Store conversation metadata such as timestamps and user sessions.
* Add RAG evaluation metrics for response quality measurement.
* Implement conversation summarization for efficient memory management.
* Deploy using cloud platforms with production monitoring.

---

## Skills Demonstrated

* Large Language Models (LLMs)
* Prompt Engineering
* Semantic Search
* Vector Databases
* Embeddings
* LangChain Application Development
* Streamlit Deployment
* API Integration
* Environment Security

---

## Author

**Maragoni Venkatesh**

Generative AI Engineer | Agentic AI Engineer


