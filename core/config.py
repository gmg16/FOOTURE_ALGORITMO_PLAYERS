from pydantic import BaseSettings
class Settings(BaseSettings):

    WYSCOUT_USERNAME: str
    WYSCOUT_PASSWORD: str
    MONGO_CONN_STR: str

    class Config:
        case_sensitive = True
        env_file = '.env'


settings = Settings()
