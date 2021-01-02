from AppiumStudy.frame.pages.basepage import BasePage
from AppiumStudy.frame.pages.search import Search


class MarketPage(BasePage):
    def goto_search(self):
        # self.find((By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']")).click()
        self.prase_yaml("../datas/market.yaml", "goto_search")
        return Search(self.driver)