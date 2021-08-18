import json
from .utilities.classifications import get_classification_list
from aims_ui import app


class AddressAttribute():
  def __init__(
      self,
      address_data,
      name,
  ):
    self.name = name
    self.raw_value = address_data.get(name)
    self.value = self.format_special(self.raw_value)
    self.show = False

    # Set values to show in small overview of an address
    values_to_show = [
        'uprn',
        'classificationCode',
        'confidenceScore',
    ]

    # Values to show in the 'full info' page on a particular address
    full_values_to_show = [
        'uprn',
        'classificationCode',
        'classificationCodeList',
        'confidenceScore',
        'nag',
    ]
     
    if name in full_values_to_show:
      self.full_show = True

    if name in values_to_show:
      self.show = True

  def format_special(self, value):
    # Special formatting for some values
    if self.name == 'confidence_score':
      return (f'{value}% match')
    if self.name == 'geo':
      # Convert geo to strings
      new_d = {
          'longitude': str(value.get('longitude')),
          'latitude': str(value.get('latitude')),
      }
      return new_d
    if self.name == 'classificationCodeList':
      return get_classification_list()
    if self.name == 'nag':
      self.name = 'localCustodianName'
      return self.raw_value[0].get('localCustodianName') if len(self.raw_value) > 0 else ''


    return f'{value}'


class Address():
  def __init__(self, address_data):
    # Essentially all atributes of an expected address from AIMS API (Verbose)
    self.uprn = AddressAttribute(address_data, 'uprn')
    self.formatted_address = AddressAttribute(address_data, 'formattedAddress')
    self.parent_uprn = AddressAttribute(address_data, 'parentUprn')
    self.formatted_address_nag = AddressAttribute(address_data,
                                                'formattedAddressNag')
    self.formatted_address_paf = AddressAttribute(address_data,
                                                'formattedAddressPaf')
    self.formatted_address_nisra = AddressAttribute(address_data,
                                                  'formattedAddressNisra')
    self.welsh_formatted_address_nag = AddressAttribute(
        address_data, 'welshFormattedAddressNag')
    self.welsh_formatted_address_paf = AddressAttribute(
        address_data, 'welshFormattedAddressPaf')
    self.geo = AddressAttribute(address_data, 'geo')
    self.classification_code = AddressAttribute(address_data,
                                               'classificationCode')
    self.classification_code_list = AddressAttribute(address_data,
                                               'classificationCodeList')
    self.census_address_type = AddressAttribute(address_data,
                                              'censusAddressType')
    self.census_estab_type = AddressAttribute(address_data, 'censusEstabType')
    self.country_code = AddressAttribute(address_data, 'countryCode')
    self.lpi_logical_status = AddressAttribute(address_data, 'lpiLogicalStatus')
    self.confidence_score = AddressAttribute(address_data, 'confidenceScore')
    self.underlying_score = AddressAttribute(address_data, 'underlyingScore')
    self.nag = AddressAttribute(address_data, 'nag')


  











