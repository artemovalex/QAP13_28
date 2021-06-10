import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.main_page import MainPage


@pytest.mark.parametrize("search_string", ["f"*15, "", "f"*255, "ф"*255, "ф"*15, 0, 1, 250, -1, 1.5, "   ", "|!@#$%^&*()-_=+`~?№;:[]{}"])
def test_guest_can_see_search_results(browser, search_string):
    page = MainPage(browser, MainPage.URL)
    page.open_page()
    page.search(search_string)

    result_page = BasePage(browser, page.browser.current_url)
    result_text = result_page.choose_element(By.CSS_SELECTOR, "h1").text

    expected_text1 = "Все, что мы нашли в Лабиринте по запросу «Бунин»"
    expected_text2 = "Мы ничего не нашли по вашему запросу! Что делать?"

    assert result_text == expected_text1 or result_text == expected_text2
