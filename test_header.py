from pages.locators import BasePageLocators
from pages.main_page import MainPage

def test_header_is_visible(browser):
    page = MainPage(browser, MainPage.URL)
    page.open_page()

    assert browser.find_element(*BasePageLocators.HEADER)

def test_message_hover_appears(browser):
    page = MainPage(browser, MainPage.URL)
    page.open_page()
    page.show_hover(*BasePageLocators.MESSAGES_BUTTON)

    assert page.choose_element(*BasePageLocators.MESSAGE_HOVER)
    assert page.choose_element(*BasePageLocators.MESSAGE_HOVER).text == "У вас пока нет сообщений!"

def test_cart_hover_appears(browser):
    page = MainPage(browser, MainPage.URL)
    page.open_page()
    page.show_hover(*BasePageLocators.CART_BUTTON)

    assert page.choose_element(*BasePageLocators.CART_HOVER)

def test_cabinet_hover_appears(browser):
    page = MainPage(browser, MainPage.URL)
    page.open_page()
    page.show_hover(*BasePageLocators.CABINET_BUTTON)

    assert page.choose_element(*BasePageLocators.CABINET_HOVER)

def test_favourites_hover_appears(browser):
    page = MainPage(browser, MainPage.URL)
    page.open_page()
    page.show_hover(*BasePageLocators.FAVOURITES_BUTTON)

    assert page.choose_element(*BasePageLocators.FAVOURITES_HOVER)

def test_all_header_elements_presented(browser):
    page = MainPage(browser, MainPage.URL)
    page.open_page()

    assert page.choose_element(*BasePageLocators.LOGO)
    assert page.choose_element(*BasePageLocators.MESSAGES_BUTTON)
    assert page.choose_element(*BasePageLocators.CABINET_BUTTON)
    assert page.choose_element(*BasePageLocators.FAVOURITES_BUTTON)
    assert page.choose_element(*BasePageLocators.CART_BUTTON)
    assert page.choose_element(*BasePageLocators.ADULT_ONLY_ICON)
    assert page.choose_element(*BasePageLocators.MENU_BOOKS_BUTTON)
    assert page.choose_element(*BasePageLocators.MENU_MAIN_2021_BUTTON)
    assert page.choose_element(*BasePageLocators.MENU_SCHOOL_BUTTON)
    assert page.choose_element(*BasePageLocators.MENU_TOYS_BUTTON)
    assert page.choose_element(*BasePageLocators.MENU_STATIONARY_BUTTON)
    assert page.choose_element(*BasePageLocators.MENU_MORE_BUTTON)
    assert page.choose_element(*BasePageLocators.MENU_CLUB_BUTTON)
    assert page.choose_element(*BasePageLocators.MENU_CITY_BUTTON)
    assert page.choose_element(*BasePageLocators.MENU_DELIVERY_DATE_BUTTON)