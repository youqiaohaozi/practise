from SeleniumStudy.total_simulator import TotalCalculator


class TestCal:
    def setup(self):
        self.index=TotalCalculator()

    def test_calculator(self):
        self.index.total_calculator()
