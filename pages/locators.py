from selenium.webdriver.common.by import By

class BasePageLocators:
    # Header elements (includes 1st and 2nd lines)
    HEADER = (By.CSS_SELECTOR, ".b-header-outer")

    # 1st line:
    LOGO = (By.CSS_SELECTOR, "a[href='/']")
    SEARCH_FIELD = (By.CSS_SELECTOR, "#search-field")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".b-header-b-search-e-btn")
    MESSAGES_BUTTON = (By.CSS_SELECTOR, ".top-link-main_notification")
    CABINET_BUTTON = (By.CSS_SELECTOR, ".js-b-autofade-wrap")
    FAVOURITES_BUTTON = (By.CSS_SELECTOR, ".top-link-main_putorder")
    CART_BUTTON = (By.CSS_SELECTOR, "span[class='b-header-b-personal-e-icon-count-m-cart basket-in-cart-a']")
    ADULT_ONLY_ICON = (By.CSS_SELECTOR, ".b-header-e-icon-adult-m-big")

    # 1st line hovers
    CART_HOVER = (By.CSS_SELECTOR,
                  "div[class='popup-window top-block-popup basket-popup dropdown-block js-change-popup-position  "
                  "not-empty-hidden dropdown-block-opened']")
    MESSAGE_HOVER = (By.CSS_SELECTOR,
                     "div[class='b-menu-list-title font_regular']")
    CABINET_HOVER = (By.CSS_SELECTOR, ".b-header-login-action-logo-e-wrap")
    CABINET_HOVER_REGISTER_BUTTON = (By.XPATH,
                                     "//div[@class='popup-window top-block-popup basket-popup dropdown-block "
                                     "js-change-popup-position dropdown-block-opened']//div["
                                     "@class='b-header-login-e-enter']")

    FAVOURITES_HOVER = (By.CSS_SELECTOR, "[class='b-menu-list-title font_regular tac']")

    # 2nd line:
    MENU_BOOKS_BUTTON = (By.CSS_SELECTOR, 'li[data-toggle="header-genres"]')
    MENU_MAIN_2021_BUTTON = (By.CSS_SELECTOR, 'li[data-toggle="header-best"]')
    MENU_SCHOOL_BUTTON = (By.CSS_SELECTOR, 'li[data-toggle="header-school"]')
    MENU_TOYS_BUTTON = (By.CSS_SELECTOR, 'li[data-toggle="header-toys"]')
    MENU_STATIONARY_BUTTON = (By.CSS_SELECTOR, 'li[data-toggle="header-office"]')
    MENU_MORE_BUTTON = (By.CSS_SELECTOR, 'li[data-toggle="header-more"]')
    MENU_CLUB_BUTTON = (By.CSS_SELECTOR, 'li[data-toggle="header-club"]')
    MENU_CITY_BUTTON = (By.CSS_SELECTOR, 'span[class="b-header-b-menu-e-link last-child"]')
    MENU_DELIVERY_DATE_BUTTON = (By.CSS_SELECTOR, 'span[class="b-header-b-menu-e-link first-child last-child analytics-click-js"]')

    # Footer elements:
    FOOTER = (By.CSS_SELECTOR, ".b-rfooter-info-content")

    # Basic elements:
    COOKIE_POLICY = (By.CSS_SELECTOR, ".cookie-policy__button")


class MainPageLocators:
    BIG_FIRST_FOTORAMA = (By.CSS_SELECTOR, "div[class ='banner-big fleft radius-5 fotorama-no-transition']")
    TOP_TITLE = (By.CSS_SELECTOR, ".index-top-title")
    FIRST_FOTORAMA = (By.CSS_SELECTOR, "div[class ='banner-big fleft radius-5 fotorama-no-transition']")
    BIG_BANNER = (By.CSS_SELECTOR, ".fotorama__stage")
    MEDIUM_BANNER = (By.CSS_SELECTOR, ".banners-small-wrapper__index")
    SMALL_BANNER = (By.CSS_SELECTOR, ".banner-shelf__cover-wrapper")

    BLOCKER_SLIDER_ARROWS_ON_BIG_BANNER = (By.CSS_SELECTOR, ".fotorama__wrap--no-controls")

    IMAGES = (By.CSS_SELECTOR, "img[src]")

    DELIVERY_DATE = (By.CSS_SELECTOR, 'span[class="b-header-b-menu-e-link first-child last-child analytics-click-js"]')


class CartPageLocators:
    CART_EMPTY_TITLE = (By.XPATH, "//span[contains(text(),'Ваша корзина пуста. Почему?')]")
    MY_CART_LABEL = (By.CSS_SELECTOR, "a[data-event-label='myCart']")
    TOTAL_PRICE_IN_CART = (By.CSS_SELECTOR, "#basket-default-sumprice-discount")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product-title")


class ProductPageLocators:
    GOODS_PRICE = (By.CSS_SELECTOR, ".buying-pricenew-val-number")
    ADD_TO_CART = (By.CSS_SELECTOR, "span[class ='text']")
    POPUP_ADDED_TO_CART = (By.CSS_SELECTOR, "a[class='b-basket-popinfo-close']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "h1")
