from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class AppSettings(BaseSettings):
    TEST_ENV_VARIABLE:str       # 하단 os.environ 으로 추가하는 환경변수
    EXPORT_FROM_TERMINAL:str    # 터미널에서 직접 추가하는 환경변수
    model_config = SettingsConfigDict()

os.environ['TEST_ENV_VARIABLE'] = "base_setting_custom_env_test" # export custom env
settings = AppSettings()

print(settings.TEST_ENV_VARIABLE)
print(settings.EXPORT_FROM_TERMINAL)