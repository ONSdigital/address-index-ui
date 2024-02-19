import re
from .page_error import page_error
from .google_utils import get_username
from . import app


def get_current_group():
  access_groups = app.config.get('USER_GROUPS')
  username = get_username()

  for group in access_groups:
    if username in group.get('usernames', []):
      return group
  return False


def deny_access_error_page(page_name):
  return page_error(
      None,
      page_name,
      override_error_description='You do not have access to this page',
      override_error_name='Access Error')


def check_user_has_access_to_page(page_name, endpoints):
  current_group = get_current_group()
  if not current_group:
    return deny_access_error_page(page_name)

  current_access = current_group.get('allowed_pages', [])
  
  if page_name in current_access:
    return True
  return deny_access_error_page(page_name)


def detect_xml_injection(input_string):
  # Regular expression pattern for detecting XML injection
  pattern = r'<[^>]+(/)?>'

  # Search for the pattern in the input string
  match = re.search(pattern, input_string)

  if match:
    return True
  return False
