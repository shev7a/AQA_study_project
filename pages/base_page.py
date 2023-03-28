from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    __slots__ = 'browser', 'url', 'timeout'

    def __init__(self, browser: WebDriver, url: str, timeout: int = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, by, selector):
        try:
            self.browser.find_element(by, selector)
        except NoSuchElementException:
            return False
        return True
