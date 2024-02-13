from .endpoint import Endpoint
from flask import url_for, request
from aims_ui.google_utils import get_username
from aims_ui import app

def get_current_selected_endpoint(endpoints, called_from):
  for endpoint in endpoints:
    if endpoint.page_name == called_from:
      return endpoint.url
  print('ERROR getting endpoint')


def get_endpoints(called_from=None):
  # Add new endpoints here for auto-creation on all pages
  endpoints = [
      Endpoint(
          'Single Search',
          'singlesearch',
          'Provide as much of the address as possible for best results.',
      ),
      Endpoint(
          'Single UPRN',
          'uprn',
          "Search for a property via its unique property reference number. This is a 12 digit number which contains no characters.",
      ),
      Endpoint(
          'Postcode',
          'postcode',
          "Search for a property using its postcode. This is effective and a valid postcode will return a list of possible addresses.",
      ),
      Endpoint(
          'Typeahead',
          'typeahead',
          "This search types ahead. Autosuggest on steroids basically. Useful if you quickly want a user to find an address.",
      ),
      Endpoint(
          'Multiple Address',
          'multiple_address_original',
          "Search for not just  one address. Several. Get lots of results you can look through. This service completes many single searches from a file.",
      ),
      Endpoint(
          'Multiple UPRN',
          'uprn_multiple_match',
          "Search for multiple addresses providing mulitple UPRNs (Unique Property Reference Numbers)",
      ),
     Endpoint(
          'API',
          'custom_response',
          'Submit requests directly to the API and receive JSON style fromatting in return. Use this if you want to test out API features that the UI currently does not support',
      ),
     Endpoint(
          'Help',
          'help',
          'See information about the other pages and how to contact support.',
          url = url_for('help', subject='home'),
      ),
     Endpoint(
          'Settings',
          'settings',
          'User prefferences are stored locally on their web-browser. Adjust or reset those settings here.',
      ),
  ]

  username = get_username()

  called_from = '' if called_from == None else called_from
  current_selected_endpoint = get_current_selected_endpoint(endpoints, called_from)

  # Create dict for ons-navigation component
  nav_info = [{
      'title': endpoint.title,
      'url': endpoint.url
  } for endpoint in endpoints]

  # Add a copy of the navigation info to each Endpoint
  for endpoint in endpoints:
    endpoint.nav_info = nav_info
    endpoint.current_selected_endpoint = current_selected_endpoint

  return endpoints
