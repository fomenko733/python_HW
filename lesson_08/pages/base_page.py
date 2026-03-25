import requests
from typing import Optional, Dict
from config import Config


class BasePage:
    """Базовый класс для PageObject паттерна"""

    def __init__(self, session: Optional[requests.Session] = None):
        self.config = Config()
        self.session = session or requests.Session()
        self.session.headers.update(self.config.auth_headers)

    def _make_request(
            self,
            method: str,
            endpoint: str,
            json_data: Optional[Dict] = None,
            params: Optional[Dict] = None
    ) -> requests.Response:
        """Универсальный метод для выполнения запросов"""
        url = f"{self.config.api_url}{endpoint}"

        response = self.session.request(
            method=method,
            url=url,
            json=json_data,
            params=params,
            timeout=self.config.REQUEST_TIMEOUT
        )
        return response

    def get(self, endpoint: str, params: Optional[Dict] = None) -> requests.Response:
        return self._make_request("GET", endpoint, params=params)

    def post(self, endpoint: str, json_data: Dict) -> requests.Response:
        return self._make_request("POST", endpoint, json_data=json_data)

    def put(self, endpoint: str, json_data: Dict) -> requests.Response:
        return self._make_request("PUT", endpoint, json_data=json_data)

    def delete(self, endpoint: str) -> requests.Response:
        return self._make_request("DELETE", endpoint)
