from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import JsonOutputParser
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema
load_dotenv()

# Define the model
# llm = HuggingFaceEndpoint(
#     repo_id="google/gemma-2-2b-it",
#     task="text-generation"
# )

# model = ChatHuggingFace(llm=llm)
model= ChatOpenAI(model='gpt-4o-mini')

schema= [
    ResponseSchema(name ='fact1', description = ' fact 1 about the topic'),
    ResponseSchema(name ='fact2', description = ' fact 2 about the topic'),
    ResponseSchema(name ='fact3', description = ' fact 3 about the topic'),

]

parser = StructuredOutputParser.from_response_schemas(schema)
template= PromptTemplate(
    template= 'Give 3 facts about the {topic} \n {format_instruction}',
    input_variables= ['topic'],
    parser = StructuredOutputParser.from_response_schemas(schema)

)

prompt= template.invoke({'topic':'Cosmology'})
result= model.invoke(prompt)
final_result= parser.parse(result.content)

print(final_result)
