import os
from config.config import config, secret
from .vectorstores import get_chroma_collection, upsert_document
from llm.embedding import embedding

def read_documents(document_dir_path:str|None=config["path"]["documents"]):
    documents = []
    for file in os.listdir(document_dir_path):
        file_path = os.path.join(document_dir_path, file)
        with open(file_path, "r", encoding="utf-8") as f:
            documents.append(f.read())
    return documents

def init(document_dir_path:str|None=config["path"]["documents"],
         vector_db_dir_path:str|None = config["path"]["vector_store"],
         collection_name:str|None = config["name"]["collection"],
         api_key:str|None = secret["apikey"]["google"]):
    collection = get_chroma_collection(dir_path = vector_db_dir_path,
                                       collection_name = collection_name)
    documents = read_documents(document_dir_path)
    ids = [f"id_{i}" for i in range(len(documents))]
    embeddings = [embedding(text=doc, api_key=api_key) for doc in documents]
    collection = upsert_document(collection, ids, documents, embeddings)
    return collection
    