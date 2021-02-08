'''Workarounds for common browser issues and capatalibilty stints'''
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotSelectableException
from qa.settings import log


def scroll_to_webelement(driver, web_element):
    '''
    Scroll to a web element
    '''
    x = web_element.location['x']  # pylint: disable=C0103
    y = web_element.location['y']  # pylint: disable=C0103
    scroll_by_coord = 'window.scrollTo(%s,%s);' % (
        x,
        y
    )
    driver.execute_script(scroll_by_coord)
    time.sleep(0.5)


def scroll_nav_out_of_way(driver):
    '''
    Scroll nav out of the way
    '''
    script = 'window.scrollBy(0, -80);'
    driver.execute_script(script)
    time.sleep(0.5)


def scroll_double_nav_out_of_way(driver):
    '''
    Scroll the double out of the way
    '''
    script = 'window.scrollBy(0, -130);'
    driver.execute_script(script)
    time.sleep(0.5)


def scroll_footer_out_of_way(driver):
    '''
    Scroll nav out of the way
    '''
    script = 'window.scrollBy(0, 110);'
    driver.execute_script(script)
    time.sleep(0.5)


def avoid_footer_and_nav_click(driver, element):
    '''
    Tries avoiding the nav, if that excepts tries avoiding the footer
    '''
    try:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        action = ActionChains(driver)
        action.move_to_element(element)
        action.click()
        action.perform()
        scroll_nav_out_of_way(driver)
        action.move_to_element(element)
        action.click()
        action.perform()
    except ElementNotSelectableException:
        driver.execute_script('window.scrollTo(0,0);')
        action = ActionChains(driver)
        action.move_to_element(element)
        action.click()
        action.perform()
        scroll_footer_out_of_way(driver)
        action.move_to_element(element)
        action.click()
        action.perform()


def safari_window_switcher(context, title):
    '''Safari has timing issues with which window is what.'''
    if 'safari' in context.driver.capabilities['browserName']:
        context.expected_title = title
        for i in range(0, len(context.driver.window_handles)):
            context.driver.switch_to_window(context.driver.window_handles[i])
            if context.driver.title == context.expected_title:
                context.handle_to_switch_to = context.driver.current_window_handle
        log.info(context.driver.title)
        context.driver.switch_to_window(context.handle_to_switch_to)
        assert context.driver.title == context.expected_title, \
            'Safari swindow switching issue at %s' % context.driver.current_url


def make_sure_safari_back_on_only_window(driver):
    '''
        Without this it sometimes doesn't switch to the original window.
        Oddly though the time it takes to run makes it unnecessary.
    '''
    if 'safari' in driver.capabilities['browserName']:
        if len(driver.window_handles) > 1:
            log.info('Waiting for only 1 tab')
            time.sleep(0.25)
            make_sure_safari_back_on_only_window(driver)
        else:
            log.error('Only 1 tab open!')
            driver.switch_to_window(driver.window_handles[0])


def safari_text_shim(selector_type, text_to_find, driver):
    '''Safari isn't good with XPATH text selector'''
    all_els = driver.find_elements(By.CSS_SELECTOR, selector_type)
    for element in all_els:
        if text_to_find in element.text:
            log.info('Found text: %s' % element.text)  # pylint: disable=W1201
            actions = ActionChains(driver)
            actions.move_to_element(element)
            actions.click()
            actions.perform()
            return


# From somebody else but works well
class LocalStorage:
    '''Utlity Object for dealing with browser local storage'''

    def __init__(self, driver):
        self.driver = driver

    def __len__(self):
        return self.driver.execute_script("return window.localStorage.length;")

    def items(self):
        '''Gets an item in local storage'''
        return self.driver.execute_script(
            'var ls = window.localStorage, items = {}; '
            'for (var i = 0, k; i < ls.length; ++i) '
            '  items[k = ls.key(i)] = ls.getItem(k); '
            'return items; '
        )

    def keys(self):
        '''Gets keys for items in local storage'''
        return self.driver.execute_script(
            'var ls = window.localStorage, keys = []; '
            'for (var i = 0; i < ls.length; ++i) '
            '  keys[i] = ls.key(i); '
            'return keys; '
        )

    def get_all(self, key):
        '''Gets all items in local storage'''
        return self.driver.execute_script(
            'return window.localStorage.getItem(arguments[0]);',
            key
        )

    def set(self, key, value):
        '''Set an item in local storage by key value'''
        self.driver.execute_script(
            "window.localStorage.setItem(arguments[0], arguments[1]);",
            key,
            value
        )

    def has(self, key):
        '''checks to see if key exists in local storage'''
        return key in self.keys()

    def remove(self, key):
        '''remove an item local storage by key'''
        self.driver.execute_script(
            "window.localStorage.removeItem(arguments[0]);",
            key
        )

    def clear(self):
        '''clears local storage by key'''
        self.driver.execute_script("window.localStorage.clear();")
