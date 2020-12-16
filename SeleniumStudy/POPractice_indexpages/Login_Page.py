from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")

    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR,'.login_registerBar_link').click()
        return RegPage(self.driver)
