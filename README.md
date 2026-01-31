# 📄 Ask-the-Docs — RAG Based Document Question Answering
A full-stack **Retrieval-Augmented Generation (RAG)** system that allows users to upload documents (**PDF / TXT**) and ask natural-language questions grounded strictly in the uploaded content.

This project demonstrates **end-to-end AI system engineering**, covering backend RAG pipelines, UI integration, Dockerization, and real-world AWS deployment using **Nginx reverse proxy**.

---

## 🧠 What This Project Demonstrates

- Retrieval-Augmented Generation (RAG)
- Vector databases (FAISS)
- Semantic search using embeddings
- Context-grounded LLM answering
- Backend + UI separation
# 📄 Ask-the-Docs — RAG Based Document Question Answering System

A full-stack **Retrieval-Augmented Generation (RAG)** system that allows users to upload documents (**PDF / TXT**) and ask natural-language questions grounded strictly in the uploaded content.

This project demonstrates **end-to-end AI system engineering**, covering backend RAG pipelines, UI integration, Dockerization, and real-world AWS deployment using **Nginx reverse proxy**.

---

## 🧠 What This Project Demonstrates

- Retrieval-Augmented Generation (RAG)
- Vector databases (FAISS)
- Semantic search using embeddings
- Context-grounded LLM answering
- Backend + UI separation
- Dockerized microservices
- Cloud deployment (AWS EC2)
- Reverse proxy with Nginx
- Production-style architecture

---

## 🔍 Core Features

### ✅ Document Upload
- Supports **PDF** and **TXT**
- Automatic OCR fallback for scanned PDFs
- Large file upload support via Nginx configuration

### ✅ RAG Pipeline
- Recursive text chunking
- Semantic embeddings generation
- FAISS vector similarity search
- Top-k context retrieval
- Strict context-grounded answers

### ✅ Accurate Answers
- LLM answers strictly from retrieved document context
- Prevents hallucinations
- Clear fallback when answer is not found

### ✅ Source Tracking
- Retrieved document chunks are logged
- Answer sources stored for explainability

### ✅ Interaction Logging
- Every question and answer stored in:

- Includes timestamp, file name, question, answer, and sources

---

## 🧠 RAG Architecture (Backend)

### 1️⃣ Document Loading
- PDFs parsed using **Poppler**
- OCR fallback using **Tesseract**
- Text normalized and cleaned

### 2️⃣ Chunking
- RecursiveCharacterTextSplitter
- Overlapping chunks for context continuity

### 3️⃣ Embeddings
- Text embeddings generated for each chunk
- Stored in FAISS vector index

### 4️⃣ Retrieval
- User query embedded
- Top-K most relevant chunks retrieved
- Context dynamically assembled

### 5️⃣ Answer Generation
- Prompt constructed using:
  - retrieved context
  - user question
- LLM generates final grounded response

---

## ⚙️ Tech Stack

### Backend
- FastAPI
- Python 3.11
- FAISS
- OpenAI / LLM API
- Tesseract OCR
- Poppler Utils

### Frontend
- Gradio
- Clean vertical user interface
- File upload and Q&A workflow

### Infrastructure
- Docker
- AWS EC2
- Nginx Reverse Proxy

---

## 🐳 Docker Architecture

### Backend Container
- Runs FastAPI application
- Exposed internally on port **8000**
- Accessible via Nginx route `/api`

### UI Container
- Runs Gradio interface
- Exposed internally on port **7860**
- Served publicly via Nginx root `/`

### Benefits
- Clean separation of concerns
- Independent service scaling
- Environment isolation
- Production-ready deployment

---

## 🌐 Nginx Reverse Proxy

Nginx handles:

- Public access on port **80**
- Routing between UI and backend
- Large file upload handling
- Security boundary between internet and containers

---

## ☁️ AWS Deployment

### Platform
- AWS EC2 (Amazon Linux 2023)
- Free Tier compatible

