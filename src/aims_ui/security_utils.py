import re
from .page_error import page_error


def deny_access_error_page(page_name):
  return page_error(
      None,
      page_name,
      override_error_description='You do not have access to this page',
      override_error_name='Access Error')


def check_user_has_access_to_page(page_name, endpoints):
  accessible_pages = [endpoint.page_name for endpoint in endpoints]
  print(page_name, accessible_pages)
  if page_name in accessible_pages:
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
