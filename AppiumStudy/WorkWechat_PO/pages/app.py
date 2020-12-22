from AppiumStudy.WorkWechat_PO.pages.mainpage import MainPage
from AppiumStudy.WorkWechat_PO.pages.basepage import BasePage
from appium import webdriver

class App(BasePage):
    def start(self):      ##启动APP
        if self.driver is None:
            desired_caps = {'platformName': 'Android', 'platformVersion': '6.0', 'deviceName': '127.0.0.1:7555',
                            'appPackage': 'com.tencent.wework', 'appActivity': '.launch.LaunchSplashActivity',
                            'noReset': 'True', "dontStopAppOnReset": "true", 'skipDeviceInitialization': 'true',
                            'skipServerInstallation': 'true'}

            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(3)
        else:
            self.driver.launch_app()

    def restart(self):          ##重启APP
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):         ##退出APP
        self.driver.quit()

    def goto_main_page(self):           ###进入首页
        return MainPage(self.driver)

    def back(self):    ###返回上一页
        self.driver.back()