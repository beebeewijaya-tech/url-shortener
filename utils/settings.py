from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    airtable_key: str
    airtable_base_id: str
    spaces_access: str
    spaces_secret: str
    spaces_bucket_url: str
    spaces_bucket_name: str
    spaces_region: str
    host: str = "shortswift.cloud"

    db_host: str
    db_user: str
    db_pass: str
    db_port: str
    db_name: str

    jwt_secret: str
    model_config = SettingsConfigDict(env_file=".env")
