from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview")

result = model.invoke("capital of India?")

print(result)
print()
print(result.content[0]['text'])









# from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
# client = genai.Client()

# response = client.models.generate_content(
#     model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
# )

# response = client.invoke("Explain how AI works in a few words") this is not working
# print(response.text)