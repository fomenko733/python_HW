import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BASE_URL = os.getenv("YOUGILE_BASE_URL", "https://yougile.com")
    API_TOKEN = os.getenv("YOUGILE_API_TOKEN")
    COMPANY_ID = os.getenv("YOUGILE_COMPANY_ID")
    TEST_USER_ID = os.getenv("YOUGILE_TEST_USER_ID")  # ID пользователя для назначения роли

    @classmethod
    def get_headers(cls):
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {cls.API_TOKEN}"
        }

    @classmethod
    def validate(cls):
        """Проверка наличия обязательных переменных"""
        required = ["API_TOKEN", "COMPANY_ID", "TEST_USER_ID"]
        missing = [var for var in required if not getattr(cls, var)]
        if missing:
            raise ValueError(f"Не заданы переменные окружения: {missing}")