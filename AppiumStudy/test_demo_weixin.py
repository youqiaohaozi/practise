from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_demo:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.tencent.mm'
        desired_caps['appActivity'] = '.ui.LauncherUI'
        desired_caps['noReset'] = 'True'          # noReset 保留缓存， 比如登录状态
        # desired_caps["dontStopAppOnReset"] = "true"     # 不停止应用，直接运行测试用例

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_findsomeone(self):
        '''
        1.进入微信通信录
        2.进入公众号列表
        3.滑动查找腾讯课堂，并进入公众号
        '''
        ele=WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((MobileBy.XPATH,"//*[@text='通讯录']")))
        ele.click()           ##进入通讯录页面

        self.driver.find_element(MobileBy.XPATH,"//*[@text='公众号']").click()         ##进入公众号列表页

        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("腾讯课堂").instance(0));').click()           ###滑动查找指定公众号，点击进入
        sleep(3)