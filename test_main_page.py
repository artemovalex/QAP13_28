from selenium.webdriver.common.by import By

from pages.locators import BasePageLocators, MainPageLocators, CartPageLocators
from pages.main_page import MainPage


def test_big_main_fotorama_is_visible(browser):
    page = MainPage(browser, MainPage.URL)
    page.open_page()

    assert browser.find_element(*MainPageLocators.FIRST_FOTORAMA)


def test_cookie_policy_is_visible(browser):
    page = MainPage(browser, MainPage.URL)
    page.open_page()

    assert browser.find_element(*BasePageLocators.COOKIE_POLICY)


def test_all_images_are_placed(browser):
    page = MainPage(browser, MainPage.URL)
    page.open_page()
    images = browser.find_elements(By.CSS_SELECTOR, "img[src]")

    cnt_img = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            cnt_img += 1
    assert cnt_img == len(images)
