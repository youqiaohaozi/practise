from AppiumStudy.frame.pages.app import App


class TestMarket:
    def test_search(self):
        self.session = App()
        self.session.start()
        self.market = self.session.goto_mainpage().goto_market()
        self.market.goto_search().search()
