from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    URL = "https://www.labirint.ru/books/796276/"

    def add_product_to_cart(self):
        self.browser.execute_script("arguments[0].scrollIntoView();", self.choose_element(*ProductPageLocators.ADD_TO_CART))
        self.choose_element(*ProductPageLocators.ADD_TO_CART).click()

    def close_popup_add_to_cart(self):
        self.choose_element(*ProductPageLocators.POPUP_ADDED_TO_CART).click()

    def get_product_price(self):
        return self.choose_element(*ProductPageLocators.GOODS_PRICE).text

    def get_product_name(self):
        return self.choose_element(*ProductPageLocators.PRODUCT_TITLE).text
