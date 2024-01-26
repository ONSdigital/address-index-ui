from .endpoint import Endpoint
from flask import url_for, request
from aims_ui import app


def get_endpoints(called_from=None):
  # Add new endpoints here for auto-creation on all pages
  endpoints = [
      Endpoint(
          'Single Search',
          'singlesearch',
          'Provide as much of the address as possible for best results.',
      ),
      Endpoint(
          'UPRN Single Search',
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
  ]

  # Set the username on all endpoints
  user_email = request.headers.get('X-Goog-Authenticated-User-Email',
                                   'UserNotLoggedIn')
  user_email = user_email.replace('accounts.google.com:', '')
  user_email = user_email.replace('@ons.gov.uk', '')

  if called_from == None:
    called_from = ''
  if called_from == 'help':
    current_selected_endpoint = '/help/home'
  elif 'multiple_address' in called_from:
    called_from = 'multiple_address_original'
  elif called_from != 'address_info':
    current_selected_endpoint = url_for('settings')
  else:
    current_selected_endpoint = ''

  for endpoint in endpoints:
    endpoint.user_email = user_email
    if endpoint.url_title == called_from:
      endpoint.selected = True
      current_selected_endpoint = url_for(endpoint.url_title)

  # Paywall check
  
  # Remove users from everything but help and settings
  paywall_checked_endpoints = []
  conf = app.config
  remove_conf = [{key: conf[key]} for key in conf if key.startswith("REMOVE_")]

  for endpoint in endpoints:
    for remove in remove_conf:
      for key, remove_values in remove.items():
        to_remove_name = remove_values.get('name') # e.g. typeahead, multiple_address_match
        if to_remove_name == endpoint.url_title:
          users_to_remove = remove_values.get('users_to_remove')
          if user_email in users_to_remove: 
            print('removing', user_email, 'from', endpoint.title, '\n')
          else:
            print('adding', endpoint, '\n')
            paywall_checked_endpoints.append(endpoint)

  nav_info = [{
      'title': endpoint.title,
      'url': endpoint.url
  } for endpoint in paywall_checked_endpoints]

  if user_email not in app.config.get('REMOVE_HELP').get('users_to_remove'):
    nav_info.insert(len(nav_info), {'title': 'Help', 'url': '/help/home'}) # YAPF disable
  if user_email not in app.config.get('REMOVE_SETTINGS').get('users_to_remove'):
    nav_info.insert(len(nav_info), {'title': 'Settings', 'url': url_for('settings') }) # YAPF disable

  for endpoint in paywall_checked_endpoints:
    endpoint.nav_info = nav_info
    endpoint.current_selected_endpoint = current_selected_endpoint

  return paywall_checked_endpoints 
