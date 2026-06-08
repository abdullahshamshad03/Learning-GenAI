from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch,RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatGroq(model = "llama-3.3-70b-versatile")

parser1 = StrOutputParser() 

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description = "Give the sentiment of the feedback.")

parser2 = PydanticOutputParser(pydantic_object = Feedback)

prompt1 = PromptTemplate(
    template = 'Classify the sentiment of the following feedback text into positive or negative. \n {feedback} \n {format_instructions}',
    input_variables = ['feedback'],
    partial_variables = {'format_instructions': parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template = 'Write appropriate response for positive feedback \n {feedback}',
    input_variables=['feedback']
)
prompt3 = PromptTemplate(
    template = 'Write appropriate response for negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2|model|parser1 ),
    (lambda x:x.sentiment == 'negative', prompt3|model|parser1),
    RunnableLambda(lambda x: "could not find the sentiment.")
)

final_chain = classifier_chain | branch_chain

result = final_chain.invoke({'feedback': 'Hello'})

print(result)

