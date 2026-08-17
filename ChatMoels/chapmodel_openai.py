from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI(model='gpt-4', temperature=0.2)
result=model.invoke("write 3 Idian famous person's name ")
print(f" result as : {result.content}")


