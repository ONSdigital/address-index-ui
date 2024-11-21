from requests.exceptions import ConnectionError, Timeout

from aims_ui.page_controllers.f_error_pages.page_error import page_error
from aims_ui.page_controllers.f_error_pages.page_error_annotation_single import page_error_annotation_single
from aims_ui.page_controllers.f_error_pages.page_service_error import page_service_error
from aims_ui.page_helpers.error.error_logging import log_err, log_warn
""" Handle Errors Messages for User when connecting to and in the response of the API """


def get_primary_error_message(full_response, page_name, user_input):
  """ Get the primary error message from the API response - it could be in mutliple places """
  # Handle HTML responses (Can happen if the gateway is completely down)
  if 'The server encountered a temporary error and could not complete your request.<p>Please try again in 30 seconds' in full_response:
    return 'The server encountered a temporary error and could not complete your request.<p>Please try again in 30 seconds. This is probably because the Gateway is down.'

  # Handle responses that aren't JSON
  try:
    # {'response': 'Error calling API', 'status': {'code': 400, 'message': 'Missing parameter: input'}}
    json_result = full_response.json()
    api_response = json_result.get('status', {})
  except:
    # If there was a problem parsing the JSON, return a generic error message and log
    log_err(page_name, user_input,
            f'Error parsing JSON from the API: "{full_response}"')
    return 'Error parsing issue from the API'

  # In some cases the error will be in full_response.status.message "Missing parameter: input"
  # In other cases the error will be in full_repsonse.errors [{'code':8, 'message': 'Limit parameter is too large'}]
  primary_error_message = api_response.get(
      'message', 'No further information provided by the API')
  if json_result.get('errors'):
    # There are errors in the 'errors' field, so use the first one
    primary_error_message = json_result.get('errors')[0].get('message')

  return primary_error_message


def error_page_api_request(page_name, user_input, error):
  if isinstance(error, ConnectionError):
    return error_page_connection(page_name, user_input, error)
  elif isinstance(error, Timeout):
    return error_page_timeout(page_name, user_input, error)
  else:
    return error_page_unknown(page_name, user_input, error)


def error_page_no_access(page_name):
  log_warn(page_name, 'NA',
           f'User not in group with access to "{page_name}" page')
  return page_error(
      page_name,
      'You do not have access to this page',
      [
          f'If you think you should have access, please contact the AIMS team and request access to the "{page_name}" page.',
          'Contact can be made through the link at the bottom of the page'
      ],
  )


def error_page_unknown(page_name, user_input, error):
  """ Return error page for unknown error """
  log_err(page_name, user_input, f'Generic Error: "{error}"')
  return page_service_error(
      page_name,
      'Unknown Error',
      [
          'There was an unknown error connecting to the AIMS API.',
          'Please try again later.',
          'If this problem persists, please contact the AIMS team using the link at the bottom of the page.',
      ],
  )


def error_page_timeout(page_name, user_input, error):
  """ Return error page for timeout error """
  log_err(page_name, user_input, f'Timeout Error: "{error}"')
  return page_service_error(
      page_name,
      'Timeout Error',
      [
          'There was a timeout error connecting to the AIMS API.',
          'This could be because the request was too large.',
          'Try limiting the number of results, or using a more specific query.',
          'If this problem persists, please contact the AIMS team using the link at the bottom of the page.',
      ],
  )


def error_page_xml(page_name, user_input):
  """ Return error page for XML attack """
  log_warn(page_name, user_input, 'XML Attack Detected')
  return page_error(
      page_name,
      'XML Attack Detected. This incident will be reported.',
      [
          'If you beleive this is an eroneous detection, please contact the AIMS team using the link at the bottom of the page.',
          'You can also try removing special characters from the address and try again.',
      ],
  )


def error_page_connection(page_name, user_input, error):
  """ Return error page for connection error """
  error_details_full = f"Exception Type: {type(error).__name__}\nError Details: {str(error)}"
  log_err(page_name, user_input, f'Connection Error: "{error_details_full}"')

  return page_service_error(
      page_name,
      'Connection Error',
      [
          'There was an error connecting to the AIMS API.',
          'Please try again later.',
          'If this problem persists, please contact the AIMS team using the link at the bottom of the page.',
      ],
  )


def clean_api_response(result):
  try:
    return str(result.json())
  except:
    return str(result.text)


def error_page_api_response(page_name, user_input, result):
  status_code = int(result.status_code)
  clean_result = clean_api_response(result)

  # Error message from status message or first error in 'errors'
  primary_error_message = get_primary_error_message(page_name, user_input,
                                                    result)

  if status_code == 429:
    log_warn(page_name, user_input, f'Rate Limit Error: "{clean_result}"')
    return page_service_error(
        page_name,
        'Rate Limit Error',
        [
            'The API is currently under exceptional load and your request cannot be processed at this time.',
            'Please try again later.',
            primary_error_message,
        ],
    )

  if status_code == 500:
    log_err(page_name, user_input, f'Server Error: "{clean_result}"')
    return page_service_error(
        page_name,
        'Internal Server Error',
        [
            'There was an API error processing your request.',
            'If this problem persists, please contact the AIMS team using the link at the bottom of the page.',
            primary_error_message
        ],
    )

  if status_code == 400:
    log_err(page_name, user_input, f'Bad Request Error: "{clean_result}"')
    # Handle errors that the API has a suggesgion to fix! (i.e. "input" cannot be empty)
    primary_error_message = get_primary_error_message(result, page_name,
                                                      user_input)

    return page_error_annotation_single(page_name, user_input,
                                        primary_error_message)

  if status_code == 404:
    log_err(page_name, user_input, f'Not Found Error: "{clean_result}"')
    # 404 errors that relate to blank input fields, otherwise a generic error message is shown
    primary_error_message = get_primary_error_message(result, page_name,
                                                      user_input)
    if page_name == 'postcode':
      primary_error_message = 'Not found error. This is likely due to a blank search feild. Please check your inputs.'

    return page_error_annotation_single(page_name,
                                        user_input,
                                        primary_error_message,
                                        override_input_name=page_name)

  if status_code == 401:
    log_err(page_name, user_input, f'Authentication Error: "{clean_result}"')
    return page_service_error(
        page_name,
        'Authentication Error',
        [
            'There was an error with your authentication.',
            'Please try logging in again or refreshing your page.',
            'If this problem persists, please contact the AIMS team using the link at the bottom of the page.',
            primary_error_message,
        ],
    )

  if status_code == 502:
    log_err(page_name, user_input, f'Bad Gateway Error: "{clean_result}"')
    return page_service_error(
        page_name,
        'Bad Gateway Error',
        [
            'An issue occured from a bad gateway.',
            'If this problem persists, please contact the AIMS team using the link at the bottom of the page.',
            primary_error_message,
        ],
    )

  log_err(page_name, user_input, f'Unknown HTTP error code: "{clean_result}"')
  return page_service_error(
      page_name,
      'Unknown issue',
      [
          'An issue occured, we don\'t know much else.',
          'If this problem persists, please contact the AIMS team using the link at the bottom of the page.',
          primary_error_message,
      ],
  )
