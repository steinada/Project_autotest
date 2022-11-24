from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_good(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form"), "Basket not found"
