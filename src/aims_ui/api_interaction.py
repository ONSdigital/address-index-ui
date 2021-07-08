import requests
from . import app


def api(
    url,
    called_from,
    all_user_input,
    ):

  if called_from == 'uprn':
    url = app.config.get('API_URL') + url + all_user_input.get(called_from)
    r = requests.get(url, )
  elif called_from == 'postcode':
    url = app.config.get('API_URL') + url + all_user_input.get(called_from)
    r = requests.get(url, )

  elif called_from == 'singlesearch':
    url = app.config.get('API_URL') + url 
    params =  {'input': all_user_input.get('input')}
    r = requests.get(url, params=params  )
    


  return r
