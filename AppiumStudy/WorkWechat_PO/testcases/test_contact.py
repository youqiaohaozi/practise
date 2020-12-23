import pytest
import yaml
from AppiumStudy.WorkWechat_PO.pages.app import App

with open('../datas/test_data.yml', encoding='utf-8') as f:
    test_data=yaml.safe_load(f)

class TestContact:
    def setup_class(self):
        self.session = App()
        self.session.start()
        self.contact_page = self.session.goto_main_page().goto_contact_list()

    def teardown_class(self):
        self.session.stop()

    def teardown(self):
        self.session.back()

    @pytest.mark.skip
    @pytest.mark.parametrize('name,gender,mobile', test_data['addmember_list'])
    def test_add(self,name,gender,mobile):
        toast = self.contact_page.add_member().manual_add().add_member(name, gender, mobile)
        assert '添加成功' in toast

    # @pytest.mark.skip
    @pytest.mark.parametrize('name', test_data['deletemember_list'])
    def test_delete(self, name):
        self.contact_page.goto_member_detail(name).goto_modify().delete_member()
        result_list = self.contact_page.search_member().search(name)
        assert not result_list
        self.session.back()




