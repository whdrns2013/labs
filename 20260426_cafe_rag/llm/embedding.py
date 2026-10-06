from google import genai

# google 임베딩
def embedding(text:str, api_key:str):
    client = genai.Client(api_key = api_key)
    result = client.models.embed_content(
            model="gemini-embedding-2",
            contents=text
    )
    return result.embeddings[0].values