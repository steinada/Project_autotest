from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "form .btn.btn-lg.btn-primary[value='Register']")


class ProductPageLocators():
    ADD_TO_BACKET = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESS_ADDED = (By.CSS_SELECTOR, "#messages .alertinner strong")
    GO_TO_BACKET = (By.CSS_SELECTOR, "p a.btn.btn-info:nth-child(1)")
    BOOK_NAME = (By.CSS_SELECTOR, "div.col-sm-6 h1")
    BOOK_IN_BASKET_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main p")
    BACKET_COST = (By.CSS_SELECTOR, ".alertinner p strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p > a")