import yaml
from AppiumStudy.WorkWechat_PO.pages.mainpage import MainPage
from AppiumStudy.WorkWechat_PO.pages.basepage import BasePage
from appium import webdriver

with open('../datas/base_data.yml') as f:
    myconfig = yaml.safe_load(f)
    desired_caps = myconfig['desirecaps']
    ip = myconfig['server']['ip']
    port = myconfig['server']['port']


class App(BasePage):
    def start(self):      ##启动APP
        if self.driver is None:
            self.driver = webdriver.Remote('http://'+ip+':'+port+'/wd/hub', desired_caps)
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