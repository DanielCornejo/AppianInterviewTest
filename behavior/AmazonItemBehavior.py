from page.AmazonItemPage import AmazonItemPage


class AmazonItemBehavior(AmazonItemPage):

    def __init__(self, browser):
        super().__init__(browser)

    def item_is_correct(self, item):
        if self._get_name_of_item() is None:
            return False
        if item.lower() in self._get_name_of_item().lower():
            return True
        else:
            return False

    def get_price(self):
        return self._get_item_price()

    def add_to_cart(self):
        self._click_on_add_to_cart()

    def added_to_cart_message_displayed(self):
        return self._is_add_to_cart_message()

