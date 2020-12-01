from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def press_add_to_basket_button(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_product_name_match(self, product_name):
        assert product_name == self.pull_text(*ProductPageLocators.PRODUCT_NAME_MESSAGE), \
            "Product name doesn't match product name message"

    def should_product_price_match(self, product_price):
        assert product_price == self.pull_text(*ProductPageLocators.PRODUCT_PRICE_MESSAGE), \
            "Product price doesn't match product price message"

    def pull_product_name(self):
        return self.pull_text(*ProductPageLocators.PRODUCT_NAME)

    def pull_product_price(self):
        return self.pull_text(*ProductPageLocators.PRODUCT_PRICE)
