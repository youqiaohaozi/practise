from appium.webdriver.common.mobileby import MobileBy
from AppiumStudy.WorkWechat_PO.pages.basepage import BasePage
from AppiumStudy.WorkWechat_PO.pages.addmember import AddMember


class SelectAdd(BasePage):
    def manual_add(self):
        self.find_click((MobileBy.XPATH, "//*[@class='android.widget.TextView' and @text='手动输入添加']"))
        # 进入手动添加页面
        return AddMember(self.driver)
