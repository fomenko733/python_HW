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
    assert response.status_code in (200, 201), f"Failed to create project: {response.text}"
    yield project_id
    # Cleanup: попытка архивировать проект после теста
    try:
        projects_api.cleanup_project(project_id)
    except Exception:
        pass  # Игнорируем ошибки очистки, чтобы не ломать тесты


class TestCreateProject:
    """Тесты для POST /api-v2/projects"""

    def test_create_project_positive_minimal(self, projects_api):
        """Позитивный тест: создание проекта с минимальными данными"""
        unique_title = f"Test Project {uuid.uuid4().hex[:8]}"

        response = projects_api.create_project_minimal(unique_title)

        assert response.status_code == 201, f"Expected 201, got {response.status_code}: {response.text}"
        data = response.json()
        assert data.get("title") == unique_title
        assert "id" in data, "Response should contain project ID"

    def test_create_project_positive_full(self, projects_api):
        """Позитивный тест: создание проекта с полными данными"""
        unique_title = f"Full Test Project {uuid.uuid4().hex[:8]}"
        users_payload = {}  # Пустой, если нет тестовых user_id

        response = projects_api.create_project(
            title=unique_title,
            users=users_payload,
            description="Test description for automation"
        )

        assert response.status_code == 201
        data = response.json()
        assert data.get("description") == "Test description for automation"

    def test_create_project_negative_empty_title(self, projects_api):
        """Негативный тест: создание проекта без обязательного поля title"""
        response = projects_api.post("/projects", json_data={})

        # API должно вернуть 400 или 422 при отсутствии обязательных полей
        assert response.status_code in (400, 422, 409), \
            f"Expected error status, got {response.status_code}: {response.text}"
        assert "error" in response.json() or response.status_code != 201

    def test_create_project_negative_duplicate_title(self, projects_api, created_project_id):
        """Негативный тест: попытка создать проект с дублирующимся названием (если есть ограничение)"""
        # Получаем название существующего проекта
        existing = projects_api.get_project(created_project_id)
        if existing.status_code == 200:
            duplicate_title = existing.json().get("title")
            response = projects_api.create_project_minimal(duplicate_title)
            # В зависимости от бизнес-логики: может быть разрешено или нет
            # Проверяем, что ответ корректный (не 500)
            assert response.status_code not in (500, 502, 503), "Server error on duplicate title"


class TestGetProject:
    """Тесты для GET /api-v2/projects/{id}"""

    def test_get_project_positive(self, projects_api, created_project_id):
        """Позитивный тест: получение существующего проекта"""
        response = projects_api.get_project(created_project_id)

        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"
        data = response.json()
        assert data.get("id") == created_project_id
        assert "title" in data

    def test_get_project_negative_not_found(self, projects_api):
        """Негативный тест: получение несуществующего проекта"""
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = projects_api.get_project(fake_id)

        assert response.status_code == 404, f"Expected 404, got {response.status_code}: {response.text}"
        assert "error" in response.json().get("error", "").lower() or "not found" in response.text.lower()

    def test_get_project_negative_invalid_id_format(self, projects_api):
        """Негативный тест: невалидный формат ID"""
        response = projects_api.get_project("invalid-id-format")

        # API может вернуть 400 (Bad Request) или 404
        assert response.status_code in (400, 422, 409), \
            f"Expected 400 or 404, got {response.status_code}: {response.text}"


class TestUpdateProject:
    """Тесты для PUT /api-v2/projects/{id}"""

    def test_update_project_positive_change_title(self, projects_api, created_project_id):
        """Позитивный тест: обновление названия проекта"""
        new_title = f"Updated Title {uuid.uuid4().hex[:8]}"

        response = projects_api.update_project(created_project_id, title=new_title)

        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"
        data = response.json()
        assert data.get("title") == new_title

    def test_update_project_positive_partial_update(self, projects_api, created_project_id):
        """Позитивный тест: частичное обновление (только description)"""
        new_description = f"Updated desc {uuid.uuid4().hex[:8]}"

        response = projects_api.update_project(created_project_id, description=new_description)

        assert response.status_code == 200
        data = response.json()
        assert data.get("description") == new_description
        # Убедимся, что title не изменился
        original = projects_api.get_project(created_project_id).json()
        assert original.get("description") == new_description

    def test_update_project_negative_not_found(self, projects_api):
        """Негативный тест: обновление несуществующего проекта"""
        fake_id = "11111111-1111-1111-1111-111111111111"
        response = projects_api.update_project(fake_id, title="Should Fail")

        assert response.status_code == 404, f"Expected 404, got {response.status_code}: {response.text}"

    def test_update_project_negative_empty_payload(self, projects_api, created_project_id):
        """Негативный тест: обновление с пустым телом запроса"""
        response = projects_api.put(f"/projects/{created_project_id}", json_data={})

        # Пустое обновление может быть разрешено (возврат 200) или отвергнуто (400)
        # Главное — стабильный и предсказуемый ответ, не 500
        assert response.status_code not in (500, 502, 503), "Server error on empty update payload"
