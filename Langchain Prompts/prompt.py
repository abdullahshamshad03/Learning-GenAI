from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = GoogleGenerativeAI(model="gemini-3.1-flash-lite-preview")

st.header("Research Paper Summary")

user_input = st.text_input("Enter your prompt")

if st.button('Summarize'):
    result = model.invoke(user_input)
    st.write(result)
