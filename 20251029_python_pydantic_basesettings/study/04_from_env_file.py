from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class AppSettings(BaseSettings):
    
    DEV__TIMEOUT:int
    DEV__LOG_LEVEL:str
    
    TEST__TIMEOUT:int
    TEST__LOG_LEVEL:str
    
    PROD__TIMEOUT:int
    PROD__LOG_LEVEL:str
    
    model_config = SettingsConfigDict(
        env_file="core/04.env",
        env_file_encoding='utf-8'
    )

settings = AppSettings()

print(settings.DEV__TIMEOUT)
print(settings.TEST__LOG_LEVEL)

# env_file : 기본값 : Path('') : 현재 디렉터리 / None 을 전달하면 .env 파일에서 환경 변수를 로드하지 않도록 할 수 있다.