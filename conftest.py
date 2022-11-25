import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose prefer language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print("\nstart chrome browser for test..")
    if language:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    else:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

