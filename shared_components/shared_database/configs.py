from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import ValidationError
from dotenv import load_dotenv


load_dotenv()


class DatabaseSettings(BaseSettings):
    PGHOST: str
    PGUSER: str
    PGPASSWORD: str
    PGPORT: str
    PGDATABASE: str
    try:
        model_config = SettingsConfigDict(
            env_file=".env", env_file_encoding="utf-8", extra="allow"
        )
    except ValidationError as exc:
        print(repr(exc.errors()[0]["type"]))



db_settngs = DatabaseSettings()
