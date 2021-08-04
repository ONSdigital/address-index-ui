import os
import json
import requests
from . import app
from flask import render_template
from .models.get_endpoints import get_endpoints
import urllib

def get_params(all_user_input):
  """Return a list of aparameters formatted for API header, from class list of inputs"""
    
  params = ['verbose=True']
  for param, value in all_user_input.items():
    if not str(value):
      continue
    if (os.getenv('FLASK_ENV') == 'development') and (param == 'epoch'):
      # do not add epoch for testing
      continue
    quoted_param = urllib.parse.quote_plus(str(param))
    quoted_value = urllib.parse.quote_plus(str(value))
    params.append(quoted_param + '=' + quoted_value)  
  
  return '&'.join(params)


def api(
    url,
    called_from,
    all_user_input):
  """API helper, all pages go through here to interact with API"""

  header = {"Content-Type": "application/json",}

  if (called_from == 'uprn') or (called_from == 'postcode'):
    url = app.config.get('API_URL') + url + all_user_input.get(called_from)
    params = get_params(all_user_input)
    r = requests.get(url, params=params, headers=header, )

  elif called_from == 'singlesearch':
    url = app.config.get('API_URL') + url
    proposed_params = {k: v for k, v in all_user_input.items() if v}
    params = get_params(all_user_input)
    r = requests.get(url, params=params, headers=header, )

  return r
