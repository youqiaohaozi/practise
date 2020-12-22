from appium.webdriver.common.mobileby import MobileBy
from AppiumStudy.WorkWechat_PO.pages.basepage import BasePage
from AppiumStudy.WorkWechat_PO.pages.modifymember import ModifyMember


class MemberDetail(BasePage):
    def goto_modify(self):
        self.find_xpath((MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/guk']")).click()
        self.find_xpath((MobileBy.XPATH, "//*[@text='编辑成员']")).click()
        return ModifyMember(self.driver)
