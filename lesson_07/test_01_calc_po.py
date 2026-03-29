import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage


def test_calculator_result():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    try:
        page = CalculatorPage(driver)
        page.open() \
            .set_delay("45") \
            .click_button("7") \
            .click_button("+") \
            .click_button("8") \
            .click_button("=")

        result = page.get_result_text()
        assert result == "15", f"Expected '15', got '{result}'"
    finally:
        driver.quit()