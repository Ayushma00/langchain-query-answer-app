import os
import streamlit as st
import pickle
import time
import langchain
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

st.title("Ask Me Anything")
st.sidebar.title("Your Answer Buddy")
st.sidebar.write(
    "Hello I am your buddy. I can help you answers your queries from the weblinks that you provide me 😊"
)
urls = []
for i in range(3):
    url = st.sidebar.text_input(f"Website {i+1}")
    urls.append(url)
file_path = "vectorstore"
url_submitted = st.sidebar.button("Submit")
llm = OpenAI(temperature=0.9, max_tokens=500)
print(url_submitted)
placeholder = st.empty()
if url_submitted:
    loader = UnstructuredURLLoader(urls=urls)
    data = loader.load()
    placeholder.text("Data Loading")
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", ","], chunk_size=1000
    )
    placeholder.text("Text Splitter")
    docs = text_splitter.split_documents(data)
    embeddings = OpenAIEmbeddings()
    vectorstore_openai = FAISS.from_documents(docs, embeddings)
    placeholder.text("Embedding Vector Started Building")
    time.sleep(2)
    file_path = "vectorstore"
    vectorstore_openai.save_local(file_path)
    placeholder.text("Embedding Vector Started Building")


query = placeholder.text_input("Your Query")

if query:
    if os.path.exists(file_path):
        x = FAISS.load_local(
            "vectorstore", OpenAIEmbeddings(), allow_dangerous_deserialization=True
        )
        retriever = x.as_retriever()
        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=retriever)
        result = chain({"question": query}, return_only_outputs=True)
        st.write("Answer:")
        st.write(result["answer"])
        sources = result.get("sources", "")
        if sources:
            st.write("Sources:")
            sources_list = sources.split("\n")  # Split the sources by newline
            for source in sources_list:
                st.write(source)
