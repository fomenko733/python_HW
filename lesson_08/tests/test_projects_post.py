import pytest
from config import Config


class TestProjectsPost:
    """Тесты метода POST /api-v2/projects"""

    def test_create_project_positive(self, projects_api):
        """Позитивный тест: создание проекта с корректными данными"""
        payload = {
            "title": f"AutoTest_{int(time.time())}",
            "users": {Config.TEST_USER_ID: "admin"}
        }
        response = projects_api.create_project(**payload)

        assert response.status_code == 201
        data = response.json()
        assert data["title"] == payload["title"]
        assert "id" in data

    def test_create_project_missing_title_negative(self, projects_api):
        """Негативный тест: создание проекта без обязательного поля title"""
        payload = {
            "users": {Config.TEST_USER_ID: "admin"}
        }
        response = projects_api.post(
            projects_api.PROJECTS_ENDPOINT,
            json=payload
        )

        assert response.status_code >= 400
        assert "error" in response.json() or response.status_code == 400