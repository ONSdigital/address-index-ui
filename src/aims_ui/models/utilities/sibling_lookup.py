from aims_ui import app
import json 
import requests

def multiple_uprn_lookup(siblings):
  header = {
        "Content-Type": "application/json",
        "Authorization": app.config.get('JWT_TOKEN'),
    }

  url_endpoint = app.config.get('API_URL') + '/addresses/multiuprn'
  siblings = [str(x) for x in siblings]
  data = {'uprns': siblings}
  class_call = requests.post(
      url_endpoint,
      json=data,
      headers=header)

  return class_call

def getHierarchy(parentUPRN):
  relatives = parentUPRN.get('relatives')
  tables = []

  table_headers = [
      'placeholder', 'Primary', 'Secondary', 'Tertiary', 'Quaternary'
  ]

  for level in relatives:
    siblings =  level.get('siblings')
    # Get Address list of all siblings
    siblings_info = multiple_uprn_lookup(siblings)
    result = siblings_info.json().get('response').get('addresses')

    # Add each child address to table
    for address in result:
      #[{'uprn': '1775115412', 'parentUprn': '1775091131', 'formattedAddress'
      property_name = address.get('formattedAddress')
      property_uprn = address.get('uprn')
      parent_uprn = address.get('parentUprn')
  
      tables.append([
          table_headers[level.get('level')],
          property_name,
          property_uprn,
          parent_uprn,
      ])

  return tables
