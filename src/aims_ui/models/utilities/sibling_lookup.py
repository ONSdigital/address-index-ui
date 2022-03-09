from aims_ui import app
from aims_ui.table_utils import create_table
import requests
import urllib


def get_params(all_user_input):
  """Return a list of parameters formatted for API header, from class list of inputs"""
  params = ['verbose=True']
  for param, value in all_user_input.items():
    if not str(value):
      continue

    if type(value) == str:
      value = value.replace('%', '')

    # Check if the value is for the classifications, if so, check to see if it needs reversing
    if param == 'classificationfilter':
      value = check_reverse_classification(value)

    quoted_param = urllib.parse.quote_plus(str(param))
    quoted_value = urllib.parse.quote_plus(str(value))
    params.append(quoted_param + '=' + quoted_value)

  return '&'.join(params)


def api(url, called_from, all_user_input):
  """API helper, all pages go through here to interact with API"""

  header = {
      "Content-Type": "application/json",
  }

  params = get_params(all_user_input)
  url = app.config.get('API_URL') + str(url) + str(
      all_user_input.get(called_from, ''))

  r = requests.get(
      url,
      params=params,
      headers=header,
  )

  return r


def getHierarchy(parentUPRN):
  relatives = parentUPRN.get('relatives')

  tables = []

  table_headers = [
      'placeholder', 'Primary', 'Secondary', 'Teriternary', 'Quaternaty'
  ]
  ths = ['UPRN', 'Property Name']
  trs = []

  all_relatives = []
  for level in relatives:
    for sibling_uprn in level.get('siblings'):
      result = api(
          '/addresses/uprn/',
          'uprn',
          {'uprn': sibling_uprn},
      )
      address = result.json().get('response').get('address')
      property_name = address.get('formattedAddress')
      property_uprn = address.get('uprn')

      tables.append([
          table_headers[level.get('level')],
          property_name,
          property_uprn,
      ])

  test_table = [[tables[0][1], tables[0][2]]]
  table1 = create_table(['Name', 'UPRN'], test_table)

  return tables
