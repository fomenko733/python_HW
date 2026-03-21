from selenium.webdriver.common.by import By
from .base_page import BasePage
from .cart_page import CartPage


class InventoryPage(BasePage):
    """Класс страницы с товарами (инвентарь)."""

    # Локаторы кнопок "Добавить в корзину" для конкретных товаров
    BACKPACK_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    BOLT_TSHIRT_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")

    CART_BUTTON = (By.CSS_SELECTOR, "a.shopping_cart_link")
    CART_BADGE = (By.CSS_SELECTOR, "span.shopping_cart_badge")

    def init(self, driver, url: str) -> None:
        super().init(driver, url)

    def add_backpack_to_cart(self) -> None:
        """Добавляет товар 'Sauce Labs Backpack' в корзину."""
        button = self.wait.until(EC.element_to_be_clickable(self.BACKPACK_ADD_BUTTON))
        button.click()

    def add_bolt_tshirt_to_cart(self) -> None:
        """Добавляет товар 'Sauce Labs Bolt T-Shirt' в корзину."""
        button = self.wait.until(EC.element_to_be_clickable(self.BOLT_TSHIRT_ADD_BUTTON))
        button.click()

    def add_onesie_to_cart(self) -> None:
        """Добавляет товар 'Sauce Labs Onesie' в корзину."""
        button = self.wait.until(EC.element_to_be_clickable(self.ONESIE_ADD_BUTTON))
        button.click()

    def get_cart_items_count(self) -> str:
        """
        Получает количество товаров в корзине (текст бейджа).

        :return: Количество товаров в виде строки.
        """
        badge = self.wait.until(EC.visibility_of_element_located(self.CART_BADGE))
        return badge.text

    def go_to_cart(self) -> CartPage:
        """
        Переходит на страницу корзины.

        :return: Экземпляр страницы корзины (CartPage).
        """
        cart_button = self.wait.until(EC.element_to_be_clickable(self.CART_BUTTON))
        cart_button.click()
        return CartPage(self.driver, self.url)