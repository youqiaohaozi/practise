from appium.webdriver.common.mobileby import MobileBy
from AppiumStudy.WorkWechat_PO.pages.basepage import BasePage
from AppiumStudy.WorkWechat_PO.pages.memberdetail import MemberDetail
from AppiumStudy.WorkWechat_PO.pages.selectadd import SelectAdd


class ContactPage(BasePage):
    def add_member(self):
        self.find_scroll("添加成员")
        return SelectAdd(self.driver)

    def search_member(self, name):
        self.find_xpath((MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/guu']")).click()
        self.find_xpath((MobileBy.XPATH, "//*[@text='搜索']")).send_keys(name)
        return self.driver.page_source

    def goto_member_detail(self, name):
        self.find_scroll(name)
        return MemberDetail(self.driver)
