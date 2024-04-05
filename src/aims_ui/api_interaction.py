import os
import logging
import json
import requests
from . import app
from io import StringIO, BytesIO
from .models.get_addresses import get_addresses
from .classification_utilities import check_reverse_classification
from .api_helpers import get_header
from .google_utils import get_username
from flask import request
import urllib
import csv
import logging
import xml.etree.ElementTree as ET
import jwt
import datetime


def get_response_attributes(r):
  """ Return high level response attributes """
  # "r" should be result.json() from an API call
  res = r.get('response')

  matchType = res.get('matchtype', 'N/A')
  recommendationCode = res.get('recommendationCode', 'N/A')

  return {'matchType': matchType, 'recommendationCode': recommendationCode}


def get_api_auth():
  """Get the auth type for typeahead"""
  api_auth = {}
  if app.config.get('API_AUTH_TYPE') == 'JWT':
    api_auth['API_AUTH_TYPE'] = 'JWT'
    api_auth['PROJECT_DOMAIN'] = app.config.get('PROJECT_DOMAIN')

    current_time = datetime.datetime.utcnow()
    payload = {"exp": current_time + datetime.timedelta(minutes=10)}
    token = jwt.encode(payload,
                       app.config.get('JWT_K_VALUE'),
                       algorithm="HS256")
    api_auth['API_JWT_TOKEN'] = token

  elif app.config.get('API_AUTH_TYPE') == 'BASIC_AUTH':
    api_auth['API_AUTH_TYPE'] = 'BASIC_AUTH'
    api_auth['API_BSC_AUTH_USERNAME'] = app.config.get('API_BSC_AUTH_USERNAME')
    api_auth['API_BSC_AUTH_PASSWORD'] = app.config.get('API_BSC_AUTH_PASSWORD')
  return api_auth


def get_epoch_options():
  """Get the result of the Epoch Endpoint and format for radio button use"""
  api_url = app.config.get('API_URL') + '/epochs'

  header = get_header(username=False)

  if os.getenv("FLASK_ENV") != "testing":
    try:
      epoch_call = requests.get(
          api_url,
          headers=header,
      )
    except:
      logging.warn('No epoch endpoint found, falling back to Preset Options')
      sorted_epochs = app.config.get('DEFAULT_EPOCH_OPTIONS')
      default = app.config.get('DEFAULT_EPOCH_SELECTED')

      return sorted_epochs, default

    if epoch_call.status_code != 200:
      logging.warn('No epoch endpoint found, falling back to Preset Options')
      sorted_epochs = app.config.get('DEFAULT_EPOCH_OPTIONS')
      default = app.config.get('DEFAULT_EPOCH_SELECTED')

      return sorted_epochs, default

    # If there are no errors from the epoch call, extract the epochs
    epoch_options = json.loads(epoch_call.text).get('epochs')
  else:
    logging.warn('Test mode, falling back to Preset Options')
    sorted_epochs = app.config.get('DEFAULT_EPOCH_OPTIONS')
    default = app.config.get('DEFAULT_EPOCH_SELECTED')

    return sorted_epochs, default

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

  sorted_epochs = sorted(epoch_formatted,
                         key=lambda d: int(d['id']),
                         reverse=True)

  return sorted_epochs, default


def job_data_by_job_id(job_id):
  url = f'/bulk-progress/{job_id}'
  r = job_api(url)
  return r


def job_result_formatter(job_id):
  # TODO Might switch to the new results endpoint
  buttonContent = job_result_by_job_id(job_id)

  return buttonContent


def job_result_by_job_id(job_id):
  url = f'/bulk-result/{job_id}'
  r = job_api(url)
  r = r.json()
  # We must check if the output still exists (it may have been cleaned up)
  downloadableResult = check_url(r.get('signedUrl'), job_id)
  return downloadableResult


def check_url(url, job_id):
  try:
    response = requests.get(url)
    if response.status_code == 200:
      buttonUrl = f'<a href="/downloads/googlefiledownload{job_id}">Download Job {job_id} Here</a>'
      return buttonUrl
    else:
      # Check if the error message is in XML format
      try:
        root = ET.fromstring(response.text)
        error_code = root.find('Code').text
        if error_code == 'NoSuchBucket':
          return "Unavailable"
        else:
          logging.info(
              f"Error, HTTP Status Code: {response.status_code}, Error: {error_code}"
          )
      except ET.ParseError:
        logging.info("Error, the url is no longer available")
  except requests.exceptions.RequestException as err:
    if url == None:
      return "Not Yet Available"


def all_jobs():
  url = f'/jobs'
  r = job_api(url)
  return r


