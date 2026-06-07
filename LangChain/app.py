import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

os.environ["LANGCHAIN_API_KEY"]= os.environ.get("LANGCHAIN_API_KEY")

llm= ChatGroq(model="llama-3.3-70b-versatile")

prompt= ChatPromptTemplate.from_messages(
    [
        ("system", "Act as an AI Engineer and provide the answer based on context:"),
        ("user", "Question: {question}")
    ]
)

## Streamlit framework
st.title("Langchain demo with llama-3")
input_text= st.text_input("Enter your question here:")

## llama model
llm= ChatGroq(model="llama-3.3-70b-versatile")
output_parser= StrOutputParser()

chain= prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))
