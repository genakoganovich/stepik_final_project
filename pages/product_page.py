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

    def guest_should_not_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_MESSAGE), \
            "Guest should not see success message after adding product to basket"

    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_MESSAGE), \
            "Guest should not see success message after opening the product page"

    def message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_MESSAGE), \
            "Success message should dissappear after adding product to basket"
