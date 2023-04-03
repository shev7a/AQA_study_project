from .base_page import BasePage
from .login_page import LoginPage
from .locators import MainPageLocators

MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/"


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
