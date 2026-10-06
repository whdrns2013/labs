import chromadb
from config.config import config

# 벡터스토어 로딩
def get_chroma_collection(dir_path:str|None = config["path"]["vector_store"],
                          collection_name:str|None = config["name"]["collection"]):
    client = chromadb.PersistentClient(path = dir_path)
    collection = client.get_or_create_collection(collection_name)
    return collection

# 문서 저장
def upsert_document(collection:chromadb.Collection,
                    ids:list[str],
                    documents:list[str],
                    embeddings:list[list[float]]|None=None,
                    metadatas:list|None=None):
    parameters = {"ids":ids, "documents":documents}
    if embeddings is not None:
        parameters.update({"embeddings":embeddings})
    if metadatas is not None:
        parameters.update({"metadatas":metadatas})
    collection.upsert(**parameters)
    return collection

# 문서 검색
def retrieve(collection:chromadb.Collection,
             query_texts:list[str]|None=None,
             query_embeddings:list[list[float]]|None=None,
             num_result:int=10):
    if query_texts is not None:
        result = collection.query(query_texts=query_texts, n_results=num_result)
    elif query_embeddings is not None:
        result = collection.query(query_embeddings=query_embeddings, n_results=num_result)
    else:
        raise ValueError("필요한 값이 입력되지 않았습니다.")
    return result["documents"][0][0]