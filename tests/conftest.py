import pytest, allure


def pytest_addoption(parser):
    parser.addoption('--base_url', action='store', dest='base_url')


@pytest.fixture()
def _base_url(request):
    yield request.config.getoption('base_url')
