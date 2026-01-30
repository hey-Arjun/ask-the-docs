from fastapi import FastAPI, UploadFile, File
from rag.loader import load_document
from rag.chunker import chunk_text
from rag.vector_store import create_faiss_index
from rag.retriever import retrieve_context
from rag.prompt import build_rag_prompt
from llm.generator import generate_answer
from utils.logger import log_interaction

import shutil
import os

app = FastAPI(title = "Ask the docs - RAG App")

VECTOR_DB = None
CURRENT_FILE = None

@app.get("/")
def health_check():
    return "Health status OK"

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    global VECTOR_DB, CURRENT_FILE

    os.makedirs("data/uploads", exist_ok=True)
    filename = os.path.basename(file.filename)
    file_path = os.path.join("data/uploads", filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    #1 Load doc
    text = load_document(file_path)

    #2 Chunk text
    chunks = chunk_text(text)

    #3 Create FAISS index
    VECTOR_DB = create_faiss_index(chunks)

    CURRENT_FILE = filename

    return {
        "message": "Document Processed successfully",
        "total_chunks": len(chunks)
    }

@app.post("/ask")
async def ask_question(question: str):
    global VECTOR_DB, CURRENT_FILE

    if VECTOR_DB is None:
        return {"error": "Please Upload a document first"}
    
    if not question or len(question.strip()) < 3:
        return {"error": "Question too short"}
    
    
    #4 Retreive context
    context, sources = retrieve_context(VECTOR_DB, question)

    if not context.strip():
        return {
            "question": question,
            "answer": "I cannot find the answer in the provided document.",
            "sources": []
        }

    #5 Build Rag Prompt
    prompt = build_rag_prompt(context, question)

    #6 Generate Answer
    answer = generate_answer(prompt)

    #7 Logging
    log_interaction(
        filename = CURRENT_FILE,
        question = question,
        answer = answer,
        sources = sources
    )

    return {
        "question": question,
        "answer": answer,
        "sources": sources[:2]
    }