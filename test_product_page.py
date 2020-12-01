from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.press_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.should_product_name_match(page.pull_product_name())
    page.should_product_price_match(page.pull_product_price())