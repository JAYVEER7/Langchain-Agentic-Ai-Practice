from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()
embedding=OpenAIEmbeddings(model='text-embedding-3-large', dimensions=200)
documents=[
    "Runs on HuggingFace model (no API key needed).",
    "Uses LangChain for agent + tools.",
    "Integrates RAG for knowledge grounding.",
    "Can later be quantized/pruned for Jetson deployment."
]

query="Which Models should I use if I don't have API key?"
doc_embedding=embedding.embed_documents(documents)
query_embedding=embedding.embed_query(query)

scores=cosine_similarity([query_embedding], doc_embedding)[0]
print(f" Cosine Similary is as: {scores}")
score_list=list(enumerate(scores))
# print(list(enumerate(scores)))  
sorted_scores=sorted(score_list, key=lambda x:x[1])
index, score_value=sorted_scores[-1] 
print(f" sorted score is as:{ sorted_scores} \n max similarity index: {index} \n score :{score_value}")