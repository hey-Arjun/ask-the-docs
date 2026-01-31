import os
from langchain_community.vectorstores import FAISS
from rag.embeddings import get_embedding_model

def create_faiss_index(chunks: list):
    """
    Create FAISS vector store from text chunks
    """
    embeddings = get_embedding_model()
    vector_store = FAISS.from_texts(
        texts = chunks,
        embedding = embeddings
    )
    return vector_store

def save_faiss_index(vector_store, path: str = "data/faiss_index"):
    """
    Save FAISS index locally
    """
    vector_store.save_local(path)

def load_faiss_index(path: str = "data/faiss_index"):
    """
    Load FAISS index from disk
    """
    embeddings = get_embedding_model()
    if not os.path.exists(path):
        raise FileNotFoundError("FAISS index not found")
    
    return FAISS.load_local(
        path, 
        embeddings,
        allow_dangerous_deserialization=True
    )