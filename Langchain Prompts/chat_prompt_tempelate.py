from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model = "llama-3.3-70b-versatile")

chat_tempelate = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain me {topic} in simple terms')
])

prompt = chat_tempelate.invoke(
    {
        'domain': 'Cricket',
        'topic' : 'Hit Wicket'
    }
)

print(prompt)