from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
try:
    driver.get("http://uitestingplayground.com/textinput")

    # Вводим текст в поле
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")

    # Нажимаем на синюю кнопку
    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    # Получаем новый текст кнопки
    updated_text = button.text
    print(updated_text)  # Ожидаем: "SkyPro"
finally:
    driver.quit()