from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from time import sleep

from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_demo:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'cn.kmob.screenfingermovelock'
        desired_caps['appActivity'] = 'com.samsung.ui.FlashActivity'
        desired_caps['noReset'] = 'True'          # noReset 保留缓存， 比如登录状态
        # desired_caps["dontStopAppOnReset"] = "true"     # 不停止应用，直接运行测试用例

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_touchdemo(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,'手势密码锁').click()
        action=TouchAction(self.driver)
        action.press(x=130,y=200).wait(100).move_to(x=400,y=200).wait(100).move_to(x=670,y=200).wait(100).release().perform()  ##点击滑动
        sleep(3)
        # action1=action.tap(x=130,y=200)
        # action2=action.tap(x=670,y=200)
        # MultiAction(self.driver).add(action1).add(action2).perform()       ##多点触摸

