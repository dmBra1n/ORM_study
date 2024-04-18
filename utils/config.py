from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseDBSettings(BaseSettings):
    """
    Base class for database settings configuration.
    Contains common database connection parameters.
    """
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_NAME: str
    DB_PASS: str

    @property
    def connection_url_template(self) -> str:
        """
        Returns the template for database connection URL.
        This property can be used to construct the full connection URL.
        """
        return (
            f"{self.DB_USER}:{self.DB_PASS}@"
            f"{self.DB_HOST}:{self.DB_PORT}/"
            f"{self.DB_NAME}"
        )


class PostgreSQLSettings(BaseDBSettings):
    """
    Class for PostgreSQL database settings configuration.
    Provides properties to generate PostgreSQL connection URL.
    """

    @property
    def psycopg_connection_url(self) -> str:
        """
        Generates psycopg PostgreSQL connection URL.
        """
        return f"postgresql+psycopg://{self.connection_url_template}"

    @property
    def asyncpg_connection_url(self) -> str:
        """
        Generates asyncpg PostgreSQL connection URL.
        """
        return f"postgresql+asyncpg://{self.connection_url_template}"

    model_config = SettingsConfigDict(env_file="../.env")


settings = PostgreSQLSettings()
