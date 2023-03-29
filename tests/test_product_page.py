from pages.product_page import ProductPage

url = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, url)
    page.open()
    item_name, item_price = page.add_product_to_cart()
    page.should_be_popup_about_adding_to_cart()
    page.check_item_name_in_popup(item_name)
    page.should_be_popup_about_cart_info()
    page.check_cart_price(item_price)
