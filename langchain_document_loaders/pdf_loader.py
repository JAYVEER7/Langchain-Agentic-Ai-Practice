from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('/home/jay/Desktop/JAY/AI/AI_Agent_LangChain/langchain_document_loaders/dl-curriculum.pdf')

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)