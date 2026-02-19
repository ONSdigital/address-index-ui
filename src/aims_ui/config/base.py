"""FLASK BASE CONFIG"""
import base64
import json
import os

from aims_ui.app_helpers.get_app_version import get_app_version

# Port that the Flask server will run on
UI_EXPOSED_PORT = 5000

JSONIFY_PRETTYPRINT_REGULAR = True
MAX_CONTENT_LENGTH = 10 * 1024 * 1024
API_AUTH_TYPE = os.getenv('API_AUTH_TYPE')

API_JWT_TOKEN = os.getenv('API_JWT_TOKEN')
API_JWT_TOKEN_BEARER = 'Bearer ' + str(API_JWT_TOKEN if API_JWT_TOKEN else '')

BM_JWT_TOKEN = os.getenv('BM_JWT_TOKEN')
BM_JWT_TOKEN_BEARER = 'Bearer ' + str(BM_JWT_TOKEN if BM_JWT_TOKEN else '')
BM_JOB_NAME_CHAR_LIMIT = int(os.getenv('BM_JOB_NAME_CHAR_LIMIT', '20'))

PROJECT_DOMAIN = os.getenv('PROJECT_DOMAIN')
BM_API_URL = os.getenv('BM_API_URL')
BM_MAX_JOBS = int(os.getenv('BM_MAX_JOBS', '7'))

SESSION_COOKIE_SECURE = True
AIMS_UI_PAGES_LOCATION = 'aims_ui_pages'

API_BSC_AUTH_USERNAME = os.getenv('API_BSC_AUTH_USERNAME')
API_BSC_AUTH_PASSWORD = os.getenv('API_BSC_AUTH_PASSWORD')

API_JWT_K_VALUE = str(os.getenv('API_JWT_K_VALUE'))
API_JWT_K_VALUE = base64.b64decode(API_JWT_K_VALUE)

FLASK_ENV = str(os.getenv('FLASK_ENV')).upper()

# Current version of local storage, increment when making breaking changes
LOCAL_STORAGE_VERSION = '1'

# Get the app version from version.txt in the root directory
APP_VERSION = get_app_version()

# Default usernames for paywall
USER_AUTHS = json.loads(os.getenv('USER_AUTHS', '{}'))

# Define order of pages on header and Paywall Limitations
ALL_PAGE_NAMES = [
    'singlesearch', 'uprn', 'postcode', 'typeahead',
    'multiple_address_original', 'multiple_address_results',
    'multiple_address_attributes', 'multiple_address', 'uprn_multiple_match',
    'radiussearch', 'custom_response', 'help', 'settings'
]

DEFAULT_BULK_LIMITS = {
    'limit_mini_bulk': 5000,
    'limit_vast_bulk': 100000,
    'limit_uprn_match': 5000,
}

# yapf: disable
USER_GROUPS = [
    {
        'name': 'default',  # UNSPECIFIED USERS WILL BE IN THIS GROUP
        'description': 'Users that do not fall into another group will be part of this group',
        'usernames': USER_AUTHS.get('default', []),
        'pages_to_remove': ['custom_response'],
        'bulk_limits': DEFAULT_BULK_LIMITS,
    },
    {
        'name': 'developers',
        'description': 'Developer users who might need more granular access to the API and are comfortable dealing with errors and less guard rails',
        'usernames': USER_AUTHS.get('developers', []),
        'pages_to_remove': [],
        'bulk_limits': DEFAULT_BULK_LIMITS,
    },
    {
        'name': 'bulk_removed',
        'description': 'Completely remove access to the bulk match pages',
        'usernames': USER_AUTHS.get('bulk_removed', []),
        'pages_to_remove': [
            'multiple_address_original', 'uprn_multiple_match',
            'multiple_address', 'multiple_address_results', 'multiple_address_attributes'
        ],
        'bulk_limits': DEFAULT_BULK_LIMITS,
    },
    {
        'name': 'limited_bulk',
        'description': 'Limit the matching capacity but leave access to the pages',
        'usernames': USER_AUTHS.get('limited_bulk', []),
        'pages_to_remove': [],
        'bulk_limits': {
            'limit_mini_bulk': 10,
            'limit_vast_bulk': 550,
            'limit_uprn_match': 50,
        }
    },
]
# yapf: enable

# For each group, create a list of "allowed pages"
for group in USER_GROUPS:
  allowed_pages = []
  for page_name in ALL_PAGE_NAMES:
    if page_name not in group.get('pages_to_remove'):
      allowed_pages.append(page_name)
  group['allowed_pages'] = allowed_pages

# Default Classification and Epoch options, should the initial server response be incorrect (or the endpoint doesn't exist)

DEFAULT_EPOCH_SELECTED = '89'
DEFAULT_EPOCH_OPTIONS = [{
    'id': '39',
    'text': '39',
    'value': '39',
    'description': 'Exeter Sample'
}, {
    'id': '80',
    'text': '80',
    'value': '80',
    'description': 'Census no extras'
}, {
    'id': '87',
    'text': '87',
    'value': '87',
    'description': 'September 2021'
}, {
    'id': '89',
    'text': '89',
    'value': '89',
    'description': 'December 2021'
}]
