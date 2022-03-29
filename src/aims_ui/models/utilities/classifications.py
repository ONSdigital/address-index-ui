import requests
import json
import re
from aims_ui import app


def get_class_list(classifications_api_url):
  header = {
      "Content-Type": "application/json",
      "Authorization": app.config.get('JWT_TOKEN_BEARER'),
  }

  class_call = requests.get(
      classifications_api_url,
      headers=header,
  )

  class_list = json.loads(class_call.text).get('classifications')
  return class_list


def get_class_subset(classifications_api_url, code):
  header = {
      "Content-Type": "application/json",
      "Authorization": app.config.get('JWT_TOKEN_BEARER'),
  }

  class_call = requests.get(
      classifications_api_url,
      headers=header,
  )

  class_list = json.loads(class_call.text).get('classifications')

  final_list = [code]
  for c in class_list:
    if c.get('code') == code[0]:
      final_list.append(c.get('label'))

  for c in class_list:
    if c.get('code') == code[:2]:
      final_list.append(c.get('label'))

  for c in class_list:
    if c.get('code') == code:
      final_list.append(c.get('label'))

  # Check to remove final string if identical to prior
  length = len(final_list) - 1
  final_word = final_list[length]
  final_list = [x if x != final_word else '' for x in final_list]

  final_string = ''
  for desc in final_list:
    if desc != '':
      final_string = final_string + '[' + desc + '] '

  # Add back final word as all instances have been removed
  final_string = final_string + '[' + final_word + ']'

  return final_string


def get_classification_list(code=None):
  class_list = []
  api_url = app.config.get('API_URL')
  classifications_url = f'{api_url}/classifications'

  class_list = get_class_subset(classifications_url, code)

  return str(class_list)
