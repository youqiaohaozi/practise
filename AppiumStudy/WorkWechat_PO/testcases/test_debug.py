from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from time import sleep


class TestDebug:
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

    def teardown_class(self):
        self.driver.quit()

    def test_debug(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/dqn' and @text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/guu']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys("12")
        result_list = self.driver.find_elements(MobileBy.XPATH, "//*[contains(@text,'12') "
                                                 "and @class='android.widget.TextView' "
                                                 "and not(contains(@text, '网络查找手机'))]")
        # act = self.driver.current_activity
        print(result_list)
        for ele in result_list:
            # self.driver.wait_activity(act, 10)
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/d2f']")))
            ele.click()
            # self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/gu_']").click()
            self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/guk']").click()
            self.driver.find_element(MobileBy.XPATH,"//*[@text='编辑成员']").click()
            self.driver.find_element(MobileBy.XPATH, "//*[@text='删除成员']").click()
            self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()