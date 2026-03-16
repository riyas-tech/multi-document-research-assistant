from langchain_community.vectorstores import FAISS
from app.ingestion.embeddings import get_embeddings

def create_vectorstore(chunks):
    embeddings = get_embeddings()
    vectorstore = FAISS.from_embeddings(
        chunks,
        embeddings
    )
    return vectorstore

def save_vectorstore(vectorstroe):
    vectorstroe.save_local("vectorstore")

def load_vectorstore():
    embeddings = get_embeddings()

    return FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )    