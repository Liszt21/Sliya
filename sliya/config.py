import secrets
from typing import List, Union
from pydantic import BaseSettings, AnyHttpUrl, validator
from dotenv import load_dotenv

load_dotenv(".env")


class Settings(BaseSettings):
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str = "Sliya"
    SERVER_HOST: str = "localhost"
    SERVER_PORT: int = 9715
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:3000",
        "http://localhost:5000",
        "https://liszt.space",
        "https://eliya.liszt.space"
    ]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls,
                              v: Union[str, List[str]]) -> Union[List[str],
                                                                 str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)


settings = Settings()
