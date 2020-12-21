from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_WorkWechat:
    def setup(self):
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
        # desired_caps["settings[waitForIdleTimeout]"] = 0    ###不需要控件加载完成，该参数可定义成全局参数或局部参数

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()


    def test_daka(self):
        ##进入工作台页面
        # ele=WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/dqk"]//*[@text="工作台"]')))
        ele = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/dqn" and @text="工作台"]')))
        ele.click()

        ##滚动滑动屏幕，查到打卡并进入打卡页面
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("打卡").instance(0));').click()



        # 1. 选择外出打卡
        # 2. 进行打卡
        self.driver.update_settings({"waitForIdleTimeout": 0})
        self.driver.find_element(MobileBy.XPATH,"//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'次外出')]").click()
        result=WebDriverWait(self.driver,10).until(lambda x:'打卡成功' in x.page_source)
        print(result)
        assert result