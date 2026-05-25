from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')
    openai_api_key: str = ''
    github_token: str = ''
    database_url: str = 'sqlite+aiosqlite:///./reposage.db'
    chroma_path: str = '.reposage_chroma'


settings = Settings()
