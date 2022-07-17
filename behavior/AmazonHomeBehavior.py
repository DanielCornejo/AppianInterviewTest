from page.AmazonHomePage import AmazonHomePage


class AmazonHomeBehavior(AmazonHomePage):

    def __init__(self, browser):
        super().__init__(browser)

    def access_home(self):
        self._access()

    def check_home(self):
        return self._is_at_home()

    def are_category_recommendations_loaded(self):
        return self._category_recommendation_load()
