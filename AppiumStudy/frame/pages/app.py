from appium import webdriver
from AppiumStudy.frame.pages.basepage import BasePage
from AppiumStudy.frame.pages.mainpage import MainPage


class App(BasePage):

    def start(self):
        if self.driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["noReset"] = "true"
            caps["deviceName"] = "127.0.0.1:7555"
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(5)

    def stop(self):
        self.driver.quit()

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def back(self):
        self.driver.back()

    def goto_mainpage(self):
        return MainPage(self.driver)