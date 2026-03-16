from langchain_community.document_loaders import PyPDFLoader

import os

def load_pdfs(directory):
    documents = []

    for file in os.listdir(directory):
        if file.endswith(".pdf"):
            path = os.path.join(directory, file)
            loader = PyPDFLoader(path)
            docs = loader.load()
            for d in docs:
                d.metadata["source"] = file

            documents.extend(docs)

    return documents
    
                