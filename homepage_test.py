import pytest

from selenium import webdriver
from selenium.webdriver import FirefoxOptions

import page


@pytest.fixture
def browser():
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    browser = webdriver.Firefox(executable_path="/usr/bin/geckodriver", options=opts)

    # return
    yield browser
    # retake
    browser.quit()


def test_title_home(browser):
    """Checks if the word "Propiv" is in title"""
    browser.get("https://propiv.com/")

    main_page = page.MainPage(browser)
    assert main_page.is_title_matches() is True


def test_click_card_departamentos(browser):
    """Check navigation by home card Departamentos"""

    browser.get("https://propiv.com/")

    main_page = page.MainPage(browser)

    main_page.click_button_list_of_departamentos()

    listado_propiedades_page = page.ListOfPropiedadesResultPage(browser)
    assert listado_propiedades_page.is_title_listado_propiedades() is True
    assert listado_propiedades_page.is_departamento_result() is True


def test_click_card_oficinas(browser):
    """Check navigation by home card Oficinas"""
    browser.get("https://propiv.com/")

    main_page = page.MainPage(browser)
    main_page.click_button_list_of_oficinas()

    listado_propiedades_page = page.ListOfPropiedadesResultPage(browser)
    assert listado_propiedades_page.is_title_listado_propiedades() is True
    assert listado_propiedades_page.is_oficina_result() is True


def test_click_card_casa(browser):
    """Check navigation by home card casas"""
    browser.get("https://propiv.com/")

    main_page = page.MainPage(browser)
    main_page.click_button_list_of_casas()

    listado_propiedades_page = page.ListOfPropiedadesResultPage(browser)
    assert listado_propiedades_page.is_title_listado_propiedades() is True
    assert listado_propiedades_page.is_casa_result() is True


def test_click_card_terrenos(browser):
    """Check navigation by home card terrenos"""
    browser.get("https://propiv.com/")

    main_page = page.MainPage(browser)
    main_page.click_button_list_of_terrenos()

    listado_propiedades_page = page.ListOfPropiedadesResultPage(browser)
    assert listado_propiedades_page.is_title_listado_propiedades() is True
    assert listado_propiedades_page.is_terreno_result() is True


def test_click_card_propiedades_todas(browser):
    """Check navigation by home card todas"""
    browser.get("https://propiv.com/")

    main_page = page.MainPage(browser)
    main_page.click_button_list_of_todas()

    listado_propiedades_page = page.ListOfPropiedadesResultPage(browser)
    assert listado_propiedades_page.is_title_listado_propiedades() is True
    assert listado_propiedades_page.is_todas_result() is True
