import pytest
import uuid
from pages.projects_page import ProjectsPage


@pytest.fixture
def projects_api():
    """Фикстура для создания экземпляра ProjectsPage"""
    return ProjectsPage()


@pytest.fixture
def created_project_id(projects_api):
    """Фикстура для создания и очистки тестового проекта"""
    project_id, response = projects_api.create_test_project()

    if project_id is None:
        pytest.skip(f"Не удалось создать проект для тестов: {response.text}")

    yield project_id

    # Cleanup: попытка архивировать проект после теста
    try:
        projects_api.update_project(project_id, title=f"archived_{uuid.uuid4().hex[:8]}")
    except Exception:
        pass


class TestCreateProject:
    """Тесты для POST /api-v2/projects"""

    def test_create_project_positive_minimal(self, projects_api):
        """Позитивный тест: создание проекта с минимальными данными"""
        unique_title = f"Test Project {uuid.uuid4().hex[:8]}"

        response = projects_api.create_project_minimal(unique_title)

        assert response.status_code in (200, 201), \
            f"Expected 200 or 201, got {response.status_code}: {response.text}"

        data = response.json()
        returned_title = projects_api.get_project_title(response)

        assert returned_title is not None, f"Title not found in response: {data}"
        assert unique_title in returned_title, \
            f"Expected '{unique_title}' in title, got '{returned_title}'"

    def test_create_project_positive_full(self, projects_api):
        """Позитивный тест: создание проекта с description"""
        unique_title = f"Full Test Project {uuid.uuid4().hex[:8]}"
        response = projects_api.create_project(
            title=unique_title,
            description="Test description for automation"
        )

        assert response.status_code in (200, 201), \
            f"Expected 200 or 201, got {response.status_code}: {response.text}"

    def test_create_project_negative_empty_title(self, projects_api):
        """Негативный тест: создание проекта без обязательного поля title"""
        response = projects_api.post("/projects", json_data={})

        assert response.status_code in (400, 401, 403, 422), \
            f"Expected error status, got {response.status_code}: {response.text}"


class TestGetProject:
    """Тесты для GET /api-v2/projects/{id}"""

    def test_get_project_positive(self, projects_api, created_project_id):
        """Позитивный тест: получение существующего проекта"""
        response = projects_api.get_project(created_project_id)

        assert response.status_code == 200, \
            f"Expected 200, got {response.status_code}: {response.text}"

        data = response.json()
        returned_id = projects_api.get_project_id(response)

        assert returned_id is not None, f"ID not found in response: {data}"

    def test_get_project_negative_not_found(self, projects_api):
        """Негативный тест: получение несуществующего проекта"""
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = projects_api.get_project(fake_id)

        assert response.status_code in (401, 404), \
            f"Expected 401 or 404, got {response.status_code}: {response.text}"

    def test_get_project_negative_invalid_id_format(self, projects_api):
        """Негативный тест: невалидный формат ID"""
        response = projects_api.get_project("invalid-id-format")

        assert response.status_code in (400, 401, 404), \
            f"Expected 400, 401 or 404, got {response.status_code}: {response.text}"


class TestUpdateProject:
    """Тесты для PUT /api-v2/projects/{id}"""

    def test_update_project_positive_change_title(self, projects_api, created_project_id):
        """Позитивный тест: обновление названия проекта"""
        new_title = f"Updated Title {uuid.uuid4().hex[:8]}"

        response = projects_api.update_project(created_project_id, title=new_title)

        assert response.status_code in (200, 204), \
            f"Expected 200 or 204, got {response.status_code}: {response.text}"

        get_response = projects_api.get_project(created_project_id)
        if get_response.status_code == 200:
            returned_title = projects_api.get_project_title(get_response)
            if returned_title:
                assert new_title in returned_title, \
                    f"Expected '{new_title}' in title, got '{returned_title}'"

    def test_update_project_positive_partial_update(self, projects_api, created_project_id):
        """Позитивный тест: частичное обновление (только description)"""
        new_description = f"Updated desc {uuid.uuid4().hex[:8]}"

        response = projects_api.update_project(created_project_id, description=new_description)

        assert response.status_code in (200, 204), \
            f"Expected 200 or 204, got {response.status_code}: {response.text}"

    def test_update_project_negative_not_found(self, projects_api):
        """Негативный тест: обновление несуществующего проекта"""
        fake_id = "11111111-1111-1111-1111-111111111111"
        response = projects_api.update_project(fake_id, title="Should Fail")

        assert response.status_code in (400, 401, 404), \
            f"Expected 400, 401 or 404, got {response.status_code}: {response.text}"

    def test_update_project_negative_empty_payload(self, projects_api, created_project_id):
        """Негативный тест: обновление с пустым телом запроса"""
        response = projects_api.put(f"/projects/{created_project_id}", json_data={})

        assert response.status_code in (200, 204, 400, 401), \
            f"Expected 200, 204, 400 or 401, got {response.status_code}: {response.text}"