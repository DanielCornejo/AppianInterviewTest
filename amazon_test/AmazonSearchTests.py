import unittest

from behavior.AmazonHomeBehavior import AmazonHomeBehavior
from behavior.AmazonItemBehavior import AmazonItemBehavior
from behavior.AmazonSearchGridBehavior import AmazonSearchGridBehavior
from behavior.AmazonTopBarBehavior import AmazonTopBarBehavior
from framework.Browser import Browser


class MyTestCase(unittest.TestCase):

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

    def test_access_searched_item(self):
        item = "xiaomi"

        # Access to Amazon Home
        self.amazon_home_behavior.access_home()
        self.assertEqual(True, self.amazon_home_behavior.check_home(), "Home loaded")

        # Search item
        self.amazon_top_bar_behavior.search_item(item)
        self.assertEqual(True, self.amazon_search_grid_behavior.is_search_loaded(), "Search loaded")
        self.assertEqual(True, self.amazon_search_grid_behavior.search_is_correct(item), "Search is correct")

        # Access to item
        self.amazon_search_grid_behavior.access_to_item_by_index(1)
        self.assertEqual(True, self.amazon_item_behavior.item_is_correct(item), "Item name correct")

    def tearDown(self):
        self.browser.close()


if __name__ == '__main__':
    unittest.main()
