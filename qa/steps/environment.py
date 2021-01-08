import pytest
import requests
from browser import Browser
from qa.conftest import DRIVER, IAP_ON

class Context(object):
    """An empty object to add stuff to"""

    def __init__(self):
        # self.host = 'https://example.com'
        pass


@pytest.fixture
def context(scope="module"):
    """A context for passing information between steps"""
    context = Context()
    context.host = 'https://example.com'
    return context


@pytest.fixture
def client(scope="module"):
    """Creates a requests session for use in between steps"""
    context.session = requests.Session()
    if IAP_ON is True:
        context.session.headers.update(bearer_header)
    yield context.session

@pytest.fixture
def driver(context, scope="module"):
    """Creates a Selenium Driver to use in tests"""
    browser = Browser()
    browsers = browser.return_driver_dict()
    context.driver = browsers.get(DRIVER)()
    yield context.driver
    context.driver.quit()
