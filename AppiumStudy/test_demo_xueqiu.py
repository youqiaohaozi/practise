from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class Test_demo:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['noReset'] = 'True'
        # 不停止应用，直接运行测试用例(多条用例或者运行多次时，需要返回，否则下一条用例可能无法执行)
        desired_caps["dontStopAppOnReset"] = "true"
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['skipServerInstallation'] = 'true'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()


    def test_search(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/listview']//*[@text='阿里巴巴']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/title_container']//*[@text='股票']").click()

        price=self.driver.find_element(MobileBy.XPATH,"//*[@text='BABA']/../../following-sibling::*[1]/*[1]").text
        print(price)
        assert float(price) >250