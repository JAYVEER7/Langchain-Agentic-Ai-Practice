from langchain_openai import OpenAI, ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

st.header("Research Tool")
model=ChatOpenAI(model='gpt-4', temperature=0.2)

# user_input=st.text_input("Enter Your prompt")

# if st.button('Summarise'):
#     st.text('What is latitude of the Jamshedpur and at what height from the sea level?')
#     result=model.invoke(user_input)
#     st.write(result.content)

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )
style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 
length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )



# template= PromptTemplate(
#     template="""
#         Please summarize the research paper titled "{paper_input}" with the following specifications:
#         Explanation Style: {style_input}  
#         Explanation Length: {length_input}  
#         1. Mathematical Details:  
#         - Include relevant mathematical equations if present in the paper.  
#         - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
#         2. Analogies:  
#         - Use relatable analogies to simplify complex ideas.  
#         If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
#         Ensure the summary is clear, accurate, and aligned with the provided style and length.
#         """,
#     input_variables=['paper_input', 'style_input', 'length_input' ],
#     validate_template= True 
# )

template= load_prompt('template.json')

# prompt= template.invoke({
#     'paper_input': paper_input,
#     'style_input': style_input, 
#     'length_input': length_input

# })

if st.button('Summarise'):

    # results= model.invoke(prompt)
    # st.write(results.content)
    chain= template | model
    results= chain.invoke({
        'paper_input':paper_input, 
        'style_input':style_input, 
        'length_input':length_input
    })
    st.write(results.content)