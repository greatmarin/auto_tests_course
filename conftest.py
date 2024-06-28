import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, es, en, fr, etc.")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    if language:
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()