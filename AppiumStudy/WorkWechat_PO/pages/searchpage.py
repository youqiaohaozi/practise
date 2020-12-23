from appium.webdriver.common.mobileby import MobileBy
from AppiumStudy.WorkWechat_PO.pages.basepage import BasePage
from AppiumStudy.WorkWechat_PO.pages.memberdetail import MemberDetail


class SearchPage(BasePage):
    def search(self,name):
        self.find_input((MobileBy.XPATH, "//*[@text='搜索']"), name)
        result_list = self.find_list((MobileBy.XPATH, "//*[contains(@text,'"+name+"') "
                                                 "and @class='android.widget.TextView' "
                                                 "and not(contains(@text, '网络查找手机'))]"))
        # name_list = [ele.text for ele in result_list]
        return result_list

    # 清空搜索
    def clear_search(self):
        self.find_click((MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/fk0']"))

    def find_resultlist(self, name):
        self.find((MobileBy.XPATH, "//*[contains(@text,'"+name+"') "
                                   "and @class='android.widget.TextView' "
                                   "and not(contains(@text, '网络查找手机'))]"))

    def goto_detail(self, ele):
        ele.click()
        return MemberDetail(self.driver)

