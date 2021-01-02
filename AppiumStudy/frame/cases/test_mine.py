from AppiumStudy.frame.pages.app import App


class TestMine:
    def test_setting(self):
        self.session = App()
        self.session.start()