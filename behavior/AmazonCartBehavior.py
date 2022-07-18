from page.AmazonCartPage import AmazonCartPage


class AmazonCartBehavior(AmazonCartPage):

    def __init__(self, browser):
        super().__init__(browser)

    def is_cart_displayed(self):
        return self._is_at_cart_page()

    def item_is_in_cart(self, item):
        for item_in_cart in self._get_items_names():
            if item in item_in_cart:
                return True
        return False
