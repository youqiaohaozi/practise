from appium.webdriver.common.mobileby import MobileBy
from AppiumStudy.WorkWechat_PO.pages.basepage import BasePage


class AddMember(BasePage):
    def add_member(self, name, gender, mobile):
        # 手动添加成员页面输入
        self.find_input((MobileBy.XPATH, "//*[contains(@text,'姓名')]/../*[@class='android.widget.EditText']"), name)   # 输入姓名
        self.find_click((MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/dux']/*"
                        "[@resource-id='com.tencent.wework:id/av2']"))
        locator = (MobileBy.XPATH, "//*[@text='女']")
        self.wait_clickable(locator, 5)    # 判断性别选择弹框是否加载完成
        self.find_click((MobileBy.XPATH, "//*[@text='"+gender+"']"))
        self.find_input((MobileBy.XPATH, "//*[@text='手机号']"), mobile)  # 输入手机号
        self.find_click((MobileBy.XPATH, "//*[@text='保存']"))
        return self.find((MobileBy.XPATH, "//*[@class='android.widget.Toast']")).text

# # 添加重复联系人失败时返回选择页
#     def back_to_select(self):
#         self.find_xpath((MobileBy.XPATH, "//*[@text='确定']")).click()
#         self.find_xpath((MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gu_']")).click()
#         self.find_xpath((MobileBy.XPATH, "//*[@text='取消']")).click()




