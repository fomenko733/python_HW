from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def init(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        return self

    def set_delay(self, value: str):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(value)
        return self

    def click_button(self, text: str):
        button = self.driver.find_element(By.XPATH, f"//span[text()='{text}']")
        button.click()
        return self

    def get_result_text(self) -> str:
        screen = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "screen")))
        return screen.text