from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model= ChatOpenAI(model= 'gpt-4', temperature= 0.1)
results= model.invoke("What is the first prime number ?")
print(f" result: {results.content}")