import json

from requests.models import Response

from aims_ui.page_controllers.d_misc_functionality.download_utils.autosuggest import get_autosuggest_list


def check_reverse_classification(classification):
  """ Given a string classification, return the code version """

  autosuggest_list = get_autosuggest_list()

  # Default to returning the original classification
  to_return = classification
  for category in autosuggest_list:
    if classification == category.get('category'):
      to_return = category.get('en') + '*'

  # Standardise wildcard to all inputs except blank
  if classification == '':
    return ''

  return to_return + '*'


def check_valid_classification(all_user_input, response):
  """Explicit check against full list of classifications as API only checks strucutre"""

  # Get the default list of classifications
  classifications = get_autosuggest_list()
  user_classification = all_user_input.get('classificationfilter', '')

  # Get the reversed version of the user input
  user_classification = check_reverse_classification(user_classification)
  user_classification = user_classification.replace('*', '')
  # The user_classification should now be in code format e.g. 'R'

  # [{'en': 'C', 'category': 'Commercial'}, ...
  # Get just the codes to compare to the user input
  classification_codes = [
      classification.get('en') for classification in classifications
  ]
  classification_codes.append('')

  if user_classification in classification_codes:
    return response
  return add_classification_error_to_response_object(response)


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
