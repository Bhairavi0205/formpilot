from rag.embeddings import get_vectorstore

def get_retriever(k=4):
    """
    Get retriever from vectorstore
    k = number of chunks to retrieve per query
    """
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k}
    )
    return retriever

def retrieve_context(query, k=4):
    """
    Retrieve relevant context for a query
    Returns list of relevant document chunks
    """
    retriever = get_retriever(k=k)
    docs = retriever.invoke(query)
    
    context = ""
    for i, doc in enumerate(docs):
        context += f"\n--- Source {i+1} ---\n"
        context += doc.page_content
        context += "\n"
    
    return context