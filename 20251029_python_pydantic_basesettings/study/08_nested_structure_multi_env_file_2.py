# 08_nested_structure_recommend_2.py
# 두 번째 방식 : 각각 따로 여러 BaseSettings 들을 만들기
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

class ServiceSettings(BaseSettings):
    TIMEOUT: int
    MULTIPROCESSOR_NUM: int
    model_config = SettingsConfigDict(
        env_file="core/service.env",
        env_file_encoding='utf-8',
        env_prefix='SERVICE__', # DEV__ 로 시작하는 항목만 읽어들임
        extra='ignore'      # 그 외의 항목은 무시함 (다른 값이 있다면 필수!)
    )

class LoggingSettings(BaseSettings):
    EXPIRE_DAY: int
    LOG_LEVEL: str
    model_config = SettingsConfigDict(
        env_file="core/logging.env",
        env_file_encoding='utf-8',
        env_prefix='LOGGING__', # PRDO 로 시작하는 항목만 읽어들임
        extra='ignore'       # 그 외의 항목은 무시함 (다른 값이 있다면 필수!)
    )


service_settings: ServiceSettings = ServiceSettings()
logging_settings: LoggingSettings = LoggingSettings()

print(service_settings.TIMEOUT)
print(logging_settings.LOG_LEVEL)