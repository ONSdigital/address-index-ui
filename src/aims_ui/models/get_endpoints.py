from .endpoint import Endpoint
from flask import url_for


def get_endpoints(called_from=None):
  # Add new endpoints here for auto-creation on landing page
  endpoints = [
          Endpoint(
          'Unique Property Reference Number',
          'uprn',
          "Search for a property via it's unique property refference number. This is a 12 didgit number which contains no characters",),

          Endpoint(
          'Postcode',
          'postcode',
          "Search for a property using it's postcode. This is effective and a valid postcode will return a list of possible addresses.",),

          Endpoint(
          'Single Search',
          'singlesearch',
          "Search for a single address using a single word phrase or paragraph",),

          Endpoint(
          'Typeahead',
          'typeahead',
          "This search types ahead. Auttosugest on steroids basically. Useful if you quickly want a user to find an address",),

          Endpoint(
          'Multiple Address',
          'multiple_address',
          "Search for not just  one address. Several. Get lots of results you can haveanice look through",),
  ]


  for endpoint in endpoints:
    if endpoint.url_title == called_from:
      endpoint.selected = True

  nav_info = [{
      'title': endpoint.title,
      'url': endpoint.url
  } for endpoint in endpoints]
  nav_info.insert(0, {'title': 'Home', 'url': url_for('landing')})

  for endpoint in endpoints:
    endpoint.nav_info = nav_info

  return endpoints
