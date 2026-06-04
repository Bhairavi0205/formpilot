from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from rag.loader import load_documents, split_documents
import os

FAISS_PATH = "faiss_index"

def get_embeddings():
    """Load HuggingFace embeddings - runs locally, no API key needed"""
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}
    )
    return embeddings

def create_vectorstore():
    """Create FAISS vector store from exam documents"""
    print("Loading documents...")
    documents = load_documents()
    chunks = split_documents(documents)

    print("Creating embeddings... (first time thoda time lagega)")
    embeddings = get_embeddings()

    print("Building FAISS index...")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(FAISS_PATH)
    print(f"FAISS index saved to {FAISS_PATH}/")
    return vectorstore

def load_vectorstore():
    """Load existing FAISS index"""
    embeddings = get_embeddings()
    vectorstore = FAISS.load_local(
        FAISS_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )
    print("FAISS index loaded!")
    return vectorstore

def get_vectorstore():
    """Get vectorstore - load if exists, create if not"""
    if os.path.exists(f"{FAISS_PATH}/index.faiss"):
        print("Existing FAISS index found - loading...")
        return load_vectorstore()
    else:
        print("No FAISS index found - creating new one...")
        return create_vectorstore()