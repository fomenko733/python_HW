from selenium.webdriver.common.by import By
from .base_page import BasePage
from .checkout_page import CheckoutPage


class CartPage(BasePage):
    """Класс страницы корзины."""

    CHECKOUT_BUTTON = (By.ID, "checkout")
    ITEM_IN_CART = (By.CSS_SELECTOR, "div.cart_item")

    def init(self, driver, url: str) -> None:
        super().init(driver, url)

    def get_cart_items(self) -> list:
        """
        Получает список товаров в корзине.

        :return: Список WebElement'ов товаров.
        """
        return self.driver.find_elements(*self.ITEM_IN_CART)

    def click_checkout(self) -> CheckoutPage:
        """
        Нажимает кнопку оформления заказа.

        :return: Экземпляр страницы оформления заказа (CheckoutPage).
        """
        button = self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON))
        button.click()
        return CheckoutPage(self.driver, self.url)