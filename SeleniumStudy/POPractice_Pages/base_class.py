from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaseClass:
    base_url = ''

    def __init__(self, driver: webdriver = None):
        if driver == None:
            options = Options()
            options.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=options)
            self.driver.implicitly_wait(3)
        else:
            self.driver = driver

        if self.base_url != '':
            self.driver.get(self.base_url)

    def element_find(self, by, locator):
        return self.driver.find_element(by, locator)

    def elements_find(self, by, locator):
        return self.driver.find_elements(by, locator)

    def wait_for_click(self, locator, wait_time=10):
        element: WebElement = WebDriverWait(self.driver, wait_time).until(
            expected_conditions.element_to_be_clickable(locator))
        return element

    def wait_for_visiable(self, locator, wait_time=10):
        element: WebElement = WebDriverWait(self.driver, wait_time).until(
            expected_conditions.visibility_of_element_located(locator))
        return element

    # def wait_for_next(self,locator):
    #     try:
    #         self.driver.find_element(*locator).click()
