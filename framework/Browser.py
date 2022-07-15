from selenium import webdriver


class Browser:

    def __init__(self):
        self.__driver = webdriver.Chrome("\Selenium\Chrome\chromedriver.exe")
        self.__driver.implicitly_wait(5)

    def _get_driver(self):
        return self.__driver

    def _open_url(self, url):
        if "https" not in url:
            url = "https://" + url
        self.__driver.get(url)

    def close(self):
        self.__driver.quit()

    def _maximize_window(self):
        self.__driver.maximize_window()

    def _get_element(self, by, locator):
        return self.__driver.find_element(by, locator)

    def _get_elements(self, by, locator):
        return self.__driver.find_elements(by, locator)
