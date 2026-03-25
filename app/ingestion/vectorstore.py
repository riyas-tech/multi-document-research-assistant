from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

def create_vector_store(chunks):
    embeddings = OpenAIEmbeddings()

    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )
    return vectorstore

def save_vector_store(vectorstore):
    vectorstore.save_local("vectorstore")

def load_vector_store():
    embeddings = OpenAIEmbeddings()

    return FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )      