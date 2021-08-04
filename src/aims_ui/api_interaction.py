import os
import json
import requests
from . import app
from flask import render_template
from .models.get_endpoints import get_endpoints

def get_params(all_user_input):
  """Return a list of aparameters formatted for API header, from class list of inputs"""
  params = 'verbose=True&'
  for param in all_user_input.keys():
    # Do not add epoch for testing
    if (param != 'epoch') and (os.getenv('FLASK_ENV') == 'development'):
      if str(all_user_input.get(param)) != '':
        params = params + str(param) +'='+ str(all_user_input.get(param)).replace('%','') + '&'

  params = params[:-2] if params != '' else ''

  return params

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
