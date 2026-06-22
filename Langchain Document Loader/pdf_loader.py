from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Introduction to Machine Learning with Python ( PDFDrive.com )-min.pdf')
docs = loader.load()

# print(len(docs))

# print(docs[4].page_content)
print(docs[4].metadata)