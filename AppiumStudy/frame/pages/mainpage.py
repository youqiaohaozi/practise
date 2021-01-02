from AppiumStudy.frame.pages.basepage import BasePage
from AppiumStudy.frame.pages.homepage import MyHome
from AppiumStudy.frame.pages.marketpage import MarketPage
from AppiumStudy.frame.pages.tradepage import Trade


class MainPage(BasePage):
    def goto_market(self):
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='行情']").click()
        self.prase_yaml("../datas/main.yaml", "goto_market")
        return MarketPage(self.driver)

    def goto_trade(self):
        self.prase_yaml("../datas/main.yaml", "goto_trade")
        return Trade(self.driver)

    def goto_myhome(self):
        self.prase_yaml("../datas/main.yaml", "goto_mine")
        return MyHome(self.driver)