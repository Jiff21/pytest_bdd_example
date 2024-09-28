import requests
from functools import partial
from pytest_bdd import scenario, given, when, then, parsers, scenarios
from qa.settings import PAGES_DICT
from qa.tests.environment import context, client


# Set file path here in case you have multiple scenarios.
# Part of path set in pytest.ini.
# scenario = partial(scenario, 'features/requests_example.feature')
# @scenario('Requests receives a success message')
# def test_requests():
#     pass

#
# @scenario('features/requests_example.feature', 'Requests receives a success message')
# def test_requests():
#     print('starting bdd test')


@given(parsers.parse("I get the {page_name} page using requests"))
@when(parsers.parse("I get the {page_name} page using requests"))
def get_with_requets(context, client, page_name):
    context.current_url = context.human_readable_pages(page_name, context.host)
    context.response = client.get(context.current_url)
    return context.response


@then('the response should be successful')
def response_succeeded(context):
    assert context.response.status_code is requests.codes.ok, \
        'Unexpectedly got a %d response code' % context.response.status_code
