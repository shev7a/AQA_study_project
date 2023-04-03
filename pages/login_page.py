from .base_page import BasePage
from .locators import LoginPageLocators

LOGIN_PAGE_URL = 'https://selenium1py.pythonanywhere.com/ru/accounts/login/'


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Incorrect PRODUCT_URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form isn't present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form isn't present"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REG_EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_REPEAT_PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_SUBMIT_BUTTON).click()
        # assert self.is_element_present(*LoginPageLocators.SUCCESS_REG_POPUP)
        self.should_be_authorized_user()
