import logging

from flask import url_for

from aims_ui.page_helpers.google_utils import get_current_group


def get_current_selected_endpoint(endpoints, called_from):
  # Get the endpoint that matches the page 'called_from'
  for endpoint in endpoints:

    # Ignore if it's a parent page
    if endpoint.get('type_of_page') != 'parent_page':
      if endpoint.get('page_name') == called_from:
        return endpoint
  
  logging.error(f'No endpoint found for page {called_from}. Check get_endpoints.py to ensure the page is added as an Endpoint')


def get_endpoints(called_from=''):

  # Add new endpoints here for auto-creation on all pages
  endpoints = [
    {
      'title': 'Single Search',
      'type_of_page': 'main_nav',
      'page_name': 'singlesearch',
      'url': url_for('singlesearch'),
      'description_text': 'Provide as much of the address as possible for best results.',
      'file_location': 'a_single_matches'
    },
    {
      'title': 'Single UPRN',
      'type_of_page': 'main_nav',
      'page_name': 'uprn',
      'url': url_for('uprn'),
      'description_text': 'Search for a property via its unique property reference number. This is a 12 digit number which contains no characters.',
      'file_location': 'a_single_matches'
    },
    {
      'title': 'Postcode',
      'type_of_page': 'main_nav',
      'page_name': 'postcode',
      'url': url_for('postcode'),
      'description_text': 'Search for a property using its postcode. This is effective and a valid postcode will return a list of possible addresses.',
      'file_location': 'a_single_matches'
    },
    {
      'title': 'Typeahead',
      'type_of_page': 'main_nav',
      'page_name': 'typeahead',
      'url': url_for('typeahead'),
      'description_text': 'This search types ahead. Autosuggest on steroids basically. Useful if you quickly want a user to find an address.',
      'file_location': 'a_single_matches'
    },
    {
      'title': 'Multiple Matches',
      'type_of_page': 'parent_page',
      'page_name': 'multiple_matches_parent',
      'url': url_for('multiple_address_small_submit'),
      'page_child_name': 'multiple_address_small_submit',
      'description_text': "Submit a small file to match addresses. This uses the singlesearch endpoint controlled by the UI instead of the bulk matching solution provided by the 'Large Multiple Match'",
      'file_location': 'b_multiple_matches/small_multiple_match',
    },
    {
      'title': 'Small Multiple Match',
      'type_of_page': 'sub_nav',
      'page_parent': 'multiple_matches_parent',
      'page_name': 'multiple_address_small_submit',
      'url': url_for('multiple_address_small_submit'),
      'description_text': "Small multiple match allows users to submit a small file of addresses to be matched. This uses the same endpoint as the single search pages",
      'file_location': 'b_multiple_matches/small_multiple_match',
    },
    {
      'title': 'Large Multiple Match',
      'type_of_page': 'sub_nav',
      'page_parent': 'multiple_matches_parent',
      'page_name': 'multiple_address_large_submit',
      'url': url_for('multiple_address_large_submit'),
      'description_text': "Submit a large file ",
      'file_location': 'b_multiple_matches/large_multiple_match',
    },
    {
      'title': 'Multiple UPRN',
      'type_of_page': 'sub_nav',
      'page_parent': 'multiple_matches_parent',
      'page_name': 'uprn_multiple_match',
      'url': url_for('uprn_multiple_match'),
      'description_text': 'Search for multiple addresses providing mulitple UPRNs (Unique Property Reference Numbers)',
      'file_location': 'b_multiple_matches/uprn_multiple_match',
    },
    {
      'title': 'API',
      'type_of_page': 'main_nav',
      'page_name': 'custom_response',
      'url': url_for('custom_response'),
      'description_text': 'Submit requests directly to the API and receive JSON style fromatting in return. Use this if you want to test out API features that the UI currently does not support',
      'file_location': 'd_misc_functionality'
    },
    {
      'title': 'Radius Search',
      'type_of_page': 'main_nav',
      'page_name': 'radiussearch',
      'url': url_for('radiussearch'),
      'description_text': 'To get started, click on the map or enter a latitude and longitude manually. Search around this location within a set range to see results plotted on the map.',
      'file_location': 'a_single_matches'
    },
    {
      'title': 'Help',
      'type_of_page': 'main_nav',
      'page_name': 'help',
      'description_text': 'See information about the other pages and how to contact support.',
      'file_location': 'c_help_pages',
      'url': url_for('help', subject='home')
    },
    {
      'title': 'Settings',
      'type_of_page': 'main_nav',
      'page_name': 'settings',
      'url': url_for('settings'),
      'description_text': 'User preferences are stored locally on their web-browser. Adjust or reset those settings here.',
      'file_location': 'd_misc_functionality',
    }
  ]


  # Get the endpoint that matches the 'called_from' to 'page_name'
  current_selected_endpoint = get_current_selected_endpoint(
      endpoints, called_from)

  current_selected_endpoint['selected'] = True

  # Before the nav component is made from Endpoints, remove unallowed pages
  current_group = get_current_group()
  allowed_pages = current_group.get('allowed_pages', [])

  secure_endpoints = []
  for endpoint in endpoints:
    if endpoint.get('page_name') in allowed_pages:
      secure_endpoints.append(endpoint)

  # Create dict for ons-navigation component
  nav_info = [{'title':'Multiple Matches', 'url': '/multiple_address_small_submit'}] 
  for endpoint in secure_endpoints:
    if endpoint.get('type_of_page') == 'main_nav':
      nav_info.append({
          'title': endpoint.get('title'),
          'url': endpoint.get('url')
      })
  
  sub_nav_info = [{
    'title': 'a',
    'url': ''
  }]
  
  current_selected_endpoint['sub_nav_info'] = sub_nav_info

  # Add a copy of the navigation info to the current endpoint
  current_selected_endpoint['nav_info'] = nav_info

  return secure_endpoints, current_selected_endpoint
