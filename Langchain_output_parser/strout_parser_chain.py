from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation"
# )

# model = ChatHuggingFace(llm=llm)

model= ChatOpenAI(model='gpt-4o-mini')
template1= PromptTemplate(
    template="Write few lines about {topic}",
    input_variables= ['topic']
)

template2= PromptTemplate(
    template= " Write a 5 line summary of the following text. /n {text}",
    input_variables =['text']
)
# prompt1= template1.invoke({'topic': 'Black Hole'})
# print(prompt1,type(prompt1))
# result= model.invoke(prompt1)

# prompt2= template2.invoke({'text': result.content})

# result2= model.invoke(prompt2)

# print(result2.content)
parser= StrOutputParser()

chain= template1 | model | parser | template2 | model | parser

result= chain.invoke({'topic': 'Black Hole'})
print(result)

