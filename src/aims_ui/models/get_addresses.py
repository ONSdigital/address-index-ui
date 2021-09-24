from .address import Address


def get_addresses(json_response, called_from):
  """Create Address classes for each address, might need to be different for each endpoint"""
  addresses = []

  if called_from == 'uprn':
    response = (json_response.get('response'))
    addresses = [Address(response)]

  elif (called_from == 'postcode') or (called_from == 'singlesearch'):
    response = (json_response.get('response'))
    address_json = response.get('addresses')

    for address in address_json:
      addresses.append(Address({'address': address}))

  return addresses
