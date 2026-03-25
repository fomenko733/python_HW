import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Конфигурация для тестов Yougile API"""

    BASE_URL = os.getenv("YOUGILE_BASE_URL", "https://yougile.com")
    API_PREFIX = "/api-v2"

    # Auth данные для получения токена
    AUTH_LOGIN = os.getenv("YOUGILE_LOGIN")
    AUTH_PASSWORD = os.getenv("YOUGILE_PASSWORD")
    COMPANY_ID = os.getenv("YOUGILE_COMPANY_ID")

    # API ключ (можно получить заранее или через фикстуру)
    API_KEY = os.getenv("YOUGILE_API_KEY")

    # Таймауты
    REQUEST_TIMEOUT = 30

    @property
    def api_url(self):
        return f"{self.BASE_URL}{self.API_PREFIX}"

    @property
    def auth_headers(self):
        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.API_KEY}"
        }
