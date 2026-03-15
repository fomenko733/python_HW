import time


class TestProjectsPut:
    """Тесты метода PUT /api-v2/projects/{id}"""

    def test_update_project_title_positive(self, projects_api, created_project):
        """Позитивный тест: обновление названия проекта"""
        new_title = f"Updated_{int(time.time())}"
        response = projects_api.update_project(created_project, title=new_title)

        assert response.status_code == 200
        data = response.json()
        assert data["title"] == new_title

    def test_update_nonexistent_project_negative(self, projects_api):
        """Негативный тест: обновление несуществующего проекта"""
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = projects_api.update_project(fake_id, title="New Title")

        assert response.status_code >= 400