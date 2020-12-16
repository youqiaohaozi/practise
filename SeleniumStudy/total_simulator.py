from selenium.webdriver.common.by import By

from SeleniumStudy.POPractice_Pages.base_class import BaseClass


class TotalCalculator(BaseClass):
    base_url = 'http://172.30.37.124/#/business/receivable/dealCheck'

    def total_calculator(self):
        ##输入查询条件进行查询
        element=self.element_find(By.XPATH,"//*[@id='app']/div/div[2]/section/div/div[1]/form/div[1]/div/section/div/div[1]/input")
        String
        jsString = "document.getElementById('app').firstChild.thirdChild.removeAttribute('readonly')";
        JavascriptExecutor
        js = (JavascriptExecutor)
        driver;
        js.executeScript(jsString);




        element.sendkeys("1004")
        elements=self.elements_find(By.CSS_SELECTOR,"el-range-input")
        elements[0].text="2020-11-01"
        elements[1].text = "2020-11-30"
        self.element_find(By.CSS_SELECTOR,".el-button--small").click()

        self.wait_for_visiable((By.ID,"el-collapse-head-6153"))

        ##统计
        # self.
        # list

