import datetime
import json
import logging
import os
import xml.etree.ElementTree as ET

import jwt
import requests
from requests.models import Response

from aims_ui import app
from aims_ui.page_controllers.b_multiple_matches.utils.multiple_match_api_utils import get_multiple_match_api_header
from aims_ui.page_helpers.api.api_helpers import get_header, job_api
from aims_ui.page_helpers.api.api_parameters_helpers import cleanup_parameters, format_params_as_string
from aims_ui.app_helpers.classification_utils.validation import classification_is_valid
from aims_ui.page_helpers.google_utils import get_username


def api(url, called_from, all_user_input):
  """API helper for individual API lookups"""
  header = get_header()

  # remove UI params if present
  all_user_input.pop('header_row_export', None)
  all_user_input.pop('display-type', None)
  all_user_input.pop('file_upload', None)

  if (called_from == 'uprn') or (called_from == 'postcode'):
    url = app.config.get('API_URL') + url + all_user_input.get(called_from, '')
  elif (called_from == 'singlesearch') or (called_from == 'radiussearch') or (
      called_from == 'multiple'):
    url = app.config.get('API_URL') + url

  # Change and clean parameters based on page
  cleaned_params = cleanup_parameters(all_user_input, called_from)

  # Format parameters as string for requests
  params = format_params_as_string(cleaned_params)

  r = requests.get(
      url,
      params=params,
      headers=header,
  )

  # Check classification, simulate HTTP error if it's invalid - otherwise return r
  user_classification = all_user_input.get('classificationfilter', '')
  if classification_is_valid(user_classification):
    return r

  return add_classification_error_to_response_object(r)


def add_classification_error_to_response_object(response):
  """Given an API response, inject the error state we would expect for an invalid result."""
  errors_array = [{
      'code':
      15,
      'message':
      'Invalid classification filter value provided. Filters must exactly match a classification code (see /classifications) or use a pattern match such as RD*. There are also four presets: residential, commercial, workplace, and educational.'
  }]

  # Get the existing content
  content = response.json()

  # Update the 'status' and 'errors' fields
  content['status'] = {'code': 400, 'message': 'Bad Request'}
  content['errors'] = errors_array

  # Create a new Response object
  new_response = Response()
  new_response.status_code = 400
  new_response.headers = response.headers
  new_response._content = json.dumps(content).encode('utf-8')
  new_response.encoding = 'utf-8'
  new_response.url = response.url
  new_response.request = response.request

  return new_response


def get_response_attributes(r):
  """ Return high level response attributes """
  # "r" should be result.json() from an API call
  res = r.get('response')

  matchType = res.get('matchtype', 'N/A')
  recommendationCode = res.get('recommendationCode', 'N/A')
  tokenisedOutput = res.get('tokens', {})

  return {
      'tokenisedOutput': tokenisedOutput,
      'matchType': matchType,
      'recommendationCode': recommendationCode
  }


def get_api_auth():
  """Get the auth type for typeahead"""
  api_auth = {}
  if app.config.get('API_AUTH_TYPE') == 'JWT':
    api_auth['API_AUTH_TYPE'] = 'JWT'
    api_auth['PROJECT_DOMAIN'] = app.config.get('PROJECT_DOMAIN')

    current_time = datetime.datetime.utcnow()
    payload = {"exp": current_time + datetime.timedelta(minutes=10)}
    token = jwt.encode(payload,
                       app.config.get('API_JWT_K_VALUE'),
                       algorithm="HS256")
    api_auth['API_JWT_TOKEN'] = token

  elif app.config.get('API_AUTH_TYPE') == 'BASIC_AUTH':
    api_auth['API_AUTH_TYPE'] = 'BASIC_AUTH'
    api_auth['API_BSC_AUTH_USERNAME'] = app.config.get('API_BSC_AUTH_USERNAME')
    api_auth['API_BSC_AUTH_PASSWORD'] = app.config.get('API_BSC_AUTH_PASSWORD')
  return api_auth


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


def job_data_by_job_id(job_id):
  url = f'/bulk-progress/{job_id}'
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

  logging.info('Submmitted Multiple Match UPRN job on endpoint"' + str(url) +
               '"  with UserId as "' + str(username) + '"')

  return r


def submit_mm_job(user, addresses, all_user_input, uprn=False):
  """API helper for job endpoints """
  url = app.config.get('BM_API_URL') + '/bulk'

  header = get_multiple_match_api_header(all_user_input)

  # Add some header data into parameters (if the API needs it as a param)
  all_user_input['uimetadata'] = header.get('uimetadata')

  cleaned_params = cleanup_parameters(all_user_input, 'multiple')
  params = format_params_as_string(cleaned_params)

  addresses = str(addresses).replace('"', '')  # Remove Quotes from address
  addresses = str(addresses).replace("'",
                                     '"')  # Switch quotes for JSON formatting

  r = requests.post(
      url,
      headers=header,
      params=params,
      data=addresses.encode('utf-8'),
  )

  log_message = ("POST Request to " + r.url + "\n\n | Status Code: " +
                 str(r.status_code) + " - " + r.reason +
                 "\n\n | Request Headers: " + str(r.request.headers) +
                 "\n\n | Response Headers: " + str(r.headers) +
                 "\n\n | Response Body: " + r.text)

  logging.info('\nSubmmitted Multiple Match Address Job on endpoint "' +
               str(url) + '"  with UserId as "' + str(get_username()) + '"' +
               'Request details: ' + str(log_message))

  return r


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
      logging.warning(
          'No epoch endpoint found, falling back to Preset Options')
      sorted_epochs = app.config.get('DEFAULT_EPOCH_OPTIONS')
      default = app.config.get('DEFAULT_EPOCH_SELECTED')

      return sorted_epochs, default

    if epoch_call.status_code != 200:
      logging.warning(
          'No epoch endpoint found, falling back to Preset Options')
      sorted_epochs = app.config.get('DEFAULT_EPOCH_OPTIONS')
      default = app.config.get('DEFAULT_EPOCH_SELECTED')

      return sorted_epochs, default

    # If there are no errors from the epoch call, extract the epochs
    epoch_options = json.loads(epoch_call.text).get('epochs')
  else:
    logging.warning('Test mode, falling back to Preset Options')
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
