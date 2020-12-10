import pytest
from pythoncode.calculator import Calculator


@pytest.mark.parametrize("a,b,expect", [
    (3, 5, 8), (-1, -2, -3), (100, 300, 400)
], ids=["int", "minus", "bigint"])
class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    def test_sub(self, a, b, expect):
        assert expect == self.calc.sub(a, b)

    def test_mul(self, a, b, expect):
        assert expect == self.calc.mul(a, b)

    def test_adiv(self, a, b, expect):
        assert expect == self.calc.div(a, b)
