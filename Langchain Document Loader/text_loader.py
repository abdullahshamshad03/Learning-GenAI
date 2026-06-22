from langchain_groq import ChatGroq
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model = "llama-3.3-70b-versatile")

prompt = PromptTemplate(
    template = "write the short summary on the following \n {poem}",
    input_variables=['poem']
)

loader = TextLoader('cricket.txt', encoding = 'utf-8')

docs = loader.load()

parser = StrOutputParser()

chain = prompt | model | parser

print(chain.invoke({'poem': docs[0].page_content}))

