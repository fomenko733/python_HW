# test_03_shop.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def test_shopping_cart_total():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.saucedemo.com/")

        # Авторизация
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Добавление товаров
        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]

        for item_name in items_to_add:
            add_button = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button")
                )
            )
            add_button.click()

        # Переход в корзину
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Checkout
        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        # Заполнение данных
        driver.find_element(By.ID, "first-name").send_keys("Данил")
        driver.find_element(By.ID, "last-name").send_keys("Фамилия")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        driver.find_element(By.ID, "continue").click()

        # Получение итоговой суммы
        total_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))
        total_text = total_element.text  # Пример: "Total: $58.29"

        assert total_text == "Total: $58.29", f"Expected 'Total: $58.29', got '{total_text}'"

    finally:
        driver.quit()