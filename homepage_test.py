import pytest

from selenium import webdriver
from selenium.webdriver import FirefoxOptions

import page


@pytest.fixture
def browser():
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    browser = webdriver.Firefox(options=opts)
    # return
    yield browser
    # retake
    browser.quit()


def test_title_home(browser):
    """Checks if the word "Propiv" is in title"""
    browser.get("https://propiv.com/")

    main_page = page.MainPage(browser)
    assert main_page.is_title_matches() is True


def test_click_list_of_departamentos(browser):
    """Check navigation by home card Departamentos"""
    browser.get("https://propiv.com/")

    main_page = page.MainPage(browser)
    main_page.click_button_list_of_departamentos()

    listado_propiedades_page = page.ListOfPropiedadesResultPage(browser)
    assert listado_propiedades_page.is_title_listado_propiedades() is True
    assert listado_propiedades_page.is_departamento_result() is True
