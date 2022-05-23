from selenium.webdriver.common.by import By


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here."""

    def is_title_matches(self):
        """Verifies that the hardcoded text "Propiv" appears in page title"""

        return "Propiv" in self.driver.title

    def click_button_list_of_departamentos(self):
        # busco elemento por href
        element = self.driver.find_element_by_xpath('//a[@href="/listado-de-propiedades/?property_type=2"]')
        element.click()


class ListOfPropiedadesResultPage(BasePage):
    """Pagina de listado de propiedades resultado de consultas"""

    def is_title_listado_propiedades(self):
        return "Listado de propiedades" in self.driver.title

    def is_departamento_result(self):
        element = self.driver.find_element(by=By.XPATH, value="//*[@class='ts-title']/h1")
        return "Departamento" in element.get_attribute("innerHTML")
