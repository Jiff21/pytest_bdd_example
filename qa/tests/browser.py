'''Selenium Setup for Driver'''
from selenium import webdriver
from qa.settings import log
from qa.settings import DEFAULT_WIDTH, DEFAULT_HEIGHT, DEFAULT_BROWSER_POSITION


class Browser():
    '''Object with functions for Selenium Driver setup'''

    def __init__(self):
        log.info('Loading normal browser list')
        self.browser = None
        self.chrome_options = None
        self.desired_capabilities = None
        self.drivers = None

    def set_defaults(self):
        '''set browser position and dimensions to default desktop'''
        self.browser.set_window_size(DEFAULT_WIDTH, DEFAULT_HEIGHT)
        self.browser.set_window_position(
            DEFAULT_BROWSER_POSITION['x'],
            DEFAULT_BROWSER_POSITION['y']
        )

    def mandatory_chrome_options(self):
        '''sets chrome options used amongst different chrome setups'''
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("--disable-plugins")
        self.chrome_options.add_argument("--disable-instant-extended-api")
        self.chrome_options.add_argument("--whitelisted-ips")
        return self.chrome_options

    def generic_chrome_dc(self):
        '''sets desired capabilities used amongst different chrome setups'''
        self.desired_capabilities = webdriver.DesiredCapabilities.CHROME
        self.desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
        self.desired_capabilities['acceptSslCerts'] = True
        self.desired_capabilities['acceptInsecureCerts'] = True
        return self.desired_capabilities

    def setup_firefox_dc(self):
        '''sets desired capabilities used amongst different firefox setups'''
        self.desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
        self.desired_capabilities['acceptInsecureCerts'] = True
        # self.desired_capabilities['javascriptEnabled'] = True
        return self.desired_capabilities

    def get_chrome_driver(self):
        '''Setup for basic chrome'''
        self.desired_capabilities = self.generic_chrome_dc()
        self.chrome_options = self.mandatory_chrome_options()
        self.desired_capabilities.update(self.chrome_options.to_capabilities())
        self.browser = webdriver.Chrome(
            executable_path='chromedriver',
            desired_capabilities=self.desired_capabilities
        )
        # Desktop size
        self.set_defaults()
        return self.browser

    def get_headless_chrome(self):
        '''Setup for basic headless chrome'''
        self.desired_capabilities = self.generic_chrome_dc()
        self.chrome_options = self.mandatory_chrome_options()
        self.chrome_options.add_argument("--headless")
        assert self.chrome_options.headless, 'Chrome not headless?'
        self.desired_capabilities.update(self.chrome_options.to_capabilities())
        self.desired_capabilities['acceptSslCerts'] = True
        self.desired_capabilities['acceptInsecureCerts'] = True
        self.browser = webdriver.Chrome(
            executable_path='chromedriver',
            options=self.chrome_options,
            desired_capabilities=self.desired_capabilities
        )
        # Desktop size
        self.set_defaults()
        return self.browser

    def return_driver_dict(self):
        '''Returns a '''
        self.drivers = {
            'chrome': self.get_chrome_driver,
            'headless_chrome': self.get_headless_chrome,
        }
        return self.drivers
