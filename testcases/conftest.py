import pytest


@pytest.fixture()
def setprint():
    print("开始计算")
    yield
    print("计算结束")


@pytest.fixture(scope='module')
def fristofall():
    print("全部开始")
    yield
    print("全部结束")
