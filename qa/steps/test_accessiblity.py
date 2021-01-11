'''Accessiblity Steps'''
import time
from functools import partial
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from qa.steps.environment import context, driver




## Does this overwrite?
# scenarios('about.feature')

def send_key_x_times(context, key, number_of_times):
    i = 0
    while i < number_of_times:
        action = ActionChains(context.driver)
        action.send_keys(key).perform()
        i += 1
        time.sleep(0.25)


# # Debugging Purposes
# @when(parsers.parse('I sleep {number} seconds'))
# def step_impl(context, number):
#     time.sleep(number)


@when(parsers.parse('I hit the tab key {number} time(s)'))
def step_impl(context, number):
    send_key_x_times(context, Keys.TAB, number)
    context.current_element = context.driver.switch_to.active_element


# @when(parsers.parse('I hit the shift+tab key {number} time(s)'))
# def step_impl(context, number):
#     i = 0
#     while i < number:
#         action = ActionChains(context.driver)
#         action.send_keys(Keys.SHIFT, Keys.TAB, Keys.SHIFT).perform()
#         i += 1
#         time.sleep(0.25)
#     context.current_element = context.driver.switch_to.active_element


# @when(parsers.parse('I hit the down arrow key {number} time(s)'))
# def step_impl(context, number):
#     send_key_x_times(context, Keys.ARROW_DOWN, number)
#     context.current_element = context.driver.switch_to.active_element


# @when(parsers.parse('I hit the left arrow key {number} time(s)'))
# def step_impl(context, number):
#     send_key_x_times(context, Keys.ARROW_LEFT, number)
#     context.current_element = context.driver.switch_to.active_element



# @when(parsers.parse('I hit the right arrow key {number} time(s)'))
# def step_impl(context, number):
#     send_key_x_times(context, Keys.ARROW_RIGHT, number)
#     context.current_element = context.driver.switch_to.active_element


# @when(parsers.parse('I hit the up arrow key {number} time(s)'))
# def step_impl(context, number):
#     send_key_x_times(context, Keys.ARROW_UP, number)
#     context.current_element = context.driver.switch_to.active_element
#     time.sleep(3)


# @when('I hit the Space key')
# def step_impl(context):
#     context.current_element.send_keys(Keys.SPACE)


# @when('I hit the Return key')
# def step_impl(context):
#     ActionChains(context.driver).send_keys(Keys.RETURN).perform()

# @when(parsers.parse('I type {words} into the focused element'))
# def step_impl(context, words):
#     context.current_element = context.driver.switch_to.active_element
#     context.current_element.send_keys(words)


# @when('I send the user email to the current element')
# def step_impl(context):
#     context.current_element.send_keys(USER_EMAIL)


# @when('I send the user password to the current element')
# def step_impl(context):
#     context.current_element.send_keys(USER_PASSWORD)


# @when('I click the current element')
# def step_impl(context):
#     context.current_element.click()


# @when(parsers.parse('the current element alt field should include {word}'))
# def step_impl(context, word):
#     assert word in context.current_element.text, "Did not see %s in text:\n%s" % (
#         word,
#         context.current_element.text
#     )


# @when('it should have a {width_or_height} of {more_less_equal} {expected_size}px')
# def step_impl(context, width_or_height, more_less_equal, expected_size):
#     assert 'height' in width_or_height or 'width' in width_or_height, \
#         'Unexpected value for width_or_height, got: %s' % width_or_height
#     size = int(context.current_element.size[width_or_height])
#     if more_less_equal.lower() == 'more':
#         assert size > expected_size, 'Expected it to be greater than %i' \
#             ' instead got %i' % (expected_size, size)
#     elif more_less_equal.lower() == 'less':
#         assert size < expected_size, 'Expected it to be less than %i' \
#             ' instead got %i' % (expected_size, size)
#     elif more_less_equal.lower() == 'equal':
#         assert size == expected_size, 'Expected it to be equal to %i' \
#             ' instead got %i' % (expected_size, size)
#     else:
#         assert False, 'Unexpected value for more_less_equal,' \
#             ' got: %s' % more_less_equal