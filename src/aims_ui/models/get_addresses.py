from .address import Address


def get_addresses(json_response, called_from):
  """Create Address classes for each address, might need to be different for each endpoint"""
  addresses = []


  if called_from == 'uprn':
    response = (json_response.get('response'))
    address = response.get('address')

    addresses=[Address(address)]

  return addresses
  
