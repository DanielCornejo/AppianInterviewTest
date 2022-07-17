import unittest

from behavior.AmazonHomeBehavior import AmazonHomeBehavior
from framework.Browser import Browser


class AmazonHomeTests(unittest.TestCase):

    def setUp(self):
        self.browser = Browser()
        self.amazon_home_behavior = AmazonHomeBehavior(self.browser)

    def test_sanity_check(self):
        # Access Amazon Home
        self.amazon_home_behavior.access_home()
        self.assertEqual(True, self.amazon_home_behavior.check_home(), "Home loaded")

    def test_category_recommendation_load(self):
        # Access Amazon Home
        self.amazon_home_behavior.access_home()
        self.assertEqual(True, self.amazon_home_behavior.check_home(), "Home loaded")
        self.assertEqual(True, self.amazon_home_behavior.are_category_recommendations_loaded(),
                         "Category recommendation loaded")

    def tearDown(self):
        self.browser.close()


if __name__ == '__main__':
    unittest.main()
