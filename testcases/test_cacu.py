import pytest

from pythoncode.caculator import Calculator


class TestCalc:
    @pytest.mark.parametrize('a,b,expect',
                             [[1, 1, 2], [10, 10, 15], [-1, -2, 3], [-1, 2, 1], [0.5, 0.7, 1], [0.2, 0.3, 0.5]],
                             ids=["positives", "positive1", "nagetives", "positive+nagetive", "floats", "floats1"])
    def test_add(self, a, b, expect):
        calc = Calculator()
        result = calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect',
                             [[1, 1, 1], [10, -2, -5], [-2, -1, 2], [3, 2, 1.5], [0.7, 0.2, 3.5], [0.3, 0.15, 2]],
                             ids=["positives", "pos/nage", "nagetives", "expectfloat", "floats", "expectpositive"])
    def test_div(self, a, b, expect):
        calc = Calculator()
        result = calc.div(a, b)
        assert result == expect

    def setup_class(self):
        print("开始验证计算结果正确性")

    def teardown_class(self):
        print("全部计算结果验证完成")

    def setup(self):
        print("验证开始")

    def teardown(self):
        print("验证结束")


if __name__ == '__main__':
    pytest.main(['-s -v', 'test_cacu.py'])
