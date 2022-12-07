from .endpoint import Endpoint
from flask import url_for


def get_endpoints(called_from=None):
  # Add new endpoints here for auto-creation on all pages
  endpoints = [
      Endpoint(
          'Single Search',
          'singlesearch',
          'Provide as much of the address as possible for best results.',
      ),
      Endpoint(
          'Unique Property Reference Number',
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
  ]

  if called_from == None:
    called_from = ''
  if called_from == 'help':
    current_selected_endpoint = '/help/home'
  elif 'multiple_address' in called_from:
    called_from = 'multiple_address_original'
  elif called_from != 'address_info':
    current_selected_endpoint = url_for('about')
  else:
    current_selected_endpoint = ''

  for endpoint in endpoints:
    if endpoint.url_title == called_from:
      endpoint.selected = True
      current_selected_endpoint = url_for(endpoint.url_title)

  nav_info = [{
      'title': endpoint.title,
      'url': endpoint.url
  } for endpoint in endpoints]
  # Add the 'About' section at the end, insert instead of append so it's location can easily
  # be changed later, after consulting with UX team
  nav_info.insert(len(nav_info), {'title': 'Help', 'url': '/help/home'})
  nav_info.insert(len(nav_info), {'title': 'About', 'url': url_for('about')})

  for endpoint in endpoints:
    endpoint.nav_info = nav_info
    endpoint.current_selected_endpoint = current_selected_endpoint

  return endpoints
