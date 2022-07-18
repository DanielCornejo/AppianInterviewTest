from selenium.webdriver.common.by import By


class AmazonTopBarPage:

    def __init__(self, browser):
        self.__browser = browser

    def _set_search_item(self, item):
        locator = (By.ID, "twotabsearchtextbox")
        self.__browser.get_element(locator[0], locator[1]).send_keys(item)
        self.__browser.wait_for_element_attribute_be(locator, "value", item, 10)

    def _click_search(self):
        locator = (By.ID, "nav-search-submit-text")
        self.__browser.wait_for_element_to_be_clickable(locator, 10)
        search_button = self.__browser.get_element(locator[0], locator[1])
        search_button.click()

    def click_on_cart(self):
        locator = (By.ID, "nav-cart-text-container")
        self.__browser.wait_for_element_to_be_clickable(locator, 10)
        cart_button = self.__browser.get_element(locator[0], locator[1])
        cart_button.click()



