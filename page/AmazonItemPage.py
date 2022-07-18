from selenium.webdriver.common.by import By


class AmazonItemPage:

    def __init__(self, browser):
        self.__browser = browser

    def _get_name_of_item(self):
        locator = (By.ID, 'productTitle')
        return self.__browser.wait_for_element_presence(locator, 10).text

    def _get_item_price(self):
        whole = (By.XPATH, "//div[@id='apex_desktop']//span[contains(@class,'a-price-whole')]")
        fraction = (By.XPATH, "//div[@id='apex_desktop']//span[contains(@class,'a-price-fraction')]")
        whole_num = self.__browser.get_element(whole[0], whole[1]).text
        fraction_num = self.__browser.get_element(fraction[0], fraction[1]).text
        return whole_num + "." + fraction_num

    def _click_on_add_to_cart(self):
        locator = (By.ID, "add-to-cart-button")
        self.__browser.wait_for_element_to_be_clickable(locator, 10)
        add_to_cart_button = self.__browser.get_element(locator[0], locator[1])
        add_to_cart_button.click()

    def _is_add_to_cart_message(self):
        locator = (By.XPATH, "//span[contains(@class,'sw-atc-text')]")
        if self.__browser.wait_for_element_presence(locator, 10) is not None:
            return True
        else:
            return False
