
from appium import webdriver

class BasePage:
    def __init__(self,driver: webdriver=None):
        if driver=None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = '127.0.0.1:7555'
            desired_caps['appPackage'] = 'com.xueqiu.android'
            desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
            desired_caps['noReset'] = 'True'
            # 不停止应用，直接运行测试用例(多条用例或者运行多次时，需要返回，否则下一条用例可能无法执行)
            # desired_caps["dontStopAppOnReset"] = "true"
            # desired_caps['skipDeviceInitialization'] = 'true'
            # desired_caps['skipServerInstallation'] = 'true'
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver=driver

    def find(self,locator):
        return self.driver.find_element(locator)
