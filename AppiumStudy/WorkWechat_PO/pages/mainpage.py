from appium.webdriver.common.mobileby import MobileBy
from AppiumStudy.WorkWechat_PO.pages.basepage import BasePage
from AppiumStudy.WorkWechat_PO.pages.contactpage import ContactPage


class MainPage(BasePage):
    def goto_contact_list(self):
        self.find_xpath((MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/dqn' and @text='通讯录']")).click()
        return ContactPage(self.driver)

    def goto_work_desk(self):
        pass

    def goto_mine(self):
        pass
