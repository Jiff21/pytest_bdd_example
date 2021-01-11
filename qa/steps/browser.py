from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from qa.config.conftest import log
from qa.config.conftest import DEFAULT_WIDTH, DEFAULT_HEIGHT, DEFAULT_BROWSER_POSITION


class Browser(object):


    # def __init__(self):
    def __init__(self, **kwargs):
        log.info('Loading normal browser list')

    def set_defaults(self, browser_obj):
        browser_obj.set_window_size(DEFAULT_WIDTH, DEFAULT_HEIGHT)
        # Keep position 2nd or Safari will reposition on set_window_sizeself
        # Safari also requires you account for OSX Top Nav & is iffy about edge
        browser_obj.set_window_position(
            DEFAULT_BROWSER_POSITION['x'],
            DEFAULT_BROWSER_POSITION['y']
        )


    def mandatory_chrome_options(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("--disable-plugins")
        self.chrome_options.add_argument("--disable-instant-extended-api")
        self.chrome_options.add_argument("--whitelisted-ips")
        return self.chrome_options


    def generic_chrome_dc(self):
        self.desired_capabilities = webdriver.DesiredCapabilities.CHROME
        self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
        self.desired_capabilities['acceptSslCerts'] = True
        self.desired_capabilities['acceptInsecureCerts'] = True
        return self.desired_capabilities


    def setup_firefox_dc(self):
        self.desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
        self.desired_capabilities['acceptInsecureCerts'] = True
        # self.desired_capabilities['javascriptEnabled'] = True
        return self.desired_capabilities


    def get_chrome_driver(self):
        self.desired_capabilities = self.generic_chrome_dc()
        self.chrome_options = self.mandatory_chrome_options()
        self.desired_capabilities.update(self.chrome_options.to_capabilities())
        self.browser = webdriver.Chrome(
            executable_path='chromedriver',
            desired_capabilities=self.desired_capabilities
        )
        # Desktop size
        self.set_defaults(self.browser)
        return self.browser


    def get_headless_chrome(self):
        self.desired_capabilities = self.generic_chrome_dc()
        self.chrome_options = self.mandatory_chrome_options()
        self.chrome_options.add_argument("--headless")
        assert self.chrome_options.headless == True, \
            'Chrome did not get set to headless'
        self.desired_capabilities.update(self.chrome_options.to_capabilities())
        self.desired_capabilities['acceptSslCerts'] = True
        self.desired_capabilities['acceptInsecureCerts'] = True
        self.browser = webdriver.Chrome(
            executable_path='chromedriver',
            options=self.chrome_options,
            desired_capabilities=self.desired_capabilities
        )
        # Desktop size
        self.set_defaults(self.browser)
        return self.browser


    def return_driver_dict(self):
        self.drivers = {
            'chrome': self.get_chrome_driver,
            'headless_chrome': self.get_headless_chrome,
        }
        return self.drivers
