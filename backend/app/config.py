import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    chat_api_key: str
    llm_model: str


def get_settings() -> Settings:
    return Settings(
        chat_api_key=os.environ["CHAT_API_KEY"],
        llm_model=os.environ.get("LLM_MODEL", "openai/gpt-oss-20b")
    )

Settings = get_settings()