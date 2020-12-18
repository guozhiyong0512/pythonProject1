import pytest
import yaml


@pytest.mark.parametrize("a,b,expect", yaml.safe_load(open("datas.yml"))["datas"],
                         ids=yaml.safe_load(open("datas.yml"))["myids"])
class TestCalc:

    @pytest.mark.demo
    @pytest.mark.run(order=2)
    def test_add(self, a, b, expect, myfixture):
        print("++++++++++++++", myfixture)
        pytest.assume(1 == 1)
        pytest.assume(expect == myfixture.add(a, b))

    @pytest.mark.demo
    @pytest.mark.run(order=1)
    def test_sub(self, a, b, expect, myfixture):
        assert expect == myfixture.sub(a, b)

    @pytest.mark.demo
    @pytest.mark.smoke
    @pytest.mark.run(order=4)
    def test_mul(self, a, b, expect, myfixture):
        assert expect == myfixture.mul(a, b)

    @pytest.mark.smoke
    @pytest.mark.run(order=3)
    @pytest.mark.flaky(reruns=1, delay=1)
    def test_adiv(self, a, b, expect, myfixture):
        assert expect == myfixture.div(a, b)
