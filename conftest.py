import pytest

@pytest.fixture()            # 不带参数时默认scope="function"
def login():
    print("输入账号，密码先登录")


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )

@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")