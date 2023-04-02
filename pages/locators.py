from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_POPUP_ADDING = (By.XPATH, "//div[contains(@class, 'alert-success')][1]/div")
    SUCCESS_POPUP_ADDING_ITEM_NAME = (By.XPATH, "//div[contains(@class, 'alert-success')][1]/div/strong")
    SUCCESS_POPUP_CART = (By.XPATH, "//div[contains(@class, 'alert-info')]/div/p[contains(text(), "
                                    "'Your basket total is now')]")
    SUCCESS_POPUP_CART_PRICE = (By.XPATH, "//div[contains(@class, 'alert-info')]/div/p/strong")
