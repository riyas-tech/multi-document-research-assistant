from langchain_openai import ChatOpenAI
from app.rag.retriever import get_retriever

llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )  

    
def research_answer(question):
    retriever = get_retriever()
    docs = retriever.invoke(question)
    context = "\n\n".join(
        [d.page_content for d in docs]
    )
    prompt = f"""
        You are a research assistant. 
        Use the context below to answer the question.
        Provide citations with docuement names. 

        Context: {context}
        Question : {question}

        Answer:
    """

    result = llm.invoke(prompt)
    sources = []
    for d in docs:
        sources.append(d.metadata.get("source"))
    return result.content, sources