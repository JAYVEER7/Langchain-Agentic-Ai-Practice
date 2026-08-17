from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader= PyPDFLoader('Lanchain_Text_splitter/dl-curriculum.pdf')
docs= loader.load()

splitter= CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap= 10,
    separator= ''
)

result= splitter.split_documents(docs)
print(result[1].page_content)