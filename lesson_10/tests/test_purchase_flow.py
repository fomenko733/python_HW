import allure
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Покупка товаров")
@allure.severity(allure.severity_level.CRITICAL)
class TestPurchaseFlow:

    @allure.title("Полный цикл покупки: авторизация, добавление товаров, оформление")
    @allure.description(
        "Тест проверяет полный сценарий покупки: вход как standard_user, "
        "добавление 3 товаров в корзину, оформление заказа и проверка итоговой суммы $58.29"
    )
    @allure.story("Позитивный сценарий покупки")
    def test_complete_purchase_flow(self, login_page: LoginPage) -> None:
        """
        Тест полного цикла покупки в интернет-магазине.
        Проверяет корректность расчёта итоговой стоимости.
        """
        with allure.step("Открыть страницу авторизации"):
            login_page.open()

        with allure.step("Авторизоваться как standard_user"):
            inventory_page: InventoryPage = login_page.login(
                username="standard_user",
                password="secret_sauce"
            )

        with allure.step("Добавить Sauce Labs Backpack в корзину"):
            inventory_page.add_backpack_to_cart()

        with allure.step("Добавить Sauce Labs Bolt T-Shirt в корзину"):
            inventory_page.add_bolt_tshirt_to_cart()

        with allure.step("Добавить Sauce Labs Onesie в корзину"):
            inventory_page.add_onesie_to_cart()

        with allure.step("Проверить, что в корзине 3 товара"):
            cart_count = inventory_page.get_cart_items_count()
            assert cart_count == "3", f"Ожидалось 3 товара, найдено: {cart_count}"

        with allure.step("Перейти в корзину"):
            cart_page: CartPage = inventory_page.go_to_cart()

        with allure.step("Нажать кнопку Checkout"):
            checkout_page: CheckoutPage = cart_page.click_checkout()

        with allure.step("Заполнить форму данными покупателя"):
            checkout_page.fill_checkout_info(
                first_name="Данил",
                last_name="Тестов",
                postal_code="614000"
            )

        with allure.step("Нажать Continue для перехода к итогу"):
            checkout_page.click_continue()

        with allure.step("Получить итоговую стоимость заказа"):
            total_price: str = checkout_page.get_total_price()

        with allure.step("Проверить, что итоговая сумма равна $58.29"):
            assert total_price == "$58.29", f"Ожидалась сумма $58.29, получено: {total_price}"

        with allure.step("Завершить оформление заказа"):
            checkout_page.click_finish()