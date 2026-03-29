import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_shopping_total():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    try:
        # Login
        LoginPage(driver).open().login("standard_user", "secret_sauce")

        # Add items
        inventory = InventoryPage(driver)
        inventory.add_to_cart("Sauce Labs Backpack") \
                 .add_to_cart("Sauce Labs Bolt T-Shirt") \
                 .add_to_cart("Sauce Labs Onesie") \
                 .go_to_cart()

        # Checkout
        CartPage(driver).click_checkout()
        total = CheckoutPage(driver).fill_info("Данил", "Тестеров", "123456").get_total_text()

        assert total == "Total: $58.29", f"Expected 'Total: $58.29', got '{total}'"
    finally:
        driver.quit()