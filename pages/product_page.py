from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "The add to cart button isn't present on the page"

    def add_product_to_cart(self):
        cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        cart_button.click()
        self.solve_quiz_and_get_code()
        return self.browser.find_element(*ProductPageLocators.ITEM_NAME).text, \
               self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text

    def should_be_popup_about_adding_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_POPUP_ADDING), \
            "The popup about adding item to cart isn't present on the page"

    def should_be_popup_about_cart_info(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_POPUP_CART), \
            "The popup about cart info isn't present on the page"

    def check_item_name_in_popup(self, item_name: str):
        popup_item_name = self.browser.find_element(*ProductPageLocators.SUCCESS_POPUP_ADDING_ITEM_NAME).text
        assert popup_item_name == item_name, \
            f"The product name in the popup is different from the product name in the card ({popup_item_name} instead {item_name})"

    def check_cart_price(self, item_price):
        assert self.browser.find_element(*ProductPageLocators.SUCCESS_POPUP_CART_PRICE).text == item_price, \
            "The price in the cart differs from the price in the card"
