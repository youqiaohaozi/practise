import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from AppiumStudy.frame.pages.blacklist import blacklist


class BasePage:
    black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
    error_num = 0
    max_num = 5

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @blacklist
    def find(self, by, locator=None):
        if locator is None:
            result = self.driver.find_element(*by)
        else:
            result = self.driver.find_element(by, locator)
        return result

    def prase_yaml(self, file_path, func_name):
        with open(file_path, encoding="utf-8") as f:
            data = yaml.load(f)
        self.prase(data[func_name])

    def prase(self, steps):
        for step in steps:
            if step['action'] == 'click':
                self.find(step['by'], step['locator']).click()
            elif step['action'] == 'input':
                self.find(step['by'], step['locator']).send_keys(step['content'])







