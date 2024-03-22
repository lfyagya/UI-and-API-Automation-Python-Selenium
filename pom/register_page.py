from selenium.webdriver.remote.webelement import WebElement
from base_selenium import selenium_base

class Register(selenium_base):
    def __init__(self, driver, config):
        super().__init__(driver)
        self.config = config

    __locator_name = ''

    def text (self) -> WebElement:
        self.get('locator_name')
        return self.input_textbox('css', self.__locator_name)

