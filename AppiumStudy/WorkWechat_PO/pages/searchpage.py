from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from AppiumStudy.WorkWechat_PO.pages.basepage import BasePage
from AppiumStudy.WorkWechat_PO.pages.memberdetail import MemberDetail


class SearchPage(BasePage):
    def search(self,name):
        self.find_input((MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/fk1']"), name)
        result_list = self.find_list((MobileBy.XPATH, "//*[contains(@text,'"+name+"') "
                                                 "and @class='android.widget.TextView' "
                                                 "and not(contains(@text, '网络查找手机'))]"))
        return result_list
    # def search_list(self,name):
    #     self.find_input((MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/fk1']"), name)
    #     result_list = self.find_list((MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/bid' and @text='黑路白霜渝北店']"))
    #     return result_list

    # 清空搜索
    def clear_search(self):
        self.find_click((MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/fk0']"))

    def search_namelist(self, name):
        self.find_input((MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/fk1']"), name)
        result_list = self.find_list((MobileBy.XPATH, "//*[contains(@text,'"+name+"') "
                                                 "and @class='android.widget.TextView' "
                                                 "and not(contains(@text, '网络查找手机'))]"))
        name_list = [ele.text for ele in result_list]
        return name_list

    # 搜索结果列表中查看联系人
    def goto_detail(self, name):
        ele: WebElement = self.wait_clickable((MobileBy.XPATH, "//*[@text='"+name+"']"))
        ele.click()
        return MemberDetail(self.driver)

