from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import SemanticChunker
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv

load_dotenv()

# 1. Load the target document
loader = PyPDFLoader('Lanchain_Text_splitter/dl-curriculum.pdf')
docs = loader.load()

# 2. Provide the mandatory embedding layer
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# 3. Instantiate the chunker
splitter = SemanticChunker(embeddings)

# 4. Process the split
result = splitter.split_documents(docs)
print(f"Successfully generated {len(result)} semantic chunks.")
