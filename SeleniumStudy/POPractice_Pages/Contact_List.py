from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from SeleniumStudy.POPractice_Pages.Add_Member import AddMember
from time import sleep

from SeleniumStudy.POPractice_Pages.base_class import BaseClass


class ContactList(BaseClass):
    # def __init__(self, driver: WebDriver):
    #     self.driver = driver


    def addmember(self):
        ##点击添加成员按钮进入添加页面
        ##处理点击一次没有响应的问题
        def wait_for_next(x: WebDriver):
            try:
                x.find_element(By.CSS_SELECTOR, ".js_add_member:nth-child(2)").click()
                return x.find_element(By.ID, "username")
            except:
                return False

        WebDriverWait(self.driver, 10).until(wait_for_next)
        return AddMember(self.driver)

    ##成员列表中查找成员是否存在
    def findmemberinlist(self, value):
        title_lists = []
        # for element in list:
        #     title_list.append(element.get_attribute('title'))
        while True:
            checkbox = (By.CSS_SELECTOR, ".ww_checkbox")
            self.wait_for_visiable(checkbox)
            list = self.elements_find(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')  ##获取联系人列表元素
            title_list = [element.get_attribute('title') for element in list]  ##取出列表中title属性值存入title_list列表中
            if value in title_list:  ##判断搜索关键字value是否在列表中，若在则返回True即查找成功
                return True
            title_lists = title_lists + title_list
            title_lists.extend(title_list)  ##若value不在列表中，把该列表加入到title_lists列表中

            pages: str = self.element_find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text  ##获取页码
            page, total = pages.split('/', 1)
            if int(page) == int(total):
                return False
            else:
                self.element_find(By.CSS_SELECTOR, '.js_next_page').click()
            ###判断是否为最后一页，若是则返回False，即所有页均为查到结果，若不是最后一页，则翻页进入下一页继续查找

    ##搜索成员
    def searchmember(self, username):
        locator = (By.CSS_SELECTOR, '#memberSearchInput')
        element = self.wait_for_visiable(locator)
        element.send_keys(username)
        ##判断是否有搜索结果
        elements = self.driver.find_elements(By.XPATH, '//*[@id="search_member_list"]/*')
        # print(elements)
        if elements == []:
            # print("没有")
            return []
        ##判断列表中是否有需要搜索的成员
        list = self.elements_find(By.CSS_SELECTOR, '.ww_searchResult_title_peopleName')
        name_list = [element.text.split('(')[0] for element in list]
        # print(name_list)
        return name_list
