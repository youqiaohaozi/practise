from selenium import webdriver
from selenium.webdriver.common.by import By


class RegPage:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/register_wx?from=myhome")


    def registe(self):
        pass