# -*- coding: UTF-8 -*-
# Redifining context: pylint: disable=W0621
# Using context to pass functions: pylint: disable=R0201

'''Test setup done with fixtures here per pytest-bdd docs'''
import pytest
import requests
from selenium.webdriver.support.ui import WebDriverWait
from qa.tests.steps.workarounds import LocalStorage
from qa.settings import DRIVER, IAP_ON, PAGES_DICT, HOST_URL
from qa.tests.browser import Browser

class Context():
    """An empty object to add stuff to"""

    def __init__(self):
        self.host = HOST_URL
        self.current_url = None

    def human_readable_pages(self, name, host):
        '''Allow homan readable names for url in .feature files'''
        name = name.lower()
        self.current_url = '{host}{uri}'.format(
            host=host,
            uri=PAGES_DICT[name]
        )
        return self.current_url

    def dismiss_cookie_consent(self, driver):
        '''Dismiss Cookie Consent to local storage'''
        local_storage = LocalStorage(driver)
        local_storage.set('cookieConsent', '{"Ha":true}')

    def clear_local_storage(self, driver):
        '''Clear local storage'''
        local_storage = LocalStorage(driver)
        local_storage.clear()


@pytest.fixture
def context(scope="module"): # pylint: disable=W0613
    """A context for passing information between steps"""
    context = Context()
    return context


@pytest.fixture
def client(scope="module"): # pylint: disable=W0613
    """Creates a requests session for use in between steps"""
    context.session = requests.Session()
    if IAP_ON is True:
        pass
        # context.session.headers.update(bearer_header)
    yield context.session


@pytest.fixture
def driver(context, scope="module"): # pylint: disable=W0613
    """Creates a Selenium Driver to use in tests"""
    browser = Browser()
    browsers = browser.return_driver_dict()
    context.driver = browsers.get(DRIVER)()
    # Setup a default wait
    context.wait = WebDriverWait(context.driver, 10, 0.1)
    context.driver.get(HOST_URL)
    context.dismiss_cookie_consent(context.driver)
    yield context.driver
    context.driver.quit()
