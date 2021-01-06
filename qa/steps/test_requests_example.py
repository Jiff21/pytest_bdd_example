import re
import requests
from pytest_bdd import scenario, given, when, then, parsers
from environment import context, client
from qa.settings import PAGES_DICT, FEATURE_PATH

@scenario(
    FEATURE_PATH + 'requests_example.feature',
    'Requests goes to expected page',
)
def test_publish():
    pass


@given(parsers.parse("I get {page_name} using requests"))
def get(context, client, page_name):
    context.page_name = page_name.lower()
    context.current_url = '{host}{uri}'.format(
        host=context.host,
        uri=PAGES_DICT[context.page_name]
    )
    context.response = client.get(context.current_url)
    return context.response


@then('the response should be successful')
def foo_is_foo(context, page_name):
    assert context.response.status_code is requests.codes.ok, \
        'Unexpectedly got a %d response code' % context.response.status_code
