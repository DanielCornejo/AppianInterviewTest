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

