'''Using Conftest.py as as the behave equivalent of common.py'''
# Import all common steps from the step folder here:
import pytest
from qa.tests.steps.common import *
from qa.tests.steps.accessiblity import *

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
    print('\nAfter Scenario Hook\n')
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