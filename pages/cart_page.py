from pages.base_page import BasePage
from pages.locators import CartPageLocators

class CartPage(BasePage):
    URL = "https://www.labirint.ru/cart/"

    def get_total_price(self):
        return self.choose_element(*CartPageLocators.TOTAL_PRICE_IN_CART).text

    def get_product_name(self):
        return self.choose_element(*CartPageLocators.PRODUCT_TITLE).text
