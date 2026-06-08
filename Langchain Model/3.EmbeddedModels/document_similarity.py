from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()
embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview", output_dimensionality=300)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "tell me about virat kohli"

query_embedding = embedding.embed_query(query)
document_embedding = embedding.embed_documents(documents)

scores = cosine_similarity([query_embedding], document_embedding)[0] #match karega ki query ki embedding kiss document kai vector se similar hai

index, score = sorted(list(enumerate(scores)), key= lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score is:", score)