from selenium.webdriver import Chrome
import random

import pytest


@pytest.fixture
def my_name():
    return 'Adrian'


@pytest.fixture(scope='session')
def random_positive_number():
    return random.randint(1, 100)


@pytest.fixture()
def driver(request):
    wd = Chrome()
    def close_driver():
        wd.quit()
    request.addfinalizer(close_driver)
    return wd

def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))
