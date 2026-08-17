from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model= ChatGoogleGenerativeAI(model= "gemini-3.1-flash-lite")

result= model.invoke("What is the knowledge cutoff date of gemini-2.0-flash model ?")

print(result)