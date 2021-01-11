import pytest
import requests
from qa.settings import DRIVER, IAP_ON, PAGES_DICT, HOST_URL
from selenium.webdriver.support.ui import WebDriverWait
from qa.steps.browser import Browser

class Context(object):
    """An empty object to add stuff to"""

    def __init__(self):
        self.host = HOST_URL
        print(self.host)
        # pass

    def human_readable_pages(self, name, host):
        '''Allow homan readable names for url in .feature files'''
        name = name.lower()
        current_url = '{host}{uri}'.format(
            host=host,
            uri=PAGES_DICT[name]
        )
        return current_url


@pytest.fixture
def context(scope="module"):
    """A context for passing information between steps"""
    context = Context()
    # context.host = HOST_URL
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
    # Setup a default wait
    context.wait = WebDriverWait(context.driver, 10, 0.1)
    yield context.driver
    context.driver.quit()