def job_data_by_user_id(user_id):
  url = f'/jobs?userid={user_id}'
  r = job_api(url)
  return r


def submit_uprn_mm_job(uprns_and_ids, all_user_input):
  """API helper for job endpoints """
  url = app.config.get('API_URL') + '/addresses/multiuprn'

  username = get_username()
  header = get_header(username=True)

  just_uprns = {"uprns": [item["uprn"] for item in uprns_and_ids]}
  just_uprns_stringified = json.dumps(just_uprns)

  r = requests.post(
      url,
      headers=header,
      data=just_uprns_stringified,
  )

  logging.info('Submmitted Multi-UPRN match on endpoint"' + str(url) +
               '"  with UserId as "' + str(username) + '"')

  return r


def submit_mm_job(user, addresses, all_user_input, uprn=False):
  """API helper for job endpoints """
  url = app.config.get('BM_API_URL') + '/bulk'

  # Change the paf-nag default selection
  if all_user_input.get('paf-nag-prefference') == 'PAF':
    all_user_input['pafdefault'] = 'true'
  del all_user_input['paf-nag-prefference']

  params = get_params(all_user_input, removeVerbose=True)

  username = get_username()
  tag_name = '::' + str(all_user_input.get('name', '')[:25] + '::')
  note_data = username + tag_name

  header = get_header()

  header['user'] = note_data 

  addresses = str(addresses).replace('"', '')  # Remove Quotes from address
  addresses = str(addresses).replace(
      "'", '"')  # Replace quotes for correct JSON formatting

  r = requests.post(
      url,
      headers=header,
      params=params,
      data=addresses.encode('utf-8'),
  )

  logging.info('Submmitted MMJob on endpoint"' + str(url) +
               '"  with UserId as "' + str(username) + '"')

  return r


def job_api(url):
  """API helper for job endpoints """
  url = app.config.get('BM_API_URL') + url

  header = get_header()

  r = requests.get(
      url,
      headers=header,
  )

  return r


def api(url, called_from, all_user_input):
  """API helper for individual API lookups"""
  header = get_header()

  params = get_params(all_user_input)
  if (called_from == 'uprn') or (called_from == 'postcode'):
    url = app.config.get('API_URL') + url + all_user_input.get(called_from, '')
  elif (called_from == 'singlesearch'):
    url = app.config.get('API_URL') + url

  # bulks run without verbose for speed
  if (called_from == 'multiple'):
    params = params.replace('verbose=True', 'verbose=False')
    url = app.config.get('API_URL') + url

  r = requests.get(
      url,
      params=params,
      headers=header,
  )

  return r


def get_params(all_user_input, removeVerbose=False):
  """Return a list of parameters formatted for API header, from class list of inputs"""
  params = ['verbose=True']
  if removeVerbose:
    params = []

  for param, value in all_user_input.items():
    if not str(value):
      continue
    if (os.getenv('FLASK_ENV') == 'development') and (param == 'epoch'):
      # do not add epoch for testing
      continue
    if param == 'historical':
      if str(value) == 'None':
        value = 'False'

    if type(value) == str:
      value = value.replace('%', '')
      value = value.replace('"', '')

    # Check if the value is for the classifications, if so, check to see if it needs reversing
    if param == 'classificationfilter':
      value = check_reverse_classification(value)

    # Replace paf-nag-prefference
    if str(param) == 'paf-nag-prefference':
      param = 'pafdefault'
      value = 'true' if value == 'PAF' else 'false'

    quoted_param = urllib.parse.quote_plus(str(param))
    quoted_value = urllib.parse.quote_plus(str(value))

    params.append(quoted_param + '=' + quoted_value)

  return '&'.join(params)


def get_classifications():
  """Return classification endpoint result as json pairs"""
  # All classification list aquesition should come through here

  classifications_api_url = app.config.get('API_URL') + '/classifications'
  header = get_header(username=False)

  if os.getenv("FLASK_ENV") != "testing":
    try:
      class_call = requests.get(
          classifications_api_url,
          headers=header,
      )
    except:
      logging.warn(
          'No Class Code endpoint found, falling back to Preset Options')
      class_list = app.config.get('DEFAULT_CLASSIFICATION_CLASS_LIST')

      return class_list

    if class_call.status_code != 200:
      logging.warn(
          'No Class Code endpoint found, falling back to Preset Options')
      class_list = app.config.get('DEFAULT_CLASSIFICATION_CLASS_LIST')

      return class_list

    # If there were no errors reaching the endpoint
    class_list = json.loads(class_call.text).get('classifications')
  else:
    class_list = app.config.get('DEFAULT_CLASSIFICATION_CLASS_LIST')

  return class_list
