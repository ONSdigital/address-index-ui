from .builder import get_classification_file_content_as_dict
from requests.models import Response
import json

def get_class_info_from_code(provided_code):
  """ Given a classification code, get the dict object with full info """
  class_list = get_classification_file_content_as_dict()
  # [ {'code': 'ZW99TP', 'label': 'Temple', 'primary_code': 'Z', 'secondary_code': 'W', ...}, ...]

  for class_info in class_list:
    if class_info.get('code') == provided_code:
      return class_info

  return None

def get_class_subset(code):
  # Given a classification code, get the full String of Each Subclass
  class_list = get_classification_file_content_as_dict()
  # [ {'code': 'ZW99TP', 'label': 'Temple', 'primary_code': 'Z', 'secondary_code': 'W', ...}, ...]

  code_info = get_class_info_from_code(code)

  # Collect hierarchy descriptions in order
  hierarchy = [
    code_info.get('primary_desc', ''),
    code_info.get('secondary_desc', ''),
    code_info.get('tertiary_desc', ''),
    code_info.get('quaternary_desc', ''),
  ]

  hierarchy_string_array = ['[' + x + ']' for x in hierarchy if x != '']
  hierarchy_string = ' '.join(hierarchy_string_array)

  return hierarchy_string

def get_classification_list_as_string(code=None):
  class_list = []
  class_list = get_class_subset(code)

  return str(class_list)

