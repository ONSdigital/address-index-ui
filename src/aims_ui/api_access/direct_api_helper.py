
import requests

from aims_ui import app
from aims_ui.page_helpers.api.api_helpers import get_header


def uprn_lookup(uprn):
  """API helper for UPRN lookups"""
  header = get_header()

  url = app.config.get('API_URL') + '/addresses/uprn/' + str(uprn)

  r = requests.get(
      url,
      headers=header,
  )

  return r

