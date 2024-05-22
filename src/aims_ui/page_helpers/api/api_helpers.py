import requests
from aims_ui import app
from aims_ui.page_helpers.google_utils import get_username


def get_header(username=True, bulk=False):
  """ Get defaut header for API requests """
  api_jwt = app.config.get('API_JWT_TOKEN_BEARER')
  bulk_jwt = app.config.get('BM_JWT_TOKEN_BEARER')
  auth = bulk_jwt if bulk else api_jwt

  header = {
      "Content-Type": "application/json",
      "Authorization": auth,
  }

  if username:
    header['user'] = get_username()

  return header


def job_api(url):
  """API helper for job endpoints """
  url = app.config.get('BM_API_URL') + url

  header = get_header(bulk=True)

  r = requests.get(
      url,
      headers=header,
  )

  return r
