'''An Example test using Selenium browser.'''
from pytest_bdd import scenarios, given, when, then, parsers

# Registering Feature Files as tests relative to path set in pytest.ini
scenarios('browser_example.feature','about.feature')

# Curretly using steps from qa/tests/steps, but steps specific to this test could be set below.
