
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def word_counter(text):
    return len(text.split())

model = ChatGroq(model = "llama-3.3-70b-versatile")

prompt = PromptTemplate(
    template = "Give me the joke on this {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

gen_joke_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_counter)
})

final_chain = RunnableSequence(gen_joke_chain, parallel_chain)

result = final_chain.invoke({'topic':'AI'})

# final_result = """{}\n word count - {}""".format(result['joke'], result['word_count'])

final_result = f"{result['joke']}\n word count - {result['word_count']}"

print(final_result)