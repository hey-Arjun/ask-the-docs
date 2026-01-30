
def retrieve_context(vector_store, query: str, k: int = 3):
    """
    Rettrieve top-K  relevant document chunks
    """
    docs = vector_store.similarity_search(query, k=k)
    context = "\n\n".join([doc.page_content for doc in docs])
    sources = [doc.page_content for doc in docs]
    
    return context, sources