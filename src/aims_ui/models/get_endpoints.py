import logging

from flask import url_for

from aims_ui.page_helpers.google_utils import get_current_group

from .endpoint import Endpoint


def get_current_selected_endpoint(endpoints, called_from):
  # Get the endpoint that matches the page 'called_from'
  for endpoint in endpoints:
    if endpoint.page_name == called_from:
      endpoint.selected = True
      return endpoint
  
  logging.error(f'No endpoint found for page {called_from}. Check get_endpoints.py to ensure the page is added as an Endpoint')


def get_endpoints(called_from=None):
  sub_nav_for_multiple_matches = [
    {
      'title': 'Small Multiple Match',
      'url': url_for('multiple_address_small_submit'),
    },
    {
      'title': 'Large Multiple Match',
      'url': url_for('multiple_address_large_submit'),
    },
    {
      'title': 'UPRN Multiple Match',
      'url': url_for('uprn_multiple_match'),
    }
  ]
 
  # Add new endpoints here for auto-creation on all pages
  endpoints = [
      Endpoint(
          'Single Search',
          'singlesearch',
          'Provide as much of the address as possible for best results.',
          'a_single_matches',
      ),
      Endpoint(
          'Single UPRN',
          'uprn',
          "Search for a property via its unique property reference number. This is a 12 digit number which contains no characters.",
          'a_single_matches',
      ),
      Endpoint(
          'Postcode',
          'postcode',
          "Search for a property using its postcode. This is effective and a valid postcode will return a list of possible addresses.",
          'a_single_matches',
      ),
      Endpoint(
          'Typeahead',
          'typeahead',
          "This search types ahead. Autosuggest on steroids basically. Useful if you quickly want a user to find an address.",
          'a_single_matches',
      ),
      # Multiple matches includes sub-menu
      Endpoint(
          'Multiple Matches',
          'multiple_address_small_submit',
          "Submit a small file to match addresses. This uses the singlesearch endpoint controlled by the UI instead of the bulk matching solution provided by the 'Large Multiple Match'",
          'b_multiple_matches/small_multiple_match',
          sub_nav_endpoints=sub_nav_for_multiple_matches,
     ),
      Endpoint(
          'Multiple UPRN',
          'uprn_multiple_match',
          "Search for multiple addresses providing mulitple UPRNs (Unique Property Reference Numbers)",
          'b_multiple_matches/uprn_multiple_match',
          sub_nav_endpoints=sub_nav_for_multiple_matches,
          visible_in_main_nav=False,
      ),
      Endpoint(
          'API',
          'custom_response',
          'Submit requests directly to the API and receive JSON style fromatting in return. Use this if you want to test out API features that the UI currently does not support',
          'd_misc_functionality',
      ),
      Endpoint(
          'Radius Search',
          'radiussearch',
          'To get started, click on the map or enter a latitude and longitude manually. Search around this location within a set range to see results plotted on the map.',
          'a_single_matches',
      ),
      Endpoint(
          'Help',
          'help',
          'See information about the other pages and how to contact support.',
          'c_help_pages',
          url=url_for('help', subject='home'),
      ),
      Endpoint(
          'Settings',
          'settings',
          'User preferences are stored locally on their web-browser. Adjust or reset those settings here.',
          'd_misc_functionality',
          url=url_for('settings')),
  ]

  called_from = '' if called_from == None else called_from
  current_selected_endpoint = get_current_selected_endpoint(
      endpoints, called_from)

  # Before the nav component is made from Endpoints, remove unallowed pages

  current_group = get_current_group()
  allowed_pages = current_group.get('allowed_pages', [])

  secure_endpoints = []
  for endpoint in endpoints:
    if endpoint.page_name in allowed_pages:
      secure_endpoints.append(endpoint)

  # Create dict for ons-navigation component
  nav_info = []
  for endpoint in secure_endpoints:
    if endpoint.visible_in_main_nav:
      nav_info.append({
          'title': endpoint.title,
          'url': endpoint.url
      })

  # Add a copy of the navigation info to the current endpoint
  current_selected_endpoint.nav_info = nav_info
  current_selected_endpoint.current_selected_endpoint = current_selected_endpoint

  return secure_endpoints, current_selected_endpoint
