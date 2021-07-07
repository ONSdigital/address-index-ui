import json

class AddressAttribute():
  def __init__(self, address_data, name, ):
    self.name = name
    self.raw_value = address_data.get(name)
    self.value = self.format_special(self.raw_value)
    self.show= False

    # Set values to show in small overview of an address
    values_to_show = ['uprn',
        'classificationCode',
        'confidenceScore',
        ]

    if name in values_to_show:
      self.show = True

  def format_special(self, value):
    # Special formatting for some values
    if self.name == 'confidenceScore':
      return( f'{value}% match' )
    if self.name == 'geo':
      # Convert geo to strings
      new_d = {'longitude':str( value.get('longitude')),
               'latitude': str(value.get('latitude')),}
      return new_d 

    return f'{value}'
    


class Address():
  def __init__(self, address_data):
    # Essentially all atributes of an expected address from AIMS API
    self.uprn=AddressAttribute(address_data, 'uprn')
    self.formattedAddress = AddressAttribute(address_data, 'formattedAddress')
    self.parentUprn = AddressAttribute(address_data, 'parentUprn')
    self.formattedAddressNag = AddressAttribute(address_data, 'formattedAddressNag')
    self.formattedAddressPaf = AddressAttribute(address_data, 'formattedAddressPaf')
    self.formattedAddressNisra = AddressAttribute(address_data, 'formattedAddressNisra')
    self.welshFormattedAddressNag = AddressAttribute(address_data, 'welshFormattedAddressNag')
    self.welshFormattedAddressPaf = AddressAttribute(address_data, 'welshFormattedAddressPaf')
    self.geo = AddressAttribute(address_data, 'geo')
    self.classificationCode = AddressAttribute(address_data, 'classificationCode')
    self.censusAddressType = AddressAttribute(address_data, 'censusAddressType')
    self.censusEstabType = AddressAttribute(address_data, 'censusEstabType')
    self.countryCode= AddressAttribute(address_data, 'countryCode')
    self.lpiLogicalStatus = AddressAttribute(address_data, 'lpiLogicalStatus')
    self.confidenceScore = AddressAttribute(address_data, 'confidenceScore')
    self.underlyingScore = AddressAttribute(address_data, 'underlyingScore')   
      
