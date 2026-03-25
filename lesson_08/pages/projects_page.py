from typing import Dict, Optional
from requests import Response
from pages.base_page import BasePage


class ProjectsPage(BasePage):
    """PageObject для работы с эндпоинтами проектов"""

    ENDPOINT = "/projects"

    # === POST /api-v2/projects ===

    def create_project(
            self,
            title: str,
            users: Optional[Dict[str, str]] = None,
            description: Optional[str] = None
    ) -> Response:
        """
        Создать новый проект

        :param title: Название проекта (обязательное поле)
        :param users: Словарь {user_id: role} для добавления участников
        :param description: Описание проекта
        :return: requests.Response
        """
        payload = {"title": title}
        if users:
            payload["users"] = users
        if description:
            payload["description"] = description

        return self.post(self.ENDPOINT, json_data=payload)

    def create_project_minimal(self, title: str) -> Response:
        """Создать проект с минимальными данными (только обязательные поля)"""
        return self.post(self.ENDPOINT, json_data={"title": title})

    # === GET /api-v2/projects/{id} ===

    def get_project(self, project_id: str) -> Response:
        """Получить информацию о проекте по ID"""
        return self.get(f"{self.ENDPOINT}/{project_id}")

    # === PUT /api-v2/projects/{id} ===

    def update_project(
            self,
            project_id: str,
            title: Optional[str] = None,
            description: Optional[str] = None,
            **kwargs
    ) -> Response:
        """
        Обновить проект

        :param project_id: ID проекта
        :param title: Новое название (опционально)
        :param description: Новое описание (опционально)
        :param kwargs: Дополнительные поля для обновления
        :return: requests.Response
        """
        payload = {k: v for k, v in kwargs.items() if v is not None}
        if title:
            payload["title"] = title
        if description:
            payload["description"] = description

        return self.put(f"{self.ENDPOINT}/{project_id}", json_data=payload)

    # === Вспомогательные методы для тестов ===

    def create_test_project(self, prefix: str = "test_") -> tuple[str, Response]:
        """
        Создать тестовый проект и вернуть его ID и ответ

        :return: tuple(project_id, response)
        """
        import uuid
        unique_title = f"{prefix}{uuid.uuid4().hex[:8]}"
        response = self.create_project_minimal(unique_title)

        if response.status_code in (200, 201):
            project_id = response.json().get("id")
            return project_id, response
        return None, response

    def cleanup_project(self, project_id: str) -> Response:
        """
        Удалить проект (если эндпоинт доступен) или пометить как неактивный.
        Примечание: DELETE /projects/{id} может быть не реализован в API v2,
        поэтому этот метод может требовать адаптации под реальное API.
        """
        # Если DELETE не поддерживается, можно обновить проект с флагом archived
        return self.update_project(project_id, archived=True)
