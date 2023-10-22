'''Common steps imported into conftest.py'''

from functools import partial
from pytest_bdd import given, when, then, parsers
from qa.tests.environment import context, driver
from qa.tests.steps.custom_exceptions import loop_thru_messages
from qa.settings import PAGES_DICT


@given(parsers.parse("I get the {page_name} page"))
@when(parsers.parse("I get the {page_name} page"))
def get(context, driver, page_name):
    context.current_url = context.human_readable_pages(page_name, context.host)
    context.driver.get(context.current_url)


@then(parsers.parse('I should be on {expected_page}'))
def assert_page(context, driver, expected_page):
    assert context.host in context.driver.current_url, \
    'expected {expected_host} to be in {current_host}'.format(
        expected_host=context.host,
        current_host=context.driver.current_url
    )


@when('I check the console logs')
def check_console(context, driver):
    context.console_errors = []
    for entry in context.driver.get_log('browser'):
        try:
            assert "SEVERE" not in entry['level']
        except AssertionError:
            context.console_errors.append(
                "On Page: %s. Expeced no errors in log instead got:\n%s" % (
                    context.current_url,
                    str(entry)
                )
            )


@then('there should be no severe console log errors')
def check_no_severe_errors(context, driver):
    assert len(context.console_errors) == 0, loop_thru_messages(context.console_errors)
