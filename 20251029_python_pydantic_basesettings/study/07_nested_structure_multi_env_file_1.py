# 07_nested_structure_multi_env_file.py
# 첫 번째 방식 : 여러 BaseSettings 들을 가지는 상위 클래스 만들기
# 장점 : 명확함 / 단점 : 환경 변수 파일을 여러 번 읽어들여 비효율적
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

class AppSettings(BaseSettings):
    
    service: ServiceSettings = ServiceSettings()
    logging: LoggingSettings = LoggingSettings()

settings = AppSettings()

print(settings.service.TIMEOUT)
print(settings.logging.LOG_LEVEL)