from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnablePassthrough, RunnableBranch
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model = "llama-3.3-70b-versatile")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="write a detail on {topic}",
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template="summarie the following text:\n {text}",
    input_variables=['text']
)

report_gen_chain = RunnableSequence(prompt1,model,parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) >200, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

print(final_chain.invoke({'topic': 'Russia vs Ukraine war'}))