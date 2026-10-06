from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class AppSettings(BaseSettings):
    
    model_config = SettingsConfigDict(
        secrets_dir="core/secrets/"
    )
    
    dummy_secret_1: str
    dummy_secret_2: str

settings = AppSettings()

print(settings.dummy_secret_1)
print(settings.dummy_secret_2)