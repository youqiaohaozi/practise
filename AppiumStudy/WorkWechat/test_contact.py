
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class Test_WorkWechat:
    def setup_class(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
        desired_caps['noReset'] = 'True'
        # 不停止应用，直接运行测试用例(多条用例或者运行多次时，需要返回，否则下一条用例可能无法执行)
        desired_caps["dontStopAppOnReset"] = "true"
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['skipServerInstallation'] = 'true'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.back()

    def teardown_class(self):
        self.driver.quit()

###添加联系人
    def test_addcontact(self):
        ##进入通讯录页面
        name='手机新增成员5'
        gender='女'
        mobile='13910000005'

        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/dqn' and @text='通讯录']").click()

        ##点击添加成员进入添加页面，由于当通讯录列表人数较多时，添加成员入口需要下拉才会显示，所以此处使用滚动查找
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                               'scrollable(true).instance(0)).'
                                                               'scrollIntoView(new UiSelector().'
                                                               'text("添加成员").instance(0));').click()

        self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.TextView' and @text='手动输入添加']").click()  ##进入手动添加页面

        ###手动添加成员页面输入
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'姓名')]/../*[@class='android.widget.EditText']").send_keys(name)       ###输入姓名

        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/dux']/*[@resource-id='com.tencent.wework:id/av2']").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((MobileBy.XPATH, "//*[@text='女']")))       ##判断性别选择弹框是否加载完成

        # if gender=='女':
        #     self.driver.find_element(MobileBy.XPATH,"//*[@text='女']").click()
        # else:
        #     self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()

        self.driver.find_element(MobileBy.XPATH, "//*[@text='"+gender+"']").click()

        self.driver.find_element(MobileBy.XPATH,"//*[@text='手机号']").send_keys(mobile)       ##输入手机号

        self.driver.find_element(MobileBy.XPATH,"//*[@text='保存']").click()

        # sleep(2)
        # print(self.driver.page_source)     ##获取页面属性，从而找到toast元素的属性用于查找

        result=self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.Toast']").text

        assert '添加成功' in result

    def test_deletecontact(self):
        ##进入通讯录页面
        delete_contact='手机新增成员5'
        ##1.滑动屏幕查找用户
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/dqn' and @text='通讯录']").click()
        # ele1=WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
        #                                                        'scrollable(true).instance(0)).'
        #                                                        'scrollIntoView(new UiSelector().'
        #                                                        'text("'+delete_contact+'").instance(0));')))
        # ele1.click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                               'scrollable(true).instance(0)).'
                                                               'scrollIntoView(new UiSelector().'
                                                               'text("'+delete_contact+'").instance(0));').click()

        ##2.通过搜索联系人找到联系人并操作
        # self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/guu']").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys(delete_contact)
        # self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.TextView' and @text='"+delete_contact+"']").click()
        #
        #删除用户
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/guk']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='编辑成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='删除成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()

        ##验证用户是否删除
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/guu']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys(delete_contact)
        source=self.driver.page_source
        assert "联系人" not in source
