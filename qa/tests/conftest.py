'''Using Conftest.py as as the behave equivalent of common.py'''
# Import all common steps from the step folder here:
import pytest
import requests
from pytest_bdd import scenario, given, when, then, parsers, scenarios
from qa.tests.steps.accessiblity import *
from qa.settings import PAGES_DICT
from qa.tests.environment import context, client, driver
from qa.tests.steps.custom_exceptions import loop_thru_messages
# see qa/setting.py for setup


def pytest_bdd_apply_tag(tag, function):
    # Skip tests with known bugs.
    if 'KEY-' in tag:
        reason_string = "Skipping due to known issue {}".format(tag)
        marker = pytest.mark.skip(reason=reason_string)
        marker(function)
        return True
    else:
        # Fall back to the default behavior of pytest-bdd
        return None

class Style():
  RED = "\033[31m"
  RESET = "\033[0m"

############
# Test Hooks
############

def pytest_sessionstart(session):
    print('\nBefore All Hook:\n')


def pytest_sessionfinish(session, exitstatus):
    print('\nAfter All Hook:\n')


# Before and After Feature Hooks
@pytest.fixture(scope="module", autouse=True)
def after_feature_teardown(request):
    print("\nBefore Feature Hook...\n")
    yield True
    print("\nAfter Feature Hook...\n")


# Before Scanrio Hook
def pytest_bdd_before_scenario(request, feature, scenario):
    print('\nBefore Scenario Hook\n')
    # Print Scenario as it runs
    print('\n\nScenario: {scenario.name}'.format(scenario=scenario))


# After Scenario Hook
def pytest_bdd_after_scenario(request, feature, scenario):
    print('\nAfter Scenario Hook\n')

# Before Step Hook
def pytest_bdd_before_step(request, feature, scenario, step, step_func):
    # Print steps as they run
    print('    {step.keyword} {step.name}'.format(keyword=step.keyword, step=step), end="", flush=True)


# After step passed or skipping hook
def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    # Logic for live print if step passed
    print(' - PASSED')

# After step failed hook
def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    # Logic for live print if step failed or not
    print(f'{Style.RED} - FAILED{Style.RESET}')


##############
# Shared Steps
##############



@given(parsers.parse("I get the {page_name} using requests"))
@when(parsers.parse("I get the {page_name} using requests"))
def get_with_requests(context, client, page_name):
    context.current_url = context.human_readable_pages(page_name, context.host)
    context.response = client.get(context.current_url)
    return context.response


@then('the response should be successful')
def response_succeeded(context):
    assert context.response.status_code is requests.codes.ok, \
        'Unexpectedly got a %d response code' % context.response.status_code


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
