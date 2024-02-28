from .address import Address
from .short_address import ShortAddress


def get_addresses(json_response,
                  called_from,
                  confidence_score=None,
                  underlying_score=None):
  """Create Address classes for each address, might need to be different for each endpoint"""
  addresses = []

  if called_from == 'uprn':
    response = (json_response.get('response'))
    addresses = [
        Address(response,
                include_hierarchy=True,
                underlying_score=underlying_score,
                confidence_score=confidence_score)
    ]

  elif (called_from == 'postcode') or (called_from == 'singlesearch') or (
      called_from == 'custom_response'):
    response = (json_response.get('response'))
    address_json = response.get('addresses')

    for address in address_json:
      addresses.append(Address({'address': address}))

  elif (called_from == 'multiple'):
    response = (json_response.get('response'))
    address_json = response.get('addresses')

    for address in address_json:
      addresses.append(ShortAddress({'address': address}))

  elif called_from == 'multiple_uprn':
    response = json_response.get('response')
    address_json = response.get('addresses')

    for address in address_json:
      addresses.append(ShortAddress({'address': address}))

  return addresses
