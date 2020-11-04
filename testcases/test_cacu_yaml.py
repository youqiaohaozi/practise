import pytest
import yaml
from pythoncode.caculator import Calculator


class GetDatas:
    def __init__(self, filename):
        self.filename = filename

    def get_datas(self):
        with open(self.filename, encoding='utf-8') as f:
            datas = yaml.safe_load(f)
        return datas


class TestCalc:
    calc = Calculator()
    f = GetDatas("./data/data.yml")
    datas = f.get_datas()

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,expect', datas['add']['datas'], ids=datas['add']['ids'])
    def test_add(self, setprint, fristofall, a, b, expect):
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a,b,expect', datas['div']['datas'], ids=datas['div']['ids'])
    def test_div(self, setprint, a, b, expect):
        result = self.calc.div(a, b)
        assert round(result, 2) == expect

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,expect', datas['sub']['datas'], ids=datas['sub']['ids'])
    def test_sub(self, setprint, a, b, expect):
        # calc = Calculator()
        result = self.calc.sub(a, b)
        assert round(result, 2) == expect

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a,b,expect', datas['mul']['datas'], ids=datas['mul']['ids'])
    def test_mul(self, setprint, a, b, expect):
        # calc = Calculator()
        result = self.calc.mul(a, b)
        assert round(result, 2) == expect


if __name__ == '__main__':
    pytest.main(['-vs', 'test_cacu_yaml.py'])
