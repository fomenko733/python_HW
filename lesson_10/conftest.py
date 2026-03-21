import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def browser() -> webdriver.Firefox:
    """
    Фикстура для инициализации браузера Firefox.

    :yield: Экземпляр WebDriver (Firefox).
    """
    options = Options()
    # options.headless = True  # Раскомментируйте для headless-режима
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login_page(browser: webdriver.Firefox) -> LoginPage:
    """
    Фикстура для создания объекта страницы входа.

    :param browser: Экземпляр WebDriver.
    :return: Объект LoginPage.
    """
    return LoginPage(browser, url="https://www.saucedemo.com/")