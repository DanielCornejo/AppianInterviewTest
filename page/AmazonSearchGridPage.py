from selenium.webdriver.common.by import By


class AmazonSearchGridPage:

    def __init__(self, browser):
        self.__browser = browser

    def _access_item_by_index(self, index):
        if index == "0":
            index = "1"
        locator =(By.XPATH, "//div[contains(@class,'search-results')]/div[@data-index='" + index + "']//img")
        item = self.__browser.get_element(locator[0], locator[1])
        self.__browser.wait_for_element_to_be_clickable(locator, 10)
        item.click()

    def _get_name_item_grid(self, index):
        if index == "0":
            index = "1"
        item = self.__browser.get_element(By.XPATH,
                                          "//div[contains(@class,'search-results')]/div[@data-index='" + index + "']"
                                          + "//span[contains(@class,'a-text-normal')]")
        return item.text

    def _search_loaded(self):
        locator = (By.XPATH, "//div[contains(@class,'search-results')]/div")
        if self.__browser.wait_for_elements_presence(locator, 10) is not None:
            return True
        else:
            return False
