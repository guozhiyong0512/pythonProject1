import pytest
from pythoncode.calculator import Calculator


@pytest.fixture(scope="module")
def myfixture():
    print("fixture执行开始")
    calc = Calculator()
    print("=========", calc)
    yield calc

    print("fixture执行结束")
