from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
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

get_joke_chain = RunnableSequence(prompt1,model,parser)

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'explanation' : RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(get_joke_chain, parallel_chain)

print(final_chain.invoke({'topic': 'AI'}))