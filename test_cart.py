from pages.cart_page import CartPage
from pages.locators import CartPageLocators
from pages.main_page import MainPage
from pages.product_page import ProductPage

def test_empty_cart(browser):
    page = MainPage(browser, MainPage.URL)
    page.open_page()
    page.open_cart()

    assert page.choose_element(*CartPageLocators.CART_EMPTY_TITLE)


def test_cart_url(browser):
    page = ProductPage(browser, ProductPage.URL)
    page.open_page()
    page.open_cart()

    assert "/cart/" in page.get_current_url()


def test_goods_amount_in_cart(browser):
    page = ProductPage(browser, ProductPage.URL)
    page.open_page()
    page.add_product_to_cart()

    assert page.get_goods_amount_in_cart() == "1"


def test_total_amount_on_cart_page(browser):
    page = ProductPage(browser, ProductPage.URL)
    page.open_page()
    page.add_product_to_cart()
    price = page.get_product_price()
    page.open_cart()

    page = CartPage(browser, browser.current_url)
    page.open_page()
    total = page.get_total_price()

    assert total == price


def test_product_title(browser):
    page = ProductPage(browser, ProductPage.URL)
    page.open_page()
    page.add_product_to_cart()
    title_on_prod_page = page.get_product_name()
    page.open_cart()

    page = CartPage(browser, browser.current_url)
    page.open_page()
    title_in_cart = page.get_product_name()

    assert title_in_cart in title_on_prod_page