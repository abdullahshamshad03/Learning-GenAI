from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model = "llama-3.3-70b-versatile")

prompt1 = PromptTemplate(
    template = "Give me the joke on this {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = "Explain the following joke - {text}",
    input_variable = ['text']
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

print(chain.invoke({'topic' : 'India'}))