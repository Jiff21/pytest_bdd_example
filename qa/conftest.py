'''Using Conftest.py as as the behave equivalent of common.py'''
# Import all common steps from the step folder here:
from qa.tests.steps.common import *
from qa.tests.steps.accessiblity import *

# see qa/setting.py for setup as it can't be setup here without circular logic