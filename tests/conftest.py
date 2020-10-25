from utils.driver_factory import DriverFactory
import config
import pytest

d = DriverFactory()

@pytest.fixture(scope='session', autouse=True)
def driver(request, browser):
    _driver = d.launch_driver(browser)
    d.launch_url(_driver, config.url)

    def tear_down():
        d.quit_driver(_driver)
    request.addfinalizer(tear_down)
    return _driver

@pytest.fixture(scope='session', autouse=True)
def browser(request):
    """
    Use the command line argument as a fixture function
    :param request:
    :return: --browser (command line option)
    """
    return request.config.getoption("--browser")

def pytest_addoption(parser):
    """
    Get the desired browser from command line arguments
    :param parser:
    :return: None
    """
    parser.addoption("--browser", action="store", default="chrome", help="browser: chrome or firefox")
