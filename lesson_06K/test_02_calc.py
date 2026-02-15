# test_02_calc.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_calculator():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 50)  # чуть больше 45 сек

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Устанавливаем задержку 45 сек
        delay_input = driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # Нажимаем кнопки: 7 + 8 =
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        # Ждём, пока результат станет "15"
        result_element = wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )

        screen_text = driver.find_element(By.CLASS_NAME, "screen").text
        assert screen_text == "15", f"Expected '15', got '{screen_text}'"

    finally:
        driver.quit()