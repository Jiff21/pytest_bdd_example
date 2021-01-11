import requests
from functools import partial
from pytest_bdd import scenario, given, when, then, parsers, scenarios
from qa.settings import PAGES_DICT
from qa.tests.environment import context, client


# Set file path here in case you have multiple scenarios.
# Part of path set in pytest.ini.
scenario = partial(scenario, 'requests_example.feature')
@scenario('Requests goes to expected page')
def test_requests():
    pass


@given(parsers.parse("I get {page_name} using requests"))
def get(context, client, page_name):
    context.current_url = context.human_readable_pages(page_name, context.host)
    context.response = client.get(context.current_url)
    return context.response


@then('the response should be successful')
def foo_is_foo(context, page_name):
    assert context.response.status_code is requests.codes.ok, \
        'Unexpectedly got a %d response code' % context.response.status_code
