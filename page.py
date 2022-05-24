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

    def click_button_list_of_oficinas(self):
        # busco elemento por href
        element = self.driver.find_element_by_xpath('//a[@href="/listado-de-propiedades/?property_type=17"]')
        element.click()

    def click_button_list_of_casas(self):
        # busco elemento por href
        element = self.driver.find_element_by_xpath('//a[@href="/listado-de-propiedades/?property_type=1"]')
        element.click()

    def click_button_list_of_terrenos(self):
        # busco elemento por href
        element = self.driver.find_element_by_xpath('//a[@href="/listado-de-propiedades/?property_type=7"]')
        element.click()

    def click_button_list_of_todas(self):
        # busco elemento por href
        element = self.driver.find_element_by_xpath('//a[@href="/listado-de-propiedades/"]')
        element.click()


class ListOfPropiedadesResultPage(BasePage):
    """Pagina de listado de propiedades resultado de consultas"""

    def is_title_listado_propiedades(self):
        return "Listado de propiedades" in self.driver.title

    def is_departamento_result(self):
        element = self.driver.find_element(by=By.XPATH, value="//*[@class='ts-title']/h1")
        return "Departamento" in element.get_attribute("innerHTML")

    def is_oficina_result(self):
        element = self.driver.find_element(by=By.XPATH, value="//*[@class='ts-title']/h1")
        return "Oficina" in element.get_attribute("innerHTML")

    def is_casa_result(self):
        element = self.driver.find_element(by=By.XPATH, value="//*[@class='ts-title']/h1")
        return "Casa" in element.get_attribute("innerHTML")

    def is_terreno_result(self):
        element = self.driver.find_element(by=By.XPATH, value="//*[@class='ts-title']/h1")
        return "Terreno" in element.get_attribute("innerHTML")

    def is_todas_result(self):
        element = self.driver.find_element(by=By.XPATH, value="//*[@class='ts-title']/h1")
        return "propiedades" in element.get_attribute("innerHTML")
