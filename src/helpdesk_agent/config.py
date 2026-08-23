import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    api_url: str = os.getenv(
        "AISTUDIO_API_URL",
        "https://llm.api.cloud.yandex.net/foundationModels/v1/completion",
    )
    api_key: str = os.getenv("AISTUDIO_API_KEY", "")
    model_uri: str = os.getenv("AISTUDIO_MODEL_URI", "")
    ydb_endpoint: str = os.getenv("YDB_ENDPOINT", "")
    ydb_database: str = os.getenv("YDB_DATABASE", "")
