from app.ingestion.loader import load_pdfs
from app.ingestion.chunking import chunk_documents
from app.ingestion.vectorstore import create_vector_store, save_vector_store
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

def run():
    docs = load_pdfs("data/pdfs")
    chunks = chunk_documents(docs)
    vectorstore = create_vector_store(chunks)
    save_vector_store(vectorstore)
    print("vector store created successfully....")

if __name__ == "__main__":
    run()
