import unittest

from behavior.AmazonHomeBehavior import AmazonHomeBehavior
from behavior.AmazonItemBehavior import AmazonItemBehavior
from behavior.AmazonSearchGridBehavior import AmazonSearchGridBehavior
from behavior.AmazonTopBarBehavior import AmazonTopBarBehavior
from framework.Browser import Browser


class AmazonSearchTests(unittest.TestCase):

    def setUp(self):
        self.browser = Browser()
        self.amazon_home_behavior = AmazonHomeBehavior(self.browser)
        self.amazon_top_bar_behavior = AmazonTopBarBehavior(self.browser)
        self.amazon_search_grid_behavior = AmazonSearchGridBehavior(self.browser)
        self.amazon_item_behavior = AmazonItemBehavior(self.browser)

    def test_search_item_from_top_bar(self):
        item = "xiaomi"

        # Access to Amazon Home
        self.amazon_home_behavior.access_home()
        self.assertEqual(True, self.amazon_home_behavior.check_home(), "Home loaded")

        # Search item
        self.amazon_top_bar_behavior.search_item(item)
        self.assertEqual(True, self.amazon_search_grid_behavior.is_search_loaded(), "Search loaded")
        self.assertEqual(True, self.amazon_search_grid_behavior.search_is_correct(item), "Search is correct")

    def test_navigate_to_next_page(self):
        item = "xiaomi"

        # Access to Amazon Home
        self.amazon_home_behavior.access_home()
        self.assertEqual(True, self.amazon_home_behavior.check_home(), "Home loaded")

        # Search item
        self.amazon_top_bar_behavior.search_item(item)
        self.assertEqual(True, self.amazon_search_grid_behavior.is_search_loaded(), "Search loaded")
        self.assertEqual(True, self.amazon_search_grid_behavior.search_is_correct(item), "Search is correct")

        # Go to next page
        self.amazon_search_grid_behavior.next_page()
        self.assertEqual("2", self.amazon_search_grid_behavior.get_page(), "Is page 2")


    def tearDown(self):
        self.browser.close()


if __name__ == '__main__':
    unittest.main()
