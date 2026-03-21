import requests
from config import Config


class BasePage:
    """Базовый класс для всех страниц API"""

    def init(self):
        self.base_url = Config.BASE_URL
        self.headers = Config.get_headers()
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def _make_request(self, method: str, endpoint: str, **kwargs):
        """Универсальный метод для выполнения запросов"""
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, **kwargs)
        return response

    def get(self, endpoint: str, **kwargs):
        return self._make_request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs):
        return self._make_request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs):
        return self._make_request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self._make_request("DELETE", endpoint, **kwargs)
