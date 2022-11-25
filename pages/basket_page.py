from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Basket is not empty"

    def should_not_be_order_button(self):
        assert self.is_disappeared(*BasketPageLocators.CHECKOUT_BUTTON), "Basket is not empty"