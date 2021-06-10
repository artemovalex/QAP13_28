from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.locators import BasePageLocators


class BasePage(object):
    URL = "https://www.labirint.ru/"

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def get_current_url(self):
        return self.browser.current_url

    def open_page(self):
        self.browser.get(self.url)

    def choose_element(self, how, what, timeout=5):
        element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        return element

    def open_cart(self):
        self.choose_element(*BasePageLocators.CART_BUTTON).click()

    def show_hover(self, how, what):
        ActionChains(self.browser).move_to_element(self.choose_element(how, what)).perform()

    def search(self, search_string):
        self.choose_element(*BasePageLocators.SEARCH_FIELD).send_keys(search_string)
        self.choose_element(*BasePageLocators.SEARCH_BUTTON).click()

    def scroll_to_top(self):
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

    def get_goods_amount_in_cart(self):
        return self.choose_element(*BasePageLocators.CART_BUTTON).text
