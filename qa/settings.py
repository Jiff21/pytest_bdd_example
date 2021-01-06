import logging
import os

logging.basicConfig()
log = logging.getLogger('BYNDQA')
log.setLevel(os.getenv('LOG_LEVEL', 'ERROR'))

DRIVER = os.getenv('DRIVER', 'chrome')
DRIVER = DRIVER.lower().replace(' ', '_').replace('-', '_')
FEATURE_PATH = '../features/'

# use `export QA_ENV=name` to set the current envionrment you're testing against
QA_ENV = os.getenv('QA_ENV', 'local').lower()

########
# Overwritten by ENV files
########

HOST = os.getenv('HOST', 'localhost')
PORT = os.getenv('PORT', '3000')
IAP_ON = bool(os.getenv('IAP_ON', False))

if 'local' in QA_ENV:
    HOST_URL = os.getenv('HOST_URL', 'http://%s:%s' % (HOST, PORT))
else:
    HOST_URL = os.getenv('HOST_URL', 'https://%s' % HOST)

# Basic Auth
BASIC_AUTH_USER = os.getenv('BASIC_AUTH_USER', None)
BASIC_AUTH_PASSWORD = os.getenv('BASIC_AUTH_PASSWORD', None)

# Google IAP
CLIENT_ID = os.getenv(
    'CLIENT_ID', '012345678901-am29widj4kW0l57Kaqmsh3ncjskepsk2.apps.googleusercontent.co')
GOOGLE_APPLICATION_CREDENTIALS = os.getenv(
    'GOOGLE_APPLICATION_CREDENTIALS', '/path/to/json/web/token.json')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', '0123456789')

# Admin Email and password for CMS Testing
ADMIN_URL = 'https://example.com/admin-uri'

# site map for human readable names
PAGES_DICT = {
    'index': '/',
}

DEFAULT_WIDTH = 1366
DEFAULT_HEIGHT = 768
MOBILE_WIDTH = 504
MOBILE_HEIGHT = 640
TABLET_WIDTH = 600
TABLET_HEIGHT = 1024
MOBILE_BREAKPOINT = 599
TABLET_BREAKPOINT = 1023


# Safari requires you account for OSX Top Nav & is iffy about edge
DEFAULT_BROWSER_POSITION = {
    'x': 10,
    'y': 30
}

PROXY_PASSTHROUGH = os.getenv('PROXY_PASSTHROUGH', [
    'example.storage.googleapis.com',
])

SLACK_URL = os.getenv('SLACK_URL', 'https://hooks.slack.com/services/blarg/blerg')
SLACK_CHANNEL = os.getenv('SLACK_CHANNEL', None)

OK_SRCS = [
    HOST_URL,
    '*.doubleclick.net',
    '*.ggpht.com',
    '*.google-analytics.com',
    '*.googleapis.com',
    '*.googleusercontent.com',
    '3p.ampproject.net',
    'abc.xyz',
    'accounts.google.com',
    'ajax.googleapis.com',
    'cdn.firebase.com',
    'fonts.googleapis.com',
    'fonts.gstatic.com',
    'gmodules.com',
    'google.[ccTLD]',
    'googleadservices.com',
    'googlegoro.com',
    'googleplex.com',
    'googletagmanager.com',
    'gstatic.cn',
    'i.ytimg.com',
    'maps.gstatic.com',
    'pagead2.googlesyndication.com',
    'policies.google.com',
    's0.2mdn.net',
    'schema.org',
    'securetoken.googleapis.com',
    'ssl.gstatic.com',
    'static.dialogflow.com',
    'stats.g.doubleclick.net',
    'storage.googleapis.com',
    'tagmanager.google.com',
    'tensorflow.org',
    'thinkwithgoogle.com',
    'www.google-analytics.com',
    'www.google.com',
    'www.googleapis.com',
    'www.googletagmanager.com',
    'www.googletagservices.com',
    'www.gstatic.com',
    'www.youtube.com',
    'www.zagat.com',
    'ytimg.com',
]

default_headers = {
    'Accept-Charset': 'UTF-8',
    'Accept': 'text/html,application/xhtml+xml,application/xml,application/json,image/webp,image/apng,',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36, QA Tests'
}

log.info('QA_ENV is set to {}'.format(QA_ENV))
log.info('DRIVER is set to {}'.format(DRIVER))
log.info('IAP_ON is set to {}'.format(IAP_ON))
log.info('Host url is %s' % HOST_URL)
log.info('Admin url is %s' % ADMIN_URL)
log.info('Proxy passthrough set to {}'.format(PROXY_PASSTHROUGH))
