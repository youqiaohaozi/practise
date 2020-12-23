import logging
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    root_logger = logging.getLogger()
    print(f'root_logger.handlers:{logging.getLogger().handlers}')
    for h in root_logger.handlers[:]:
        root_logger.removeHandler(h)
    logging.basicConfig(level = logging.INFO)

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        logging.info('find_element')
        logging.info(locator)
        return self.driver.find_element(*locator)

    def find_list(self, locator):
        logging.info('find element list')
        logging.info(locator)
        return self.driver.find_elements(*locator)

    def find_click(self, locator):
        logging.info('find element and click')
        logging.info(locator)
        self.driver.find_element(*locator).click()

    def find_input(self, locator, value):
        logging.info(f'find element {locator} and input value:{value}')
        self.driver.find_element(*locator).send_keys(value)

    def wait_clickable(self, locator, timeout=10):
        logging.info('wait until element clickable')
        logging.info(locator)
        return WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    def find_scroll(self, text):
        logging.info(f'scroll and find element with text:{text}')
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                               'scrollable(true).instance(0)).'
                                                               'scrollIntoView(new UiSelector().'
                                                               'text("'+text+'").instance(0));').click()
