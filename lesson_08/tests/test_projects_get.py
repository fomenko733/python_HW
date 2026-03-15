class TestProjectsGet:
    """Тесты метода GET /api-v2/projects/{id}"""

    def test_get_existing_project_positive(self, projects_api, created_project):
        """Позитивный тест: получение существующего проекта"""
        response = projects_api.get_project(created_project)

        assert response.status_code == 200
        data = response.json()
        assert data["id"] == created_project
        assert "title" in data

    def test_get_nonexistent_project_negative(self, projects_api):
        """Негативный тест: получение несуществующего проекта"""
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = projects_api.get_project(fake_id)

        assert response.status_code >= 400