import os
import requests
from . import app

def get_params(all_user_input):
  """Return a list of aparameters formatted for API header, from class list of inputs"""
  params = ''
  for param in all_user_input.keys():
    # Do not add epoch for testing
    if (param != 'epoch') and (os.getenv('FLASK_ENV') == 'development'):
      if str(all_user_input.get(param)) != '':
        params = params + str(param) +'='+ str(all_user_input.get(param)) + '&&'

  params = params[:-2] if params != '' else ''

  return params

def api(
    url,
    called_from,
    all_user_input):
  """API helper, all pages go through here to interact with API"""

  if (called_from == 'uprn') or (called_from == 'postcode'):
    url = app.config.get('API_URL') + url + all_user_input.get(called_from)
#    r = requests.get(url, )
    params = get_params(all_user_input)
    header = {"Content-Type": "application/json",}

    print(url)
    print(all_user_input)
    print(params, header)
    r = requests.get(url, params=params, headers=header, timeout=1000000., verify=False)

  elif called_from == 'singlesearch':
    url = app.config.get('API_URL') + url
    params = {'input': all_user_input.get('input')}
    print("")
    print("Old params are")
    print(params)

    print("")
    print("All user input is ")
    print(all_user_input)
    print("")
    print("proposed:")
    proposed_params = {k: v for k, v in all_user_input.items() if v}
    proposed_params['epoch'] = ''
    print(proposed_params)

    r = requests.get(url, params=params)

  return r
