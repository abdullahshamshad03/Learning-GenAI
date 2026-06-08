from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv

documents = [
    "hello my name is abdullah",
    "capital is delhi",
    "why machine learning"
]
embedding = GoogleGenerativeAIEmbeddings(model = "gemini-embedding-2-preview", output_dimensionality=32)

result = embedding.embed_documents(documents)

print(str(result))