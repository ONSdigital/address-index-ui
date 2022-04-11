import os
import json
import requests
from . import app
from io import StringIO, BytesIO
from .models.get_addresses import get_addresses
from .classification_utilities import check_reverse_classification
import urllib
import csv
import logging


def get_epoch_options():
  """Get the result of the Epoch Endpoint and format for radio button use"""
  api_url = app.config.get('API_URL') + '/epochs'

  header = {
      "Content-Type": "application/json",
      "Authorization": app.config.get('JWT_TOKEN_BEARER'),
  }

  epoch_call = requests.get(
      api_url,
      headers=header,
  )

  if epoch_call.status_code != 200:
    logging.warn('No epoch endpoint found, falling back to Preset Options')

    sorted_epochs = app.config.get('DEFAULT_EPOCH_OPTIONS')
    default = app.config.get('DEFAULT_EPOCH_SELECTED')

    return sorted_epochs, default

  epoch_options = json.loads(epoch_call.text).get('epochs')

  # Find default
  # Make epoch Numbers Ints
  default = 0
  epoch_formatted = []
  for epoch in epoch_options:
    if str(epoch.get('default')) == 'true':
      default = epoch.get('epoch')
    # Also add each epoch to a new list in the correct format
    epoch_num = epoch.get('epoch')
    epoch_formatted.append({
        'id': epoch_num,
        'text': epoch_num,
        'value': epoch_num,
        'description': epoch.get('description')
    })

  sorted_epochs = sorted(epoch_formatted, key=lambda d: d['id'])

  return sorted_epochs, default


def api(url, called_from, all_user_input):
  """API helper for individual API lookups"""

  header = {
      "Content-Type": "application/json",
      "Authorization": app.config.get('JWT_TOKEN_BEARER'),
  }

  params = get_params(all_user_input)
  if (called_from == 'uprn') or (called_from == 'postcode'):
    url = app.config.get('API_URL') + url + all_user_input.get(called_from, '')
  elif called_from == 'singlesearch':
    url = app.config.get('API_URL') + url

  r = requests.get(
      url,
      params=params,
      headers=header,
  )

  return r


def get_api_auth():
  """Get the auth type for typeahead"""
  api_auth = {}
  if app.config.get('API_AUTH_TYPE') == 'JWT':
    api_auth['API_AUTH_TYPE'] = 'JWT'
    api_auth['JWT_TOKEN'] = app.config.get('JWT_TOKEN')
    api_auth['PROJECT_DOMAIN'] = app.config.get('PROJECT_DOMAIN')
  elif app.config.get('API_AUTH_TYPE') == 'BASIC_AUTH':
    api_auth['API_AUTH_TYPE'] = 'BASIC_AUTH'
    api_auth['API_BSC_AUTH_USERNAME'] = app.config.get('API_BSC_AUTH_USERNAME')
    api_auth['API_BSC_AUTH_PASSWORD'] = app.config.get('API_BSC_AUTH_PASSWORD')
  return api_auth


def get_params(all_user_input):
  """Return a list of parameters formatted for API header, from class list of inputs"""
  params = ['verbose=True']
  for param, value in all_user_input.items():
    if not str(value):
      continue
    if (os.getenv('FLASK_ENV') == 'development') and (param == 'epoch'):
      # do not add epoch for testing
      continue

    if type(value) == str:
      value = value.replace('%', '')

    # Check if the value is for the classifications, if so, check to see if it needs reversing
    if param == 'classificationfilter':
      value = check_reverse_classification(value)

    quoted_param = urllib.parse.quote_plus(str(param))
    quoted_value = urllib.parse.quote_plus(str(value))
    params.append(quoted_param + '=' + quoted_value)

  return '&'.join(params)


def get_classifications():
  """Return classification endpoint result as json pairs"""
  # All classification list aquesition should come through here

  classifications_api_url = app.config.get('API_URL') + '/classifications'
  header = {
      "Content-Type": "application/json",
      "Authorization": app.config.get('JWT_TOKEN_BEARER'),
  }

  class_call = requests.get(
      classifications_api_url,
      headers=header,
  )

  if class_call.status_code != 200:
    logging.warn(
        'No Class Code endpoint found, falling back to Preset Options')
    class_list = app.config.get('DEFAULT_CLASSIFICATION_CLASS_LIST')

    return class_list

  class_list = json.loads(class_call.text).get('classifications')

  return class_list
