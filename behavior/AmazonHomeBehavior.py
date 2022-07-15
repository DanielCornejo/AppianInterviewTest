from page.AmazonHomePage import AmazonHomePage


class AmazonHomeBehavior(AmazonHomePage):

    def __init__(self):
        super().__init__()

    def access_home(self):
        self._access()

    def search_item(self, item):
        self._set_search_item(item)
        self._click_search()

    def check_home(self):
        return self._is_at_home()

