from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_CONTENT_TITLE = (By.CSS_SELECTOR, "#content_inner div.basket-title")
    BASKET_EMPTY_PARAGRAPH = (By.CSS_SELECTOR, "#content_inner p")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_INPUT1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_INPUT2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main  h1")
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) div strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main  .price_color")
    PRODUCT_PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages div div p:nth-child(1) strong")
