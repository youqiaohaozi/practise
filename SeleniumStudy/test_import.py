import shelve
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestCompanwx:

    @pytest.mark.skip
    def test_getcookies(self):
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)
        cookies = self.driver.get_cookies()
        print(cookies)

    def setup_class(self):
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850082124592'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'qnBAVqrWZKVmQRHUGbchDdIsEqWTjNcgMiX33eMfj_R-Bc9I2w-hN83YXXOfyzLXYwNuMi9HmlzEIV6NcmLSTpvhfaktWBoPKP5k24QDKJlV8AKdq7TSbIbFNgeP2-niSZJg8mzP7wRvbe2WyxH6TLYMJJtU1rHtwT073COjeQSVE-K1U38qZ5H5i-qVRuK-dCqFS4JqwJqAYPLoHO8KU5kLi5sneSSmghOmNdcDuB4Fub9tZZK_u9vVMcuQiIxyxM8eqoMFHpbXJ21WR0l_2Q'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850082124592'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324976178827'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'qHCdecijsQiEgTo8mkT85AAGBCn1CjLOKRm6UcaZbuJTlGrHt0vRxC098gTohsN7'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a5610724'},
            {'domain': '.qq.com', 'expiry': 1667964152, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1256129447.1604891473'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1633232675, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 2147483598, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': 'daf0a11d8058812f888797f4bd6fe074d4753e9562c293498181b3a134c10030'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '8290640124'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1636427471, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1604891472'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147483598, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'lazocWCiY+'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1604891472'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '4285916343671769'},
            {'domain': '.qq.com', 'expiry': 1604978552, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1174937851.1604891473'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1604923006, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': 'ecmen0'},
            {'domain': '.qq.com', 'expiry': 1604892212, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '7393802240'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1607484160, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'}]
        db = shelve.open('cookies')
        db['cookie'] = cookies
        db.close()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.close()

    def test_importcontact(self):
        db = shelve.open("cookies")
        cookies = db['cookie']
        db.close()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        self.driver.find_element_by_xpath(
            '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]/div').click()  ##点击导入用户，进入导入用户页面
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys(
            'D:/practise/通讯录批量导入模板.xlsx')
        ##检查上传文件名是否正确
        element = self.driver.find_element_by_class_name('ww_fileImporter_fileContainer_fileNames')
        import_filename = element.text
        assert import_filename == '通讯录批量导入模板.xlsx'

        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_submitWrap").click()  ##导入文件
        assert '导入成功' in self.driver.find_element_by_class_name('ww_fileImporter_successImportText').text

        self.driver.find_element_by_class_name('ww_fileImporter_successBtnWrap').click()  ##完成导入操作

        ###搜索导入用户，验证导入用户是否在通讯录列表中
        self.driver.find_element_by_id('menu_contacts').click()
        self.driver.find_element_by_id('memberSearchInput').send_keys('小李')  ##搜索用户
        assert '小李' == self.driver.find_element_by_class_name('member_display_cover_detail_name').text
