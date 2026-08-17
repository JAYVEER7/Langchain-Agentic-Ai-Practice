from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

# chat_template= ChatPromptTemplate([
#     ('system', "You are a helpful {domain} expert."),
#     MessagesPlaceholder(variable_name='chat_history'),
#     ('human', "Explain in simple terms, what is teh {topic}")
#     # SystemMessage(content= "You are a helpful{domain} expert."),
#     # HumanMessage(content= "Explain in simple terms, what is teh {topic}")
# ])

# chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history= []
with open('/home/jay/Desktop/JAY/AI/AI_Agent_LangChain/Langchain_Prompt/chat_history.txt') as f:
    chat_history.extend(f.readlines())

# print(chat_history)

prompt= chat_template.invoke({'chat_history': chat_history, 'query':  "where is my refund?"})
print(prompt)
