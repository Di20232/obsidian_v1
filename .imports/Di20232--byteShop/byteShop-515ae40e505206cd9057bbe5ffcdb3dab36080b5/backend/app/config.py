from pydantic_settings import BaseSettings, SettingsConfigDict

# Valores de exemplo já usados neste projeto (documentação, .env.example antigo).
# Se o SECRET_KEY atual for igual a um destes, o servidor recusa iniciar: uma
# chave conhecida/previsível permite forjar tokens JWT válidos para qualquer
# usuário (incluindo admins) sem precisar de senha.
_KNOWN_WEAK_SECRETS = {
    "dev-secret-key",
    "troque-esta-chave-por-uma-string-aleatoria-segura",
    "changeme",
    "secret",
}


class Settings(BaseSettings):
    database_url: str = "sqlite:///./ecommerce.db"
    secret_key: str = "dev-secret-key"
    access_token_expire_minutes: int = 120
    cors_origins: str = "http://localhost:5173"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @property
    def cors_origins_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",")]

    def validate_secret_key(self) -> None:
        if self.secret_key in _KNOWN_WEAK_SECRETS or len(self.secret_key) < 32:
            raise RuntimeError(
                "SECRET_KEY inválido ou fraco demais. Gere um valor aleatório forte "
                "(ex: python -c \"import secrets; print(secrets.token_hex(32))\") "
                "e defina-o em backend/.env antes de iniciar o servidor."
            )


settings = Settings()
settings.validate_secret_key()
