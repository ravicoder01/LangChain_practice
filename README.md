# 🦜 LangChain Practice — GenAI + RAG Pipeline

> A hands-on end-to-end GenAI project built with **LangChain**, **Groq (LLaMA 3.3)**, **FAISS VectorStore**, and **Streamlit** — featuring a fully deployed Question Answering bot with LangSmith monitoring.

---

## 🚀 Live Demo

[![Streamlit App](https://img.shields.io/badge/Live%20App-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://langchainpractice-dcw5vu6wqkguztfc8om7am.streamlit.app/)
[![LangSmith](https://img.shields.io/badge/Monitored%20by-LangSmith-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://smith.langchain.com)

---

## 📌 Project Overview

This project demonstrates a complete **Retrieval-Augmented Generation (RAG)** pipeline using LangChain, where a PDF document is ingested, embedded, stored in a vector database, and queried using a powerful LLM — all wrapped in a clean Streamlit UI.

The bot acts as an **AI Engineer assistant**, answering questions strictly based on the provided PDF context.

---

## 🏗️ Architecture

```
PDF Document
     │
     ▼
[Data Loading] ──► PyPDFLoader / TextLoader
     │
     ▼
[Text Splitting] ──► CharacterTextSplitter / RecursiveCharacterTextSplitter
     │
     ▼
[Embedding] ──► HuggingFace Embeddings (sentence-transformers)
     │
     ▼
[VectorStore] ──► FAISS Index (faiss_idx/)
     │
     ▼
[Retriever] ──► Similarity Search
     │
     ▼
[LLM] ──► Groq API → LLaMA 3.3 (70B)
     │
     ▼
[Response] ──► Streamlit UI (app.py)
     │
     ▼
[Monitoring] ──► LangSmith Tracing
```

---

## 🧩 Project Structure

```
LangChain_practice/
│
├── LangChain/
│   ├── Data_Embedding/          # Embedding + VectorStore notebooks
│   ├── faiss_idx/               # Persisted FAISS vector index
│   │
│   ├── Data_extraction.ipynb    # RAG pipeline: load → split → retrieve
│   ├── llmModel.ipynb           # RAG + Groq LLaMA 3.3 integration
│   ├── genai_App.ipynb          # Full GenAI app prototype (notebook)
│   │
│   ├── app.py                   # 🚀 Streamlit app — deployed QA Bot
│   ├── document.pdf             # Source PDF for knowledge base
│   ├── Synopsis_Major_project.pdf
│   ├── test.txt                 # Test ingestion file
│
├── Requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Tech Stack

| Layer | Tool / Library |
|---|---|
| **Framework** | LangChain |
| **LLM** | Groq API — LLaMA 3.3 (70B Versatile) |
| **Embeddings** | HuggingFace `sentence-transformers` |
| **Vector DB** | FAISS (persisted locally) |
| **Frontend** | Streamlit |
| **Monitoring** | LangSmith |
| **Language** | Python 3.10+ |

---

## 🔄 Pipeline Breakdown

### 1️⃣ Data Ingestion & Splitting
- Loaded PDF using `PyPDFLoader`
- Split into chunks using `RecursiveCharacterTextSplitter`
- Explored chunk size, overlap, and splitting strategies

### 2️⃣ Embedding & VectorStore
- Generated embeddings using `HuggingFaceEmbeddings`
- Stored and persisted vectors using **FAISS** (`faiss_idx/`)
- Reloaded index for retrieval without re-embedding

### 3️⃣ RAG + LLM (llmModel.ipynb)
- Built a **RetrievalQA chain** using LangChain
- Connected FAISS retriever with **Groq's LLaMA 3.3**
- Extracted context-aware answers from the PDF

### 4️⃣ Streamlit App (app.py)
- Built a conversational QA interface
- System prompt: *"Act as an AI Engineer to answer questions based on the given context"*
- Used `ChatGroq` with streaming support
- Deployed live on **Streamlit Cloud**

### 5️⃣ Monitoring with LangSmith
- Integrated **LangSmith** tracing for all chain runs
- Tracked inputs, outputs, token usage, and latency

---

## 🛠️ Setup & Installation

### 1. Clone the repo
```bash
git clone https://github.com/ravicoder01/LangChain_practice.git
cd LangChain_practice
```

### 2. Install dependencies
```bash
pip install -r Requirements.txt
```

### 3. Set environment variables
Create a `.env` file in the root:
```env
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=langchain-practice
```

### 4. Run the Streamlit app
```bash
cd LangChain
streamlit run app.py
```

---

## 📦 Requirements

```
langchain
langchain-community
langchain-groq
faiss-cpu
sentence-transformers
pypdf
streamlit
python-dotenv
langsmith
```

---

## 💡 Key Learnings

- How RAG solves LLM hallucination by grounding responses in real documents
- FAISS index persistence — embed once, query many times
- Difference between `CharacterTextSplitter` and `RecursiveCharacterTextSplitter`
- Using Groq for blazing-fast LLaMA inference
- LangSmith for production-grade observability

---

## 👨‍💻 Author

**Ravi Roy**
B.Tech CSE (AI & ML) | IILM University, Greater Noida

[![GitHub](https://img.shields.io/badge/GitHub-ravicoder01-181717?style=flat&logo=github)](https://github.com/ravicoder01)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ravi%20Roy-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/ravi-roy)
[![Email](https://img.shields.io/badge/Email-raviroy2002@gmail.com-EA4335?style=flat&logo=gmail)](mailto:raviroy2002@gmail.com)

---

> *"RAG is not just a technique — it's the bridge between static LLMs and dynamic real-world knowledge."*
