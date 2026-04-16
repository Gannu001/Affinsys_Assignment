class HomePage:
    def __init__(self, page):
        self.page = page

    def navigate_to_home(self):
        self.page.goto("https://sauce-demo.myshopify.com/")

    def select_product(self, product_name):
        product = self.page.get_by_text(product_name)
        name = product.inner_text().strip()
        product.click()
        return name