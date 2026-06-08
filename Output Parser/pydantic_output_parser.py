from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

class Person(BaseModel):
    
    name:str = Field(description='Name of the Person')
    age:int = Field(description='Age of the person', gt=18)
    city : str = Field(description='City of the person the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

tempelate = PromptTemplate(
    template= "Generate the name, age city of a fictional {place} person \n {format_instruction}",
    input_variables=['place'],
    partial_variables={'format_instruction': parser.get_format_instructions()} 
)


chain = tempelate | model | parser 

result = chain.invoke({'place': 'indian'})

print(result)