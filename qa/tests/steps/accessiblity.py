# -*- coding: UTF-8 -*-
# MISSING-DOCSTRING: pylint: disable=C0111
# CONTEXT REDEFINED: pylint: disable=W0621

'''Accessiblity Steps'''
import time
from pytest_bdd import when, then, parsers
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from qa.tests.steps.workarounds import scroll_nav_out_of_way
from qa.tests.steps.workarounds import scroll_footer_out_of_way
from qa.settings import USER_EMAIL, USER_PASSWORD


def send_key_x_times(context, key, number_of_times):
    i = 0
    while i < number_of_times:
        action = ActionChains(context.driver)
        action.send_keys(key).perform()
        i += 1
        time.sleep(0.25)


# Generic step that can be used when writing a feature file for debugging tab numbers
@when(parsers.parse('I sleep {number:d} seconds'))
def when_i_sleep(number):
    time.sleep(number)


@when(parsers.parse('I hit the tab key {number:d} time(s)'))
def tab_x_times(context, number):
    send_key_x_times(context, Keys.TAB, number)
    context.current_element = context.driver.switch_to.active_element


@when(parsers.parse('I hit the shift+tab key {number:d} time(s)'))
def shift_plus_tab(context, number):
    i = 0
    while i < number:
        action = ActionChains(context.driver)
        action.send_keys(Keys.SHIFT, Keys.TAB, Keys.SHIFT).perform()
        i += 1
        time.sleep(0.25)
    context.current_element = context.driver.switch_to.active_element


@when(parsers.parse('I hit the down arrow key {number:d} time(s)'))
def arrow_down_key(context, number):
    send_key_x_times(context, Keys.ARROW_DOWN, number)
    context.current_element = context.driver.switch_to.active_element


@when(parsers.parse('I hit the left arrow key {number:d} time(s)'))
def arrow_left_key(context, number):
    send_key_x_times(context, Keys.ARROW_LEFT, number)
    context.current_element = context.driver.switch_to.active_element


@when(parsers.parse('I hit the right arrow key {number:d} time(s)'))
def arrow_right_key(context, number):
    send_key_x_times(context, Keys.ARROW_RIGHT, number)
    context.current_element = context.driver.switch_to.active_element


@when(parsers.parse('I hit the up arrow key {number:d} time(s)'))
def arrow_up_key(context, number):
    send_key_x_times(context, Keys.ARROW_UP, number)
    context.current_element = context.driver.switch_to.active_element
    time.sleep(3)


@when('I hit the Space key')
def space_key(context):
    context.current_element.send_keys(Keys.SPACE)


@when('I hit the Return key')
def return_key(context):
    ActionChains(context.driver).send_keys(Keys.RETURN).perform()


@when('I hit the Esc key')
def escape_key(context):
    ActionChains(context.driver).send_keys(Keys.ESCAPE).perform()


@when(parsers.parse('I type {words} into the focused element'))
def type_focused(context, words):
    context.current_element = context.driver.switch_to.active_element
    context.current_element.send_keys(words)


@when('I send the user email to the current element')
def type_email_current(context):
    context.current_element.send_keys(USER_EMAIL)


@when('I send the user password to the current element')
def type_pass_current(context):
    context.current_element.send_keys(USER_PASSWORD)


@when('I click the current element')
def click_current(context):
    context.current_element.click()


@when(parsers.parse('the current element alt field should include {word}'))
def alt_field_should(context, word):
    assert word in context.current_element.text, "Did not see %s in text:\n%s" % (
        word,
        context.current_element.text
    )


@then('it should have a {width_or_height:d} of {more_less_equal} {expected_size:d}px')
def current_size_expects(context, width_or_height, more_less_equal, expected_size):
    assert 'height' in width_or_height or 'width' in width_or_height, \
        'Unexpected value for width_or_height, got: %s' % width_or_height
    size = int(context.current_element.size[width_or_height])
    if more_less_equal.lower() == 'more':
        assert size > expected_size, 'Expected it to be greater than %i' \
            ' instead got %i' % (expected_size, size)
    elif more_less_equal.lower() == 'less':
        assert size < expected_size, 'Expected it to be less than %i' \
            ' instead got %i' % (expected_size, size)
    elif more_less_equal.lower() == 'equal':
        assert size == expected_size, 'Expected it to be equal to %i' \
            ' instead got %i' % (expected_size, size)
    else:
        assert False, 'Unexpected value for more_less_equal, got: %s' % (
            more_less_equal
        )


@when('I scroll the nav out of the way')
def scroll_nav_out_way(context):
    scroll_nav_out_of_way(context.driver)


@when('I scroll the footer out of the way')
def scroll_footer_out_way(context):
    scroll_footer_out_of_way(context.driver)
