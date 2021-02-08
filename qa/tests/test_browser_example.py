'''An Example test using Selenium browser.'''
from pytest_bdd import scenarios, given, when, then, parsers


# Registering Feature Files as tests relative to path set in pytest.ini
# scenarios('features/browser_example.feature','features/about.feature')
scenarios('features')

# Curretly using steps from qa/tests/steps, but steps specific to this test could be set below.
