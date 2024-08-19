from aims_ui.page_error import page_error
from aims_ui.page_helpers.google_utils import get_username
from requests.exceptions import ConnectionError, Timeout
import logging
""" Handle Errors Connecting to and in the response of the API - logging and user response """


def basic_logging_info(page_name, user_input):
  return f'User: "{get_username()}" experienced an issue on page: "{page_name}", having entered: "{user_input}". Issue is: '

def error_page_no_access(page_name):
  logging.warning(
      basic_logging_info(page_name, 'NA') + f'User not in group with access to "{page_name}" page') 
  return page_error(
      page_name,
      'You do not have access to this page',
      [f'If you think you should have access, please contact the AIMS team and request access to the "{page_name}" page.',
       'Contact can be made through the link at the bottom of the page'],)


def error_page_api_request(page_name, user_input, error):
  if isinstance(error, ConnectionError):
    return error_page_connection(page_name, user_input, error)
  elif isinstance(error, Timeout):
    return error_page_timeout(page_name, user_input, error)
  else:
    return error_page_unknown(page_name, user_input, error)


def error_page_unknown(page_name, user_input, error):
  """ Return error page for unknown error """
  logging.error(
      basic_logging_info(page_name, user_input) + f' Generic Error: "{error}"')
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
  logging.error(
      basic_logging_info(page_name, user_input) + f'Timeout Error: "{error}"')
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
  logging.warning(
      basic_logging_info(page_name, user_input) + ' "XML Attack Detected"')
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
  logging.error(
      basic_logging_info(page_name, user_input) + f'"{error_details_full}"')

  return page_error(
      page_name,
      'Connection Error',
      [
          'There was an error connecting to the AIMS API.',
          'Please try again later.',
          'If this problem persists, please contact the AIMS team using the link at the bottom of the page.',
      ],
  )


def error_page_api_response(page_name, user_input, result):
  status_code = result.status_code
  if status_code == 429:
    logging.warning(
        basic_logging_info(page_name, user_input) +
        f' "Rate Limit Error": "{result.json()}"')
    return page_error(
        page_name,
        'Rate Limit Error',
        [
            'The API is currently under exceptional load and your request cannot be processed at this time.',
            'Please try again later.',
        ],
    )

  if status_code == 500:
    logging.error(
        basic_logging_info(page_name, user_input) +
        f' "Server Error": "{result.json()}"')
    return page_error(
        page_name,
        'Internal Server Error',
        [
            'There was an API error processing your request.',
            'If this problem persists, please contact the AIMS team using the link at the bottom of the page.',
        ],
    )

  if status_code == 400:
    logging.error(
        basic_logging_info(page_name, user_input) +
        f' "Bad Request Error": "{result.json()}"')
    return page_error(
        page_name,
        'Bad Request',
        [
            'There was an error with the request you submitted.',
            'If this problem persists, please contact the AIMS team using the link at the bottom of the page.',
        ],
    )

  if status_code == 401:
    logging.error(
        basic_logging_info(page_name, user_input) +
        f' "Authentication Error": "{result.json()}"')
    return page_error(
        page_name,
        'Authentication Error',
        [
            'There was an error with your authentication.',
            'Please try logging in again or refreshing your page.',
            'If this problem persists, please contact the AIMS team using the link at the bottom of the page.',
        ],
    )
