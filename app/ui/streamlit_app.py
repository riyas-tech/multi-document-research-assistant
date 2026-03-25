import streamlit as st
from app.rag.research_chain import research_answer

st.title("Multi PDF Research Assistant")

question = st.text_input("Ask a research question")

if st.button("Search"):

    answer, sources = research_answer(question)

    st.write("### Answer")

    st.write(answer)

    st.write("### Sources")

    for s in set(sources):
        st.write("-", s)