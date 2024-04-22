import pytest
from configuration import Settings

def test_settings():
    settings = Settings()
    assert settings.database_url is not None
    assert settings.jwt_secret_key is not None
    assert settings.jwt_algorithm is not None
    assert settings.jwt_expiration_minutes is not None

