# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from SeleniumStudy.POPractice_Pages.Add_Member import AddMember
from SeleniumStudy.POPractice_Pages.Contact_List import ContactList
from SeleniumStudy.POPractice_Pages.base_class import BaseClass


class HomePage(BaseClass):
    base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    # def __init__(self):
    #     options=Options()
    #     options.debugger_address='127.0.0.1:9222'
    #     self.driver=webdriver.Chrome(options=options)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def goto_contactlist(self):
        self.element_find(By.CSS_SELECTOR, '#menu_contacts').click()
        return ContactList(self.driver)

    def goto_addmember(self):
        ##点击首页添加成员按钮，进入添加页面
        self.element_find(By.CSS_SELECTOR, '.index_service_cnt_item_title:nth_child(1)').click()
        return AddMember(self.driver)
