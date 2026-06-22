from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model = "llama-3.3-70b-versatile")

prompt1 = PromptTemplate(
    template = "Generate a tweet on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = "Generate a Linkedin post on {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet' : RunnableSequence(prompt1, model, parser),
    'linkedin' : RunnableSequence(prompt2, model, parser)
})

result = parallel_chain.invoke({'topic': 'AI'})

print(result['tweet'])
print(result['linkedin'])