from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate 


load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

#1st tempelate
tempelate1 = PromptTemplate(
    template = "Explain me about this {topic}",
    input_variables= ["topic"]
)

#2nd tempelate

tempelate2 = PromptTemplate(
    template = 'Write a 5 lines summary on the following text. /n {text}',
    input_variables=['text']
)

prompt1 = tempelate1.invoke({'topic': 'Black Hole'})

result1 = model.invoke(prompt1)

prompt2 = tempelate2.invoke({'text': result1.content})

result2 = model.invoke(prompt2)

print(result2.content)