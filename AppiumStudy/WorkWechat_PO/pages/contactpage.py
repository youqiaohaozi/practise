from appium.webdriver.common.mobileby import MobileBy
from AppiumStudy.WorkWechat_PO.pages.basepage import BasePage
from AppiumStudy.WorkWechat_PO.pages.memberdetail import MemberDetail
from AppiumStudy.WorkWechat_PO.pages.searchpage import SearchPage
from AppiumStudy.WorkWechat_PO.pages.selectadd import SelectAdd


class ContactPage(BasePage):
    def add_member(self):
        self.find_scroll("添加成员")
        return SelectAdd(self.driver)

    def search_member(self):
        self.find_click((MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/guu']"))
        return SearchPage(self.driver)

    def goto_member_detail(self, name):
        self.find_scroll(name)
        return MemberDetail(self.driver)

