from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
try:
    driver.get("http://uitestingplayground.com/ajax")

    # Нажимаем на синюю кнопку
    button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()

    # Ждём появления зелёной плашки с текстом
    green_badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
    )

    print(green_badge.text)  # Ожидаем: "Data loaded with AJAX get request."
finally:
    driver.quit()