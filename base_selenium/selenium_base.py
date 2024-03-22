"""This is the base file where base methods will be created"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement

from selenium.common.exceptions import NoSuchElementException, TimeoutException



"""Defines a class constructor (__init__) for a class that appears to encapsulate interactions with a WebDriver. """
class SeleniumBase:
    """Defines the constructor method for the class SeleniumBase which takes one parameter 'driver',
    probably a WebDriver instance, which will be used for automating interactions with a web browser."""
    def __init__(self, driver):
        """Assigns the WebDriver instance passed to the constructor to an instance variable 'self.driver'.
        This allows the WebDriver to be accessed throughout the class"""
        self.driver = driver
        """Initializes a WebDriverWait object and assigns it to an instance variable 'self.__wait'
        which is used to wait for conditions to be met before proceeding with the execution of code"""
        self.__wait = WebDriverWait(driver, 15, 0.3, ignored_exceptions=[StaleElementReferenceException])
        """"""
        self.__action = ActionChains(driver)
    
    def find_element(self, locator):
        """
        Find and return the element identified by the locator.

        Args:
            locator: Tuple (By, value) identifying the element.

        Returns:
            WebElement: The element found.

        Raises:
            NoSuchElementException: If the element is not found.
        """
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException as e:
            raise NoSuchElementException(f"Element {locator} not found") from e
        
    def input_textbox(self, locator, clear_existing=True) -> WebElement:
        """
        Input text into the specified input box.

        Args:
            locator: Tuple (By, value) identifying the input box element.
            text: Text to input into the input box.
            clear_existing: Whether to clear existing text before inputting. Default is True.
        """
        inputbox = self.find_element(locator)
        if clear_existing:
            inputbox.clear()
            inputbox.sendkey(text)
    
    def radio_button(self, locator) -> WebElement:
        """
        Clicks the radio button identified by the locator.

        Args:
            locator: Tuple (By, value) identifying the radio button element.
        """
        radiobutton = self.find_element(locator)
        radiobutton.click()

    def click_checkbox(self, locator) -> WebElement:
        """
        Clicks the checkbox identified by the locator.

        Args:
            locator: Tuple (By, value) identifying the checkbox element.
        """
        checkbox = self.find_element(locator)
        if not checkbox.is_selected():
            checkbox.click()

    def select_dropdown_option(self, locator, option, by="text") -> WebElement:
        """
        Selects a dropdown option.

        Args:
            locator: Tuple (By, value) identifying the dropdown element.
            option: Option to select. It can be the option's text, index, or value depending on the 'by' parameter.
            by: Method to select the option. It can be "text", "index", or "value". Default is "text".
        """
        dropdown = Select(self.find_element(locator))
        if by == "index":
            dropdown.select_by_index(option)
        elif by == "value":
            dropdown.select_by_value(option)
        else:
            dropdown.select_by_visible_text(option)

    def search_and_select_dropdown_option(self, locator, search_term) -> WebElement:
        """
        Searches and selects a dropdown option by typing into the dropdown input box.

        Args:
            locator: Tuple (By, value) identifying the dropdown element.
            search_term: Text to search for in the dropdown options.
        """
        dropdown = self.find_element(locator)
        dropdown.click()
        dropdown_input = dropdown.find_element(locator)
        dropdown_input.send_keys(search_term)
        dropdown_input.send_keys(Keys.ENTER)
