import re
import requests
from environment import context, driver
from functools import partial
from pytest_bdd import scenario, given, when, then, parsers
from qa.conftest import PAGES_DICT

# Set file path here in case you have multiple scenarios.
# Part of path set in pytest.ini.
scenario = partial(scenario, 'browser_example.feature')
@scenario('Browser can get correct page')
def test_browser():
    pass


@given(parsers.parse("I get the {page_name} page"))
@when(parsers.parse("I get the {page_name} page"))
def get(context, driver, page_name):
    context.page_name = page_name.lower()
    context.current_url = '{host}{uri}'.format(
        host=context.host,
        uri=PAGES_DICT[context.page_name]
    )
    context.driver.get(context.current_url)

@then(parsers.parse('I should be on {expected_page}'))
def assert_page(context, driver, expected_page):
    assert context.host in context.driver.current_url, \
    'expected {expected_host} to be in {current_host}'.format(
        expected_host=context.host,
        current_host=context.driver.current_url
    )
