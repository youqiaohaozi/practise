# from selenium import webdriver
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.chrome.options import Options
# from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver
from SeleniumStudy.POPractice_Pages.base_class import BaseClass
from selenium.webdriver.common.by import By


class AddMember(BaseClass):
    # def __init__(self,driver: WebDriver):
    #     self.driver=driver

    def addmember(self, username, userlable, userphone):
        ##点击添加成员进入输入界面
        self.element_find(By.CSS_SELECTOR, '#username').send_keys(username)
        self.element_find(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys(userlable)
        self.element_find(By.CSS_SELECTOR, '#memberAdd_phone').send_keys(userphone)
        self.element_find(By.CSS_SELECTOR, '.js_btn_save').click()  ##输入姓名/别名/手机号后点击保存
        checkbox = (By.CSS_SELECTOR, ".ww_checkbox")
        self.wait_for_visiable(checkbox)
        return True
