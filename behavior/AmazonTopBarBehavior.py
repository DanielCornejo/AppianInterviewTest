from page.AmazonTopBarPage import AmazonTopBarPage


class AmazonTopBarBehavior(AmazonTopBarPage):

    def __init__(self, browser):
        super().__init__(browser)

    def search_item(self, item):
        self._set_search_item(item)
        self._click_search()


