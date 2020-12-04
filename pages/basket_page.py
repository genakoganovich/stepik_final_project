from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT_TITLE), \
            "Should not be product in basket on basket page"

    def pull_empty_basket_text(self):
        return self.pull_text(*BasketPageLocators.BASKET_EMPTY_PARAGRAPH)

    def should_be_empty_basket_text(self):
        assert self.pull_empty_basket_text() == "Your basket is empty. Continue shopping", \
            "Should be 'Your basket is empty.' text on basket page"
