from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ProductPage(BasePage):
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ADDED), \
            "Success message is presented, but should not be"

    def add_to_basket(self, link):
        self.browser.get(link)
        button_add_product = self.browser.find_element(*ProductPageLocators.ADD_TO_BACKET)
        button_add_product.click()
        self.solve_quiz_and_get_code()

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ADDED), "Success massage is not on page"

    def should_be_correct_name(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_IN_BASKET_NAME).text == self.browser.find_element(*ProductPageLocators.BOOK_NAME).text, "Was added another good"

    def should_be_correct_cost(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text == self.browser.find_element(*ProductPageLocators.BACKET_COST).text, "Price of added good isn't correct"
