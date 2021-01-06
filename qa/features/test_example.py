import re
import requests
from pytest_bdd import scenario, given, when, then, parsers

@scenario(
    'example.feature',
    'Test given fixture injection',
)
def test_publish():
    pass


# @given('I get <page_name> with requests session')
# def get(page_name):
#     print('Getting this url with reqests %s' % page_name)
    # page_name = page_name.lower()
    # current_url = 'https://example.com/{0}'.format(page_name)
    # print('Getting this url with reqests %s' % page_name)
    # response = session.get(current_url)
    # assert response.status_code is requests.codes.ok, \
    # ' Unexpectedly got a %d response code' % context.response.status_code



# @pytest.fixture
# def foo():
    # return "foo"


@given(parsers.parse("I get the {page_name} page"), target_fixture="foo")
def get(page_name):
    return page_name


@then('foo should be "injected foo"')
def foo_is_foo(foo):
    assert foo == 'injected foo'
