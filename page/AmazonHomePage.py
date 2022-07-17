from selenium.webdriver.common.by import By


class AmazonHomePage:

    def __init__(self, browser):
        self.__browser = browser

    def _access(self):
        self.__browser.open_url("amazon.com")
        self.__browser.maximize_window()

    def _is_at_home(self):
        locator = (By.ID, "nav-logo")
        if self.__browser.wait_for_element_presence(locator, 10) is not None:
            return True
        else:
            return False

    def _category_recommendation_load(self):
        locator = (By.XPATH, "//div[@id='gw-card-layout']/div[contains(@id,'desktop')]")
        if self.__browser.wait_for_elements_presence(locator, 10) is not None:
            return True
        else:
            return False
