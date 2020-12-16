from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class TestCreate():
    def setup_method(self, method):
        option=Options()
        option.debugger_address='127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(3)
        self.driver.get("http://192.1.30.186:19898/")
        self.driver.find_element_by_name('username').send_keys('mall1001')
        self.driver.find_element_by_name('password').send_keys('!QAZxsw2')
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/form/button').click()

    def teardown_method(self, method):
        self.driver.quit()

    def test_addtask(self):
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/li').click()
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div/ul/div[2]/li/ul/div[4]/a/li').click()
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[1]/form/button[3]').click()
        # self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[2]/div/div/button[1]').send_keys('c://用户/86165/桌面/线上测试导入名单.xls')
        self.driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section/div/div[3]/div/div[2]/div/div/input").send_keys("C:/Users/86185/Desktop/线上测试导入名单.xls")
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[2]/div/button[2]').click()
        # print(self.driver.current_window_handle)
        newwindow=self.driver.window_handles[-1]
        # print(newwindow)
        self.driver.switch_to.window(newwindow)
        # print(self.driver.current_window_handle)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[1]/div/div[1]/input').send_keys("任务demo1108")
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[2]/div[5]/div/label[1]').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[2]/div[7]/div/div/input').send_keys("2020-11-09 18:00")
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[1]/div/div[1]/input').send_keys("任务demo1108")
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[2]/div[5]/div/label[1]').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[2]/div[7]/div/div/input').send_keys("2020-11-09 18:00")
        # self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[2]/div[9]/div[1]/label/span[1]').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[2]/div[9]/div[1]/div/div[2]/div/div[1]/textarea').send_keys("这是一条测试消息")
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/form/div[2]/div[10]/div/button[2]').click()
