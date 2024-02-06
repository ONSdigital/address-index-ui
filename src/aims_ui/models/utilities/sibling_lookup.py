from aims_ui import app
import json
import requests
import logging
from flask import request


def multiple_uprn_lookup(siblings):

  user_email = request.headers.get('X-Goog-Authenticated-User-Email', '')

  header = {
      "Content-Type": "application/json",
      "Authorization": app.config.get('JWT_TOKEN_BEARER'),
      "user": user_email.replace('accounts.google.com:', ''),
  }

  url_endpoint = app.config.get('API_URL') + '/addresses/multiuprn'
  siblings = [str(x) for x in siblings]
  data = {'uprns': siblings}

  try:
    class_call = requests.post(url_endpoint, json=data, headers=header)
  except:
    logging.warn(
        'WARNING No multiple UPRN lookup endpoint found, check connection and that you are connecting to the latetst version of the API'
    )
    return False

  if class_call.status_code != 200:
    logging.warn('WARNING Issue on /addresses/multiuprn')
    return False

  return class_call


def getHierarchy(parentUPRN):
  relatives = parentUPRN.get('relatives')
  tables = []

  table_headers = [
      'placeholder',
      'Primary',
      'Secondary',
      'Tertiary',
      'Quaternary',
      'Quinary',
      'Senary',
      'Septenary',
      'Octonary',
  ]
  if not relatives:
    return []
  for level in relatives:
    siblings = level.get('siblings')
    # Get Address list of all siblings
    siblings_info = multiple_uprn_lookup(siblings)
    if siblings_info == False:
      result = []
    else:
      result = siblings_info.json().get('response').get('addresses')

    # Add each child address to table
    for address in result:
      #[{'uprn': '1775115412', 'parentUprn': '1775091131', 'formattedAddress'
      property_name = address.get('formattedAddress')
      property_uprn = address.get('uprn')
      parent_uprn = address.get('parentUprn')

      tables.append([
          table_headers[level.get('level')],
          property_name,
          property_uprn,
          parent_uprn,
      ])

  return tables
