import pytest

from .pages.product_page import ProductPage, PRODUCT_PAGE_URL
from .pages.login_page import LoginPage, LOGIN_PAGE_URL
from .pages.basket_page import BasketPage

from mimesis import Person


class TestUserAddToBasketFromProductPageTestUserAddToBasketFromProductPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        test_user = Person()
        login_page = LoginPage(browser, LOGIN_PAGE_URL)
        login_page.open()
        login_page.register_new_user(test_user.email(unique=True), test_user.password(length=9))

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, PRODUCT_PAGE_URL)
        page.open()
        item_name, item_price = page.add_product_to_cart()
        page.should_be_popup_about_adding_to_cart()
        page.check_item_name_in_popup(item_name)
        page.should_be_popup_about_cart_info()
        page.check_cart_price(item_price)

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, PRODUCT_PAGE_URL)
        page.open()
        page.should_not_be_popup_about_adding_to_cart()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    item_name, item_price = page.add_product_to_cart("promo" in link)
    page.should_be_popup_about_adding_to_cart()
    page.check_item_name_in_popup(item_name)
    page.should_be_popup_about_cart_info()
    page.check_cart_price(item_price)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_PAGE_URL)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_popup_about_adding_to_cart()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, PRODUCT_PAGE_URL)
    page.open()
    page.should_not_be_popup_about_adding_to_cart()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_PAGE_URL)
    page.open()
    page.add_product_to_cart()
    page.popup_should_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, PRODUCT_PAGE_URL)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_PAGE_URL)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_PAGE_URL)
    page.open()
    page.go_to_cart_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()
    basket_page.should_be_empty_basket_message()
