import requests
import json
import re
from aims_ui import app


def get_class_list(classifications_api_url):
  classifications = requests.get(classifications_api_url)
  return json.loads(classifications.text)


def get_class_subset(classifications_api_url, code=None):

  class_call = requests.get(classifications_api_url)
  class_list = json.loads(class_call.text)

  subset_list = []

  if code:

    if len(code) == 1:
      for classification in class_list['classifications']:
        if re.match(r'^(%s)[A-Z]$' % code, classification['code']):
          subset_list.append({
              "code": classification['code'].encode("utf-8"),
              "label": classification['label'].encode("utf-8")
          })
    elif len(code) == 2:
      for classification in class_list['classifications']:
        if re.match(r'^(%s)[0-9]{2}$' % code, classification['code']):
          subset_list.append({
              "code": classification['code'].encode("utf-8"),
              "label": classification['label'].encode("utf-8")
          })
    elif len(code) == 4:
      for classification in class_list['classifications']:
        if re.match(r'^(%s)[A-Z]{2}$' % code, classification['code']):
          subset_list.append({
              "code": classification['code'].encode("utf-8"),
              "label": classification['label'].encode("utf-8")
          })
  else:
    for classification in class_list['classifications']:
      if re.match(r'^[A-Z]$', classification['code']):
        subset_list.append({
            "code": classification['code'].encode("utf-8"),
            "label": classification['label'].encode("utf-8")
        })

  return subset_list


def get_classification_list(code=None):
  class_list = []
  api_url = app.config.get('API_URL')
  classifications_url = f'{api_url}/classifications'

  for classification in get_class_subset(classifications_url, code):
    class_list.append(' [ ' + str(classification['label'].decode()) + ' ] ')

  return ''.join(class_list)
