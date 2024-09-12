import re
from aims_ui.page_controllers.f_error_pages.page_error import page_error
from aims_ui.page_helpers.error.error_utils import error_page_no_access
from .google_utils import get_current_group


def check_user_has_access_to_page(page_name):
  current_group = get_current_group()
  if not current_group:
    return error_page_no_access(page_name)

  current_access = current_group.get('allowed_pages', [])

  if page_name in current_access:
    return True

  return error_page_no_access(page_name)


def detect_xml_injection(input_string):
  # Regular expression pattern for detecting XML injection
  pattern = r'<[^>]+(/)?>'

  # Search for the pattern in the input string
  match = re.search(pattern, input_string)

  if match:
    return True
  return False
