import re
from playwright.sync_api import expect  # type: ignore


class ShoppingCartPage:
    def __init__(self, page):
        self.page = page

    def open_cart_page(self):
        self.page.get_by_role("link", name="My Cart").click()

    def assert_checkout_button_is_visible(self):
        checkout_button = self.page.get_by_role("button", name="Check Out")
        expect(checkout_button).to_be_visible()

    def proceed_to_checkout(self):
        self.page.get_by_role("button", name="Check Out").click()
        self.page.wait_for_load_state("networkidle")

    def assert_product_is_present_in_cart(self, product_name):
        product = self.page.get_by_role(
            "link",
            name=re.compile(f"{product_name}.*")
        )
        expect(product).to_be_visible()
        print("Correct item added to cart")

    def assert_total_price_is_correct(self):
        total_price = self.page.get_by_role("heading", name="Total £120.00")
        expect(total_price).to_be_visible()
        print("Total price is correct: £120.00")

    def assert_product_quantity_is_correct(self):
        quantity_input = self.page.locator("input[name='updates[]']:visible")
        expect(quantity_input).to_have_value("2")
        print("Quantity is correct: 2")