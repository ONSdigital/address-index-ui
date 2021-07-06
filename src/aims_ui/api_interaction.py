import requests
from . import app


def api(url, called_from, uprn=None,):
  if called_from == 'uprn':
    url = app.config.get('API_URL') + url + uprn 
    r = requests.get(url, )

  return r
