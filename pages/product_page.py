class ProductDetailsPage:
    def __init__(self, page):
        self.page = page
        self.add_to_cart_button = page.locator("#add")

    def add_product_to_cart_multiple_times(self, count=2):
        for i in range(count):
            self.add_to_cart_button.click()
            print(f"Clicked Add to Cart {i+1} time(s)")
            self.page.wait_for_timeout(2000)

    def refresh_page(self):
        self.page.reload()