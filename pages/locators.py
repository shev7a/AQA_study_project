from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_BUTTON = (By.CSS_SELECTOR, ".btn-group a[href$='/basket/']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL_INPUT = (By.CSS_SELECTOR, "[name='registration-email']")
    REG_PASSWORD_INPUT = (By.CSS_SELECTOR, "[name='registration-password1']")
    REG_REPEAT_PASSWORD_INPUT = (By.CSS_SELECTOR, "[name='registration-password2']")
    REG_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
    SUCCESS_REG_POPUP = (By.CSS_SELECTOR, ".alert-success")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_POPUP_ADDING = (By.XPATH, "//div[contains(@class, 'alert-success')][1]/div")
    SUCCESS_POPUP_ADDING_ITEM_NAME = (By.XPATH, "//div[contains(@class, 'alert-success')][1]/div/strong")
    SUCCESS_POPUP_CART = (By.XPATH, "//div[contains(@class, 'alert-info')]/div/p[contains(text(), "
                                    "'Your basket total is now')]")
    SUCCESS_POPUP_CART_PRICE = (By.XPATH, "//div[contains(@class, 'alert-info')]/div/p/strong")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p:has(a[href$='/'])")
