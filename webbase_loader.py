from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model = "llama-3.3-70b-versatile")

url = 'https://www.amazon.in/Apple-2026-MacBook-laptop-chip/dp/B0GR1G3C3X/ref=asc_df_B0GR1G3C3X?mcid=8892dbf9ae093fed8924eb3f55b24579&tag=googleshopdes-21&linkCode=df0&hvadid=794212938611&hvpos=&hvnetw=g&hvrand=16551863418730671910&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9302611&hvtargid=pla-2471864468783&psc=1&hvocijid=16551863418730671910-B0GR1G3C3X-&hvexpln=0&gad_source=1'

loader = WebBaseLoader(url)

prompt = PromptTemplate(
    template = "Answer the question \n {question} based on the following text, \n {text}",
    input_variables=['question','text'] 
)

parser = StrOutputParser()

docs = loader.load()

chain = prompt | model | parser
print(chain.invoke({'question': "what is the price of this laptop?",'text': docs[0].page_content}))
