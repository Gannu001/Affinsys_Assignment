from playwright.sync_api import sync_playwright  # type: ignore
from pages.home_page import HomePage
from pages.product_page import ProductDetailsPage
from pages.cart_page import ShoppingCartPage


def test_add_product_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            viewport={"width": 1260, "height": 800}
        )
        page = context.new_page()

        home = HomePage(page)
        product_page = ProductDetailsPage(page)
        cart = ShoppingCartPage(page)

        # Open site
        home.navigate_to_home()

        # Select product
        product_name = home.select_product("Noir Jacket")

        # Add product twice
        product_page.add_product_to_cart_multiple_times(2)

        # Refresh page
        product_page.refresh_page()

        # Open cart
        cart.open_cart_page()


        # Checkout visibility
        cart.assert_checkout_button_is_visible()

        # Proceed to checkout
        cart.proceed_to_checkout()

        # Validations
        cart.assert_product_is_present_in_cart(product_name)
        cart.assert_total_price_is_correct()
        cart.assert_product_quantity_is_correct()

        context.close()
        browser.close()