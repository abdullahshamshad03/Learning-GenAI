from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

#template1

template1 = PromptTemplate(
    template = "Explain me about the {topic}",
    input_variables = ['topic']
)

#template2

template2 = PromptTemplate(
    template = "Write a 5 lines summary on the following text \n {text}",
    input_variables=['text'] 
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic' : 'blackhole'})
print(result)
