import pytest
import yaml
from AppiumStudy.WorkWechat_PO.pages.app import App
from time import sleep

with open('../datas/test_data.yml', encoding='utf-8') as f:
    test_data = yaml.safe_load(f)

class TestContact:
    def setup_class(self):
        self.session = App()
        self.session.start()
        self.search_page = self.session.goto_main_page().goto_contact_list().search_member()

    def teardown_class(self):
        self.session.stop()

    @pytest.mark.parametrize("name", ['dd'])
    def test_delete_name_contains(self, name):
        result_list = self.search_page.search_namelist(name)
        print(result_list)
        for item in result_list:
            self.search_page.goto_detail(item).goto_modify().delete_member()
        result_list = self.search_page.search(name)
        assert not result_list
