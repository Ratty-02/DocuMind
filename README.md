# 📚 DocuMind

> AI-powered Document Question Answering using RAG, FastAPI, LangChain, ChromaDB, HuggingFace Embeddings, and Groq LLM.

---

## 🚀 Overview

DocuMind is a Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions based on their contents.

The system converts PDFs into embeddings, stores them in a vector database, retrieves relevant context, and generates accurate answers using a Large Language Model.

---

## ✨ Features

- 📄 PDF Upload & Processing
- 🔍 Semantic Search
- 🧠 Retrieval-Augmented Generation (RAG)
- 🤖 Groq LLM Integration
- ⚡ HuggingFace Embeddings
- 🏢 Multi-Tenant Support
- 🌐 FastAPI REST API
- ☁️ Railway Deployment
- 📚 Source Citations

---

## 🏗️ System Architecture

```text
User
 │
 ▼
FastAPI API
 │
 ├── Upload PDF
 │       │
 │       ▼
 │   PyPDF Loader
 │       │
 │       ▼
 │ Text Splitter
 │       │
 │       ▼
 │ Embeddings Model
 │       │
 │       ▼
 │    ChromaDB
 │
 └── Ask Question
         │
         ▼
 Similarity Search
         │
         ▼
     Context
         │
         ▼
      Groq LLM
         │
         ▼
      Answer
```

---

## 🛠️ Tech Stack

### Backend

- FastAPI
- Python

### AI Stack

- LangChain
- Groq
- HuggingFace Embeddings

### Vector Database

- ChromaDB

### Deployment

- Railway

---

## 📂 Project Structure

```text
DocuMind/
│
├── api/
│   ├── main.py
│   └── routes/
│       ├── upload.py
│       └── chat.py
│
├── rag/
│   ├── embeddings.py
│   ├── ingest.py
│   └── retrieve.py
│
├── uploads/
├── chroma_data/
│
├── requirements.txt
├── Procfile
├── .env
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Ratty-02/DocuMind.git

cd DocuMind
```

### Create Virtual Environment

```bash
python -m venv myenv
```

### Activate Environment

#### Windows

```bash
myenv\Scripts\activate
```

#### Linux / Mac

```bash
source myenv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory.

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run Locally

```bash
uvicorn api.main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## ☁️ Live Deployment

### API

https://documind-production-2d9b.up.railway.app

### Swagger Documentation

https://web-production-05dc20.up.railway.app/docs

---

## 📤 Upload PDF

### Endpoint

```http
POST /upload
```

### Parameters

| Parameter | Type |
|------------|--------|
| tenant_id | string |
| file | PDF |

---

## 💬 Ask Questions

### Endpoint

```http
POST /chat
```

### Example Request

```json
{
  "tenant_id": "demo",
  "question": "What is this document about?"
}
```

### Example Response

```json
{
  "answer": "This document discusses artificial intelligence and machine learning concepts.",
  "sources": [
    {
      "page": 2,
      "source": "sample.pdf"
    }
  ]
}
```

---

## 📈 Example Workflow

### 1. Upload PDF

```text
POST /upload
```

↓

### 2. Generate Embeddings

```text
PDF → Chunks → Embeddings → ChromaDB
```

↓

### 3. Ask Questions

```text
POST /chat
```

↓

### 4. Receive Grounded Answer

```text
Question + Retrieved Context → Groq LLM → Answer
```

---

## 🎯 Future Improvements

- Chat History
- Streaming Responses
- JWT Authentication
- PostgreSQL + pgvector
- Hybrid Search
- React Frontend
- User Accounts
- Evaluation Dashboard
- Docker Deployment
- RBAC Support

---



## 👨‍💻 Author

### Rehan Azad

B.Tech Computer Science Engineering  
GLS University

GitHub:
https://github.com/Ratty-02

---

⭐ If you like this project, consider giving it a star.
