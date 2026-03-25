import pytest
import requests
from config import Config


@pytest.fixture(scope="session")
def api_session():
    """Сессия requests с предустановленными заголовками"""
    session = requests.Session()
    config = Config()
    session.headers.update(config.auth_headers)
    yield session
    session.close()


@pytest.fixture(autouse=True)
def skip_if_no_auth():
    """Пропускать тесты, если не настроены креды"""
    config = Config()
    if not all([config.AUTH_LOGIN, config.AUTH_PASSWORD, config.COMPANY_ID, config.API_KEY]):
        pytest.skip(
            "Требуется настройка окружения: "
            "YOUGILE_LOGIN, YOUGILE_PASSWORD, YOUGILE_COMPANY_ID, YOUGILE_API_KEY"
        )
