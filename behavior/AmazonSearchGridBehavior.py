from page.AmazonSearchGridPage import AmazonSearchGridPage


class AmazonSearchGridBehavior(AmazonSearchGridPage):

    def __init__(self, browser):
        super().__init__(browser)

    def access_to_item_by_index(self, index):
        index_str = str(index)
        self._access_item_by_index(index_str)

    def next_page(self):
        self._click_on_next()

    def get_page(self):
        return self._get_page_number()

    def is_search_loaded(self):
        return self._search_loaded()

    def search_is_correct(self, item):
        name = self._get_name_item_grid("1")
        if item.lower() in name.lower():
            return True
        else:
            return False


