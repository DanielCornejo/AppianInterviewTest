import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Browser:

    def __init__(self):
        self.__driver = webdriver.Chrome("\Selenium\Chrome\chromedriver.exe")
        self.__driver.implicitly_wait(5)

    def get_driver(self):
        return self.__driver

    def open_url(self, url):
        if "https" not in url:
            url = "https://" + url
        self.__driver.get(url)

    def close(self):
        self.__driver.quit()

    def maximize_window(self):
        self.__driver.maximize_window()

    def get_element(self, by, locator):
        return self.__driver.find_element(by, locator)

    def get_elements(self, by, locator):
        return self.__driver.find_elements(by, locator)

    def scroll_into_view(self, locator):
        element = self.get_element(locator[0], locator[1])
        actions = ActionChains(self.__driver)
        actions.move_to_element(element).perform()

    def wait_for_element_presence(self, locator, wait_time):
        wait = WebDriverWait(self.get_driver(), wait_time)
        try:
            return wait.until(expected_conditions.presence_of_element_located((locator[0], locator[1])))
        except TimeoutException:
            return None

    def wait_for_elements_presence(self, locator, wait_time):
        wait = WebDriverWait(self.get_driver(), wait_time)
        try:
            return wait.until(expected_conditions.presence_of_all_elements_located((locator[0], locator[1])))
        except TimeoutException:
            return None

    def wait_for_element_attribute_be(self, locator, attribute, text, wait_time):
        wait = WebDriverWait(self.get_driver(), wait_time)
        try:
            return wait.until(expected_conditions.text_to_be_present_in_element_attribute(locator, attribute, text))
        except TimeoutException:
            return None

    def wait_for_element_to_be_clickable(self, locator, wait_time):
        wait = WebDriverWait(self.get_driver(), wait_time)
        try:
            time.sleep(2)
            return wait.until(expected_conditions.element_to_be_clickable(locator))
        except TimeoutException:
            return None


