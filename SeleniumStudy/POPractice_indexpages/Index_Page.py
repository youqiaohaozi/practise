

from selenium import webdriver
from selenium.webdriver.common.by import By


class IndexPage:

    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    def goto_login(self):
        self.driver.find_element(By.CSS_SELECTOR,'.index_top_operation_loginBtn').click()
        return LoginPage(self.driver)

    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR,'.index_head_info_pCDownloadBtn').click()
        return RegPage(self.driver)