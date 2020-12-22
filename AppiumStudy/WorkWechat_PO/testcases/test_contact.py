from selenium.common.exceptions import NoSuchElementException

from AppiumStudy.WorkWechat_PO.pages.app import App

class TestContact:
    def setup_class(self):
        self.session = App()
        self.session.start()
        self.contact_page = self.session.goto_main_page().goto_contact_list()

    def teardown_class(self):
        self.session.stop()

    def teardown(self):
        self.session.back()

    def test_add(self):
        toast = self.contact_page.add_member().manual_add().add_member('测试122202', '女', '12220000002')
        assert '添加成功' in toast

    def test_delete(self):
        self.contact_page.goto_member_detail('测试122202').goto_modify().delete_member()
        source = self.contact_page.search_member('测试122202')
        assert '联系人' not in source
