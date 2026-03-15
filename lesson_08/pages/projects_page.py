from pages.base_page import BasePage


class ProjectsPage(BasePage):
    """PageObject для работы с эндпоинтами проектов"""

    PROJECTS_ENDPOINT = "/api-v2/projects"

    def create_project(self, title: str, users: dict):
        """POST /api-v2/projects — создание проекта"""
        payload = {
            "title": title,
            "users": users
        }
        return self.post(self.PROJECTS_ENDPOINT, json=payload)

    def get_project(self, project_id: str):
        """GET /api-v2/projects/{id} — получение проекта"""
        return self.get(f"{self.PROJECTS_ENDPOINT}/{project_id}")

    def update_project(self, project_id: str, **update_data):
        """PUT /api-v2/projects/{id} — обновление проекта"""
        return self.put(f"{self.PROJECTS_ENDPOINT}/{project_id}", json=update_data)

    def delete_project(self, project_id: str):
        """DELETE /api-v2/projects/{id} — удаление проекта (для очистки)"""
        return self.delete(f"{self.PROJECTS_ENDPOINT}/{project_id}")