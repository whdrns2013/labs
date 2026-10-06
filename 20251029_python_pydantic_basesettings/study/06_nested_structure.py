from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

class ServiceSettings(BaseSettings):
    TIMEOUT: int
    MULTIPROCESSOR_NUM: int

class LoggingSettings(BaseSettings):
    EXPIRE_DAY: int
    LOG_LEVEL: str

class AppSettings(BaseSettings):
    
    service: ServiceSettings
    logging: LoggingSettings
    
    model_config = SettingsConfigDict(
        env_file="core/06.env",
        env_file_encoding='utf-8',
        env_nested_delimiter='__' # __로 구분
    )

settings = AppSettings()

print(settings.service.TIMEOUT)
print(settings.logging.LOG_LEVEL)