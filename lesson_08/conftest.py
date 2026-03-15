import pytest
import time
from config import Config
from pages.projects_page import ProjectsPage


@pytest.fixture(scope="session")
def config():
    """Фикстура конфигурации"""
    Config.validate()
    return Config


@pytest.fixture(scope="function")
def projects_api():
    """Фикстура PageObject для проектов"""
    return ProjectsPage()


@pytest.fixture(scope="function")
def created_project(projects_api):
    """Фикстура: создаёт проект перед тестом и удаляет после"""
    project_data = {
        "title": f"TestProject_{int(time.time())}",
        "users": {Config.TEST_USER_ID: "admin"}
    }
    response = projects_api.create_project(**project_data)
    assert response.status_code == 201, f"Не удалось создать проект: {response.text}"
    project_id = response.json()["id"]

    yield project_id  # Передаём ID в тест

    # Teardown: удаляем проект после теста
    projects_api.delete_project(project_id)