from aims_ui.page_helpers.google_utils import get_username
import logging


def basic_logging_info(page_name, user_input):
  return f'User: "{get_username()}" experienced an issue on page: "{page_name}", having entered: "{user_input}". Issue is: '

# Handle all warning logs
def log_warn(page_name, user_input, message):
  bsc = basic_logging_info(page_name, user_input)

  logging.warning(bsc + message)

# Handle all error logs
def log_err(page_name, user_input, message):
  bsc = basic_logging_info(page_name, user_input)

  logging.error(bsc + message)
