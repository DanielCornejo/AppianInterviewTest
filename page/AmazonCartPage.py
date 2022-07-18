from selenium.webdriver.common.by import By


class AmazonCartPage:

    def __init__(self, browser):
        self.__browser = browser

    def _get_cart_items(self):
        locator = (By.XPATH, "//div[contains(@class,'a-row sc-list-item')]")
        return self.__browser.get_elements(locator[0], locator[1])

    def _is_at_cart_page(self):
        cart_message = self.__browser.get_element(By.XPATH, "//div[contains(@class,'sc-cart-header')]")
        return cart_message.is_displayed()

    def _get_items_names(self):
        locator = (By.XPATH, "//div[contains(@class,'a-row sc-list-item')]//span[contains(@class, 'sc-product-title')]"
                   + "//span[contains(@class,'a-truncate-full')]")
        items = self.__browser.get_elements(locator[0], locator[1])
        names_lowercase = []
        for i in items:
            names_lowercase.append(i.get_attribute("textContent").lower())
        return names_lowercase
