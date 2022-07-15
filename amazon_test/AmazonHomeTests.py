import unittest

from behavior.AmazonHomeBehavior import AmazonHomeBehavior


class AmazonHomeTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.amazon_home_behavior = AmazonHomeBehavior()

    def test_sanity_check(self):
        self.amazon_home_behavior.access_home()
        self.assertEqual(True, self.amazon_home_behavior.check_home())

    def test_search_item(self):
        self.amazon_home_behavior.access_home()
        self.assertEqual(True, self.amazon_home_behavior.check_home())
        self.amazon_home_behavior.search_item("xiaomi")

    @classmethod
    def tearDownClass(cls):
        cls.amazon_home_behavior.close()

if __name__ == '__main__':
    unittest.main()
