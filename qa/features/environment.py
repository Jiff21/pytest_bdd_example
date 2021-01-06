import pytest
import requests
from browser import Browser
from qa.settings import DRIVER, IAP_ON

class Context(object):
    """A context for passing information between steps"""

    def __init__(self):
        # self.host = 'https://example.com'
        pass


@pytest.fixture
def context(scope="module"):
    context = Context()
    context.host = 'https://example.com'
    return context


@pytest.fixture
def client(scope="module"):
    client = requests.Session()
    if IAP_ON is True:
        client.headers.update(bearer_header)
    return client


@pytest.fixture
def driver(context, scope="module"):
    browser = Browser()
    browsers = browser.return_driver_dict()
    context.driver = browsers.get(DRIVER)()
    yield
    context.driver.quit()
    # return context
