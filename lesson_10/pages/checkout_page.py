from selenium.webdriver.common.by import By
from .base_page import BasePage


class CheckoutPage(BasePage):
    """Класс страницы оформления заказа."""

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    TOTAL_LABEL = (By.CSS_SELECTOR, "div.total_value_label")

    def init(self, driver, url: str) -> None:
        super().init(driver, url)

    def enter_first_name(self, first_name: str) -> None:
        """
        Вводит имя.

        :param first_name: Имя покупателя.
        """
        element = self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_INPUT))
        element.clear()
        element.send_keys(first_name)

    def enter_last_name(self, last_name: str) -> None:
        """
        Вводит фамилию.

        :param last_name: Фамилия покупателя.
        """
        element = self.wait.until(EC.visibility_of_element_located(self.LAST_NAME_INPUT))
        element.clear()
        element.send_keys(last_name)

    def enter_postal_code(self, postal_code: str) -> None:
        """
        Вводит почтовый индекс.

        :param postal_code: Почтовый индекс.
        """
        element = self.wait.until(EC.visibility_of_element_located(self.POSTAL_CODE_INPUT))
        element.clear()
        element.send_keys(postal_code)

    def click_continue(self) -> None:
        """Нажимает кнопку продолжения оформления."""
        button = self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON))
        button.click()

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму данными покупателя.

        :param first_name: Имя.
        :param last_name: Фамилия.
        :param postal_code: Почтовый индекс.
        """
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

    def get_total_price(self) -> str:
        """
        Получает итоговую стоимость заказа.

        :return: Строка с итоговой суммой (например, '$58.29').
        """
        return self.get_text(*self.TOTAL_LABEL)

    def click_finish(self) -> None:
        """Завершает оформление заказа."""
        button = self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON))
        button.click()