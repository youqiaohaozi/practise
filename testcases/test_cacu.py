import pytest

from pythoncode.caculator import Calculator


class TestCalc:
    @pytest.mark.parametrize('a,b,expect',
                             [[1, 1, 2], [10, 10, 15], [-1, -2, 3], [-1, 2, 1], [0.5, 0.7, 1], [0.2, 0.3, 0.5]],
                             ids=["positives", "positive1", "nagetives", "positive+nagetive", "floats", "floats1"])
    def test_add(self, a, b, expect):
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect',
                             [[0.5, 0.7, 1], [0.2, 0.3, 0.5]],
                             ids=["floats", "floats1"])
    def test_add_float(self, a, b, expect):
        result = self.calc.add(a, b)
        assert round(result, 2) == expect


    @pytest.mark.parametrize('a,b,expect',
                             [[1, 1, 1], [10, -2, -5], [-2, -1, 2], [3, 2, 1.5], [0.7, 0.2, 3.5], [0.3, 0.15, 2]],
                             ids=["positives", "pos/nage", "nagetives", "expectfloat", "floats", "expectpositive"])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a,b', [[0.1, 0], [10, 0], [1, 1]])
    def test_div_zero(self, a, b):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(a, b)

    def setup_class(self):
        print("开始验证计算结果正确性")
        self.calc = Calculator()

    def teardown_class(self):
        print("全部计算结果验证完成")

    def setup(self):
        print("验证开始")

    def teardown(self):
        print("验证结束")


if __name__ == '__main__':
    pytest.main(['-vs', 'test_cacu.py'])
