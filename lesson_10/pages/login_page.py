from selenium.webdriver.common.by import By
from .base_page import BasePage
from .inventory_page import InventoryPage


class LoginPage(BasePage):
    """Класс страницы авторизации."""

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def init(self, driver, url: str) -> None:
        super().init(driver, url)

    def enter_username(self, username: str) -> None:
        """
        Вводит имя пользователя.

        :param username: Логин пользователя.
        """
        element = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        element.clear()
        element.send_keys(username)

    def enter_password(self, password: str) -> None:
        """
        Вводит пароль.

        :param password: Пароль пользователя.
        """
        element = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        element.clear()
        element.send_keys(password)

    def click_login_button(self) -> InventoryPage:
        """
        Нажимает кнопку входа.

        :return: Экземпляр страницы инвентаря (InventoryPage).
        """
        button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        button.click()
        return InventoryPage(self.driver, self.url)

    def login(self, username: str, password: str) -> InventoryPage:
        """
        Выполняет полную процедуру входа.

        :param username: Логин пользователя.
        :param password: Пароль пользователя.
        :return: Экземпляр страницы инвентаря.
        """
        self.enter_username(username)
        self.enter_password(password)
        return self.click_login_button()

    def get_error_message(self) -> str:
        """
        Получает текст сообщения об ошибке.

        :return: Текст ошибки.
        """
        return self.get_text(*self.ERROR_MESSAGE)