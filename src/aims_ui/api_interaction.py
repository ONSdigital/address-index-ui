import requests
from . import app 

def api(url, data):
  url = app.config.get('API_URL')+url

  r = requests.post(url, data = data )

  return r

