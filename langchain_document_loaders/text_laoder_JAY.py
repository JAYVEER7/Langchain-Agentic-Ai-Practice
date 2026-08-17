from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()
model= ChatOpenAI()

prompt= PromptTemplate(
    template=" Write a summary of the following poem  \n {poem}",
    input_variables= ['poem']
)
parser= StrOutputParser()
loader= TextLoader('/home/jay/Desktop/JAY/AI/AI_Agent_LangChain/langchain_document_loaders/cricket.txt', encoding= 'utf-8')
doc= loader.load()

chain= prompt | model | parser
result= chain.invoke({'poem': doc[0].page_content})

# print(type(doc))
# print(len(doc))
# print(doc[0])

