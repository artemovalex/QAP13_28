import pytest
from selenium.webdriver.common.by import By

from pages.locators import BasePageLocators
from pages.main_page import MainPage


@pytest.mark.positive
@pytest.mark.guest
@pytest.mark.parametrize("email", ["test3test@mail.ru", "test4test@mail.ru", "test5test@mail.ru", "test7test@mail.ru"])
def test_register_from_main(browser, email):
    browser.implicitly_wait(5)
    page = MainPage(browser, MainPage.URL)
    page.open_page()
    page.show_hover(*BasePageLocators.CABINET_BUTTON)
    page.choose_element(*BasePageLocators.CABINET_HOVER_REGISTER_BUTTON).click()
    browser.switch_to_active_element()
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите свой код скидки, телефон или эл.почту']").clear()
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите свой код скидки, телефон или эл.почту']").send_keys(email)

    assert browser.find_element(By.CSS_SELECTOR, "[data-default-value='Войти']").click()


@pytest.mark.xfail
@pytest.mark.negative
@pytest.mark.guest
@pytest.mark.parametrize("email", ["f"*15, "", "f"*255, "ф"*255, "ф"*15, 0, 1, 250, -1, 1.5, "   ", "|!@#$%^&*()-_=+`~?№;:[]{}"])
def test_register_from_main_neg(browser, email):
    browser.implicitly_wait(5)
    page = MainPage(browser, MainPage.URL)
    page.open_page()
    page.show_hover(*BasePageLocators.CABINET_BUTTON)
    page.choose_element(*BasePageLocators.CABINET_HOVER_REGISTER_BUTTON).click()
    browser.switch_to_active_element()
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите свой код скидки, телефон или эл.почту']").clear()
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите свой код скидки, телефон или эл.почту']").send_keys("email")

    assert browser.find_element(By.CSS_SELECTOR, "[data-default-value='Войти']").click()