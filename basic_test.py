import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import FirefoxOptions


@pytest.fixture
def browser():

    # apt-get install firefox-geckodriver

    opts = FirefoxOptions()
    opts.add_argument("--headless")
    browser = webdriver.Firefox(options=opts)
    yield browser
    browser.quit()


def test_basic_search(browser):

    browser.get("http://www.python.org")

    assert "Python" in browser.title

    elem = browser.find_element(by=By.NAME, value="q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)

    assert "No results found." not in browser.page_source
