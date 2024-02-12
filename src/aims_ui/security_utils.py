import re


def checkUserHasAccessToPage(page_name, endpoints):
  accessible_pages = [endpoint.title for endpoint in endpoints]
  print(page_name, accessible_pages)

def detect_xml_injection(input_string):
  # Regular expression pattern for detecting XML injection
  pattern = r'<[^>]+(/)?>'

  # Search for the pattern in the input string
  match = re.search(pattern, input_string)

  # If a match is found, return True
  if match:
    return True

  # If no match is found, return False
  return False
