from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

class AppSettings(BaseSettings):
    config_1:int = 1
    service_port:int = 8080
    model_config = SettingsConfigDict()

settings = AppSettings()

print(settings.service_port)