### Deployment Flow
1. Build Docker images locally  
2. Push images to Docker Hub  
3. Pull images on EC2 instance  
4. Run containers  
5. Configure Nginx reverse proxy  
6. Expose public IP for browser access  

---

## 📁 Project Structure

ask-the-docs/
│
├── backend/
│ ├── app.py
│ ├── rag/
│ │ ├── loader.py
│ │ ├── chunker.py
│ │ ├── embeddings.py
│ │ ├── vector_store.py
│ │ ├── retriever.py
│ │ └── prompt.py
│ ├── llm/
│ ├── utils/
│ ├── Dockerfile
│
├── ui/
│ ├── app.py
│ ├── Dockerfile
│
├── logs/
│   └── history.json
│
├── .gitignore
└── README.md



---

## 🚀 Future Improvements

- Multi-user session isolation
- Persistent vector storage
- Chat-style UI
- Streaming responses
- Authentication
- HTTPS and custom domain
- Docker Compose orchestration



- Dockerized microservices
- Cloud deployment (AWS EC2)
- Reverse proxy with Nginx
- Production-style architecture

---

## 🔍 Core Features

### ✅ Document Upload
- Supports **PDF** and **TXT**
- Automatic OCR fallback for scanned PDFs
- Large file upload support via Nginx configuration

### ✅ RAG Pipeline
- Recursive text chunking
- Semantic embeddings generation
- FAISS vector similarity search
- Top-k context retrieval
- Strict context-grounded answers

### ✅ Accurate Answers
- LLM answers strictly from retrieved document context
- Prevents hallucinations
- Clear fallback when answer is not found

### ✅ Source Tracking
- Retrieved document chunks are logged
- Answer sources stored for explainability

### ✅ Interaction Logging
- Every question and answer stored in:

- Includes timestamp, file name, question, answer, and sources

---

## 🧠 RAG Architecture (Backend)

### 1️⃣ Document Loading
- PDFs parsed using **Poppler**
- OCR fallback using **Tesseract**
- Text normalized and cleaned

### 2️⃣ Chunking
- RecursiveCharacterTextSplitter
- Overlapping chunks for context continuity

### 3️⃣ Embeddings
- Text embeddings generated for each chunk
- Stored in FAISS vector index

### 4️⃣ Retrieval
- User query embedded
- Top-K most relevant chunks retrieved
- Context dynamically assembled

### 5️⃣ Answer Generation
- Prompt constructed using:
  - retrieved context
  - user question
- LLM generates final grounded response

---

## ⚙️ Tech Stack

### Backend
- FastAPI
- Python 3.11
- FAISS
- OpenAI / LLM API
- Tesseract OCR
- Poppler Utils

### Frontend
- Gradio
- Clean vertical user interface
- File upload and Q&A workflow

### Infrastructure
- Docker
- AWS EC2
- Nginx Reverse Proxy

---

## 🐳 Docker Architecture

### Backend Container
- Runs FastAPI application
- Exposed internally on port **8000**
- Accessible via Nginx route `/api`

### UI Container
- Runs Gradio interface
- Exposed internally on port **7860**
- Served publicly via Nginx root `/`

### Benefits
- Clean separation of concerns
- Independent service scaling
- Environment isolation
- Production-ready deployment

---

## 🌐 Nginx Reverse Proxy

Nginx handles:

- Public access on port **80**
- Routing between UI and backend
- Large file upload handling
- Security boundary between internet and containers

---

## ☁️ AWS Deployment

### Platform
- AWS EC2 (Amazon Linux 2023)
- Free Tier compatible

### Deployment Flow
1. Build Docker images locally  
2. Push images to Docker Hub  
3. Pull images on EC2 instance  
4. Run containers  
5. Configure Nginx reverse proxy  
6. Expose public IP for browser access  

---


## 🚀 Future Improvements

- Multi-user session isolation
- Persistent vector storage
- Chat-style UI
- Streaming responses
- Authentication
- HTTPS and custom domain
- Docker Compose orchestration



