from appium.webdriver.common.mobileby import MobileBy
from AppiumStudy.WorkWechat_PO.pages.basepage import BasePage


class ModifyMember(BasePage):
    def modify_member(self):
        pass

    def delete_member(self):
        self.find_click((MobileBy.XPATH, "//*[@text='删除成员']"))
        self.find_click((MobileBy.XPATH, "//*[@text='确定']"))
