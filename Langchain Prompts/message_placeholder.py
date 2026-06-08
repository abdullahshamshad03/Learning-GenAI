from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

#model

model = ChatGroq(model="llama-3.3-70b-versatile")

#chat tempelate
chat_tempelate = ChatPromptTemplate([
    ('system', "You are a AI chat assistant"),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')    
])

chat_history = [] # ek empty list bana lenge jisme append kar denge previous chats 

#load previos chat files
with open ('chat_history.txt') as f:
    # chat_history.extend(f.readlines())
    for line in f:
        chat_history.extend(("human", line.strip()))

print(chat_history)

query = "Where is my refund?"
chat_history.append(HumanMessage(content = query))
# create prompt
prompt = chat_tempelate.invoke({
    'chat_history' : chat_history,
    'query' : query
})

result = model.invoke(prompt)
chat_history.append(AIMessage(content = result.content))

print()
print("You: ", query)
print("AI: ", result.content)

