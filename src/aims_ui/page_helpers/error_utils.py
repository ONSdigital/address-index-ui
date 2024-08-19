from aims_ui.page_error import page_error
from aims_ui.page_helpers.google_utils import get_username
import logging

# Idea is so that all errors and logging for those errors goes through this file
# This should make error handling in other files much cleaner and less repetitive


def error_page_xml(page_name, user_input):
  """ Return error page for XML attack """
  logging.warning(
      f'XML Attack Detected on page: "{page_name}". \nThe user "{get_username()}" entered: "{user_input}"'
  )
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
      f'The user {get_username()} experienced a Connection Error on page: "{page_name}". \nError Details: "{error_details_full}"'
  )
  return page_error(
      page_name,
      'Connection Error',
      [
          'There was an error connecting to the AIMS API.',
          'Please try again later.',
          'If this problem persists, please contact the AIMS team using the link at the bottom of the page.',
      ],
  )
