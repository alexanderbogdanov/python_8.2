import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def open_google():
    browser.config.window_height = 907
    browser.config.window_width = 1592
    browser.open('https://google.com')

    yield

    browser.quit()
