from langchain_google_genai import ChatGoogleGenerativeAI
import os
from config.config import secret

# 모델 로딩
def load_model(api_key:str|None=secret["apikey"]["google"], model_name:str|None="gemini-2.5-flash-lite"):
    os.environ["GOOGLE_API_KEY"] = api_key
    model = ChatGoogleGenerativeAI(model=model_name)
    return model