from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatOllama(model="gemma3:4b")

st.header("Research Paper Summary")

user_input = st.text_input("Enter your prompt")

if st.button('Summarize'):
    result = model.invoke(user_input)
    st.write(result.content)