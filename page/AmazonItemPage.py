from selenium.webdriver.common.by import By


class AmazonItemPage:

    def __init__(self, browser):
        self.__browser = browser

    def _get_name_of_item(self):
        locator = (By.ID, 'productTitle')
        return self.__browser.wait_for_element_presence(locator, 10).text
