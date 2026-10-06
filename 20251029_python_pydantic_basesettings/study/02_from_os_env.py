from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

class AppSettings(BaseSettings):
    Path:str
    model_config = SettingsConfigDict()

settings = AppSettings()

print(settings.TEST_ENV_VARIABLE)