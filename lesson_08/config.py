# config.py
import os
from dotenv import load_dotenv

current_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(current_dir, '.env')
load_dotenv(env_path)


class Config:
    """Конфигурация для тестов Yougile API"""

    # ✅ Убрал /api-v2 из BASE_URL (он добавится через API_PREFIX)
    BASE_URL = os.getenv("YOUGILE_BASE_URL", "https://yougile.com")
    API_PREFIX = "/api-v2"

    # Auth данные
    AUTH_LOGIN = os.getenv("YOUGILE_LOGIN")
    AUTH_PASSWORD = os.getenv("YOUGILE_PASSWORD")
    COMPANY_ID = os.getenv("YOUGILE_COMPANY_ID")
    API_KEY = os.getenv("YOUGILE_API_KEY")

    # Таймауты
    REQUEST_TIMEOUT = 30

    @property
    def api_url(self):
        # ✅ Защита от двойных слешей: https://...com//api-v2
        base = self.BASE_URL.rstrip('/')
        prefix = self.API_PREFIX.lstrip('/')
        return f"{base}/{prefix}"

    @property
    def auth_headers(self):
        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.API_KEY}"
        }