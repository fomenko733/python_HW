from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from typing import Optional


class BasePage:
    """Базовый класс для всех страниц приложения."""

    def init(self, driver: WebDriver, url: str) -> None:
        """
        Инициализация базовой страницы.

        :param driver: Экземпляр WebDriver.
        :param url: URL-адрес страницы.
        """
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> None:
        """Открывает страницу в браузере."""
        self.driver.get(self.url)

    def get_current_url(self) -> str:
        """
        Получает текущий URL страницы.

        :return: Текущий URL в виде строки.
        """
        return self.driver.current_url

    def find_element(self, by: By, value: str) -> None:
        """
        Находит элемент на странице.

        :param by: Стратегия поиска (By.ID, By.CSS_SELECTOR и т.д.).
        :param value: Значение локатора.
        :return: Найденный WebElement.
        """
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def get_text(self, by: By, value: str) -> str:
        """
        Получает текст элемента.

        :param by: Стратегия поиска элемента.
        :param value: Значение локатора.
        :return: Текст содержимого элемента.
        """
        element = self.find_element(by, value)
        return element.text