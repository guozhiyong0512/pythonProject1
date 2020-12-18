import  pytest
from pythoncode.calculator import Calculator


@pytest.fixture(scope="module")
def myfixture():
    calc = Calculator()
    print("开始计算")
    yield  calc
    print("结束计算")