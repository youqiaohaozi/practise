from AppiumStudy.frame.pages.basepage import BasePage


class Search(BasePage):
    def search(self):
        # self.driver.find_element(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/search_input_text"]').send_keys("阿里巴巴")
        self.prase_yaml("../datas/search.yaml", "search")