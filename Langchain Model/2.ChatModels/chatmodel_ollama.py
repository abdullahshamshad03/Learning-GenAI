from langchain_ollama import ChatOllama

model = ChatOllama(model="gemma3:4b")

result = model.invoke("capital of India?")

print(result)
print()
print(result.content)
