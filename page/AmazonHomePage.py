from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.common.exceptions import TimeoutException

from framework.Browser import Browser


class AmazonHomePage(Browser):

    def __init__(self):
        super().__init__()

    def _access(self):
        self._open_url("amazon.com")
        self._maximize_window()

    def _is_at_home(self):
        wait = WebDriverWait(self._get_driver(), 10)
        try:
            wait.until(expected_conditions.presence_of_element_located((By.ID, "nav-logo")))
            return True
        except TimeoutException:
            return False

    def _set_search_item(self, item):
        self._get_element(By.ID, "twotabsearchtextbox").send_keys(item)

    def _click_search(self):
        self._get_element(By.ID, "nav-search-submit-button").click()

