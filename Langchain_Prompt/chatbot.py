from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()

model= ChatOpenAI()
# chat_history= []
chat_history= [
    SystemMessage(content="You are a  helpful AI assistent")
]

messages= [
    SystemMessage(content=" You are a helpful assistant"),
    HumanMessage(content="Tell me about wikipedia")
]

# result= model.invoke(messages)
# messages.append(AIMessage(content= result.content))

# print(messages)

while True:
    user_input= input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input== 'exit':
        break
    result= model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI:", result.content)

print(f" chat_history: {chat_history}")
