from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

st.header("Research Paper Summary")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

#tempelate
tempelate = load_prompt('tempelate.json')

prompt = tempelate.invoke({ # yeh bas prompt mai apne jo input variables hai usme values humaare variable kai assin kar de raha hai
    'paper_input':paper_input,
    'style_input' : style_input,
    'length_input' : length_input
    
})
# print(result.content)

if st.button('Summarize'):
    result = model.invoke(prompt)
    st.write(result.content)
    
