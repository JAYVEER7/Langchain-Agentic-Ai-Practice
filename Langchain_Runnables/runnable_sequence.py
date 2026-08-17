from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
prompt1= PromptTemplate(
    template= "Wrte about the {topic}",
    input_variables= ['topic']
)

prompt2= PromptTemplate(
    template= "Summarise the text :{text}",
    input_variables= ['text']
)

model= ChatOpenAI()
parser= StrOutputParser()

chain= RunnableSequence(prompt1, model, parser, prompt2, model, parser)
result= chain.invoke({'topic': 'Fourier Series'})

print(result)
