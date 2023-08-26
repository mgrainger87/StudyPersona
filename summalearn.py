import streamlit as st
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    SystemMessagePromptTemplate)
from langchain.document_loaders import *
from langchain.chains.summarize import load_summarize_chain
import tempfile
from langchain.docstore.document import Document

st.title("SummaLearn")

uploaded_file = st.file_uploader("Upload PDF File", type=["pdf"])
file_path = None
if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        file_path = temp_file.name
        st.session_state['file_path'] = file_path

def load_document(file_path):
    from langchain.document_loaders import UnstructuredPDFLoader
    loader = UnstructuredPDFLoader(file_path, mode="elements", strategy="fast")
    docs = loader.load()
    return docs

document = None
if file_path:
    document = load_document(file_path)

document_string = ""
if document:
    document_string = "".join([doc.page_content for doc in document])

persona_description = st.text_area("Enter Persona Description")

def documentSummarizer(document_string, persona_description):
    chat = ChatOpenAI(
        model="gpt-3.5-turbo-16k",
        temperature=0
    )
    system_template = """You are an AI assistant tasked with generating a summary of a document based on the provided persona description."""
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_template = """Using the persona description '{persona_description}', please generate a summary of the document: '{document_string}'."""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    result = chain.run(document_string=document_string, persona_description=persona_description)
    return result

summary = ""
if document_string and persona_description:
    summary = documentSummarizer(document_string, persona_description)

st.markdown(summary)

st.button("Submit")
