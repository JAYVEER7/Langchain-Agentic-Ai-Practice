# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv

# load_dotenv()

# model= ChatOpenAI(model= 'gpt-5.6-sol')
# results= model.invoke(" Write down top 20 image processing related interview questions that are being asked in the top MNCs interviews? ")
# # results= model.invoke("Is BJP goebrnment capable to make the India a developed Country? kindly consider the aspects that are required to be in the policy maker and their ideology. Has Mr. Narendra Modi's government slowed down the progress of India by their decisions in past 12 years? Please answere precisly.")
# print(results)


#Practice
# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv

# load_dotenv()

# model= ChatOpenAI(model= 'gpt-5.6-sol', temperature= 0.2, streaming= True)
# results= model.invoke("How to think and speak structured and precise?" )
# print(results)


#### OpenAI Chat model
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()   ## this load the api key to the LLM
model_1= ChatOpenAI(model= 'gpt-4o-mini')
result= model_1.invoke("Which  is highest award in field of mathematics?")
print(result)