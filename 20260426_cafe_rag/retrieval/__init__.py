from config.config import secret
from llm import embedding
from retrieval import vectorstores
from . import vectorstores
from chromadb import Collection

def retrieve(query:str,
             db:Collection|None=None,
             api_key:str|None=secret["apikey"]["google"],
             num_result:str|None=1,):
    if db is None:
        db = vectorstores.get_chroma_collection("vector_store", "aurora_cafe_vector_db")
    query_embedding = embedding.embedding(api_key=api_key, text=query)
    result = vectorstores.retrieve(collection=db,
                                   query_embeddings=query_embedding,
                                   num_result=num_result)
    return result
