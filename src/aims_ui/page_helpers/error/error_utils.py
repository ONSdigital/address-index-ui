from aims_ui.page_controllers.f_error_pages.page_error import page_error
from aims_ui.page_helpers.error.error_logging import basic_logging_info, log_warn, log_err
from requests.exceptions import ConnectionError, Timeout
""" Handle Errors Messages for User when connecting to and in the response of the API """


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
  return page_error(
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
  return page_error(
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

  return page_error(
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
  status_code = result.status_code
  clean_result = clean_api_response(result)

  if status_code == 429:
    log_warn(page_name, user_input, f'Rate Limit Error: "{clean_result}"')
    return page_error(
        page_name,
        'Rate Limit Error',
        [
            'The API is currently under exceptional load and your request cannot be processed at this time.',
            'Please try again later.',
        ],
    )

  if status_code == 500:
    log_err(page_name, user_input, f'Server Error: "{clean_result}"')
    return page_error(
        page_name,
        'Internal Server Error',
        [
            'There was an API error processing your request.',
            'If this problem persists, please contact the AIMS team using the link at the bottom of the page.',
        ],
    )

  if status_code == 400:
    log_err(page_name, user_input, f'Bad Request Error: "{clean_result}"')
    return page_error(
        page_name,
        'Bad Request',
        [
            'There was an error with the request you submitted.',
            'If this problem persists, please contact the AIMS team using the link at the bottom of the page.',
        ],
    )

  if status_code == 401:
    log_err(page_name, user_input, f'Authentication Error: "{clean_result}"')
    return page_error(
        page_name,
        'Authentication Error',
        [
            'There was an error with your authentication.',
            'Please try logging in again or refreshing your page.',
            'If this problem persists, please contact the AIMS team using the link at the bottom of the page.',
        ],
    )

  if status_code == 502:
    log_err(page_name, user_input, f'Bad Gateway Error: "{clean_result}"')
    return page_error(
        page_name,
        'Bad Gateway Error',
        [
            'An issue occured from a bad gateway.',
            'If this problem persists, please contact the AIMS team using the link at the bottom of the page.',
        ],
    )

  log_err(page_name, user_input, f'Unknown HTTP error code: "{clean_result}"')
  return page_error(
      page_name,
      'Unknown issue',
      [
          'An issue occured, we don\t know much else.',
          'If this problem persists, please contact the AIMS team using the link at the bottom of the page.',
      ],
  )


