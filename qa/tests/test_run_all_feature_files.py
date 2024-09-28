'''An Example test using Selenium browser.'''
from pytest_bdd import scenarios, given, when, then, parsers


# Registering Feature Files as tests relative to path set in pytest.ini
# scenarios('features/browser_example.feature','features/about.feature')
scenarios('features')

# Function name must include test_ and be unique
# def test_all_tests_in_features():
#     steps for this test found in conftest.py
#     pass
