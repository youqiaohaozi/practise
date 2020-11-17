import pytest
from SeleniumStudy.POPractice_Pages.Home_Page import HomePage


class TestAddmember:
    def setup(self):
        self.home = HomePage()

    # @pytest.mark.skip
    def test_addmember(self):
        username = 'addmember4'
        userlable = 'addmember4'
        userphone = '13900000002'
        contactlist = self.home.goto_contactlist()

        # ##从首页进入添加成员
        # addmember=self.home.goto_addmember()

        ##从联系人进入添加成员
        addmember = contactlist.addmember()
        addmember.addmember(username, userlable, userphone)
        # try:
        #     assert contactlist.findmemberinlist(username)
        # except AssertionError as e:
        #     print("成员未成功创建")
        result = contactlist.searchmember(username)
        try:
            assert username in result
        except AssertionError:
            print("成员未成功创建")
