import json
from .utilities.classifications import get_classification_list
from aims_ui import app


class Pao():
  def __init__(self, pao):
    self.paoText = pao.get('paoText')
    self.paoStartNumber = pao.get('paoStartNumber')
    self.paoStartSuffix = pao.get('paoStartSuffix')
    self.paoEndNumber = pao.get('paoEndNumber')
    self.paoEndSuffix = pao.get('paoEndSuffix')


class Sao():
  def __init__(self, sao):
    self.saoText = sao.get('saoText')
    self.saoStartNumber = sao.get('saoStartNumber')
    self.saoStartSuffix = sao.get('saoStartSuffix')
    self.saoEndNumber = sao.get('saoEndNumber')
    self.saoEndSuffix = sao.get('saoEndSuffix')

class NagValue():
  def __init__(self, nag, name):
    self.value = nag.get(name)

class Nag():
  def __init__(self, nag):
    nag = nag[0]

    # Values to show in the 'full info' page on a particular address
    self.full_values_to_show = [
        'localCustodianName',
    ]

    self.uprn = NagValue(nag, 'uprn')
    self.postcodeLocator = NagValue(nag, 'postcodeLocator')
    self.addressBasePostal = NagValue(nag, 'addressBasePostal')
    self.usrn = NagValue(nag, 'usrn')
    self.lpiKey = NagValue(nag, 'lpiKey')
    self.pao = Pao(nag.get('pao'))
    self.sao = Sao(nag.get('sao'))
    self.level = NagValue(nag, 'level')
    self.officialFlag = NagValue(nag, 'officialFlag')
    self.logicalStatus = NagValue(nag, 'logicalStatus')
    self.streetDescriptor = NagValue(nag, 'streetDescriptor')
    self.townName = NagValue(nag, 'townName')
    self.locality = NagValue(nag, 'locality')
    self.organisation = NagValue(nag, 'organisation')
    self.legalName = NagValue(nag, 'legalName')
    self.localCustodianCode = NagValue(nag, 'localCustodianCode')
    self.localCustodianName = NagValue(nag, 'localCustodianName')
    self.localCustodianGeogCode = NagValue(nag, 'localCustodianGeogCode')
    self.lpiEndDate = NagValue(nag, 'lpiEndDate')
    self.lpiStartDate = NagValue(nag, 'lpiStartDate')

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
      # README swapping the long/lat values fixes things - do not change, it's not a mistake!
      new_d = {
          'longitude': str(value.get('latitude')),
          'latitude': str(value.get('longitude')),
      }
      return new_d
    if self.name == 'classificationCodeList':
      return get_classification_list()
    if self.name == 'nag':
      return Nag(self.raw_value)

    return f'{value}'


class Address():
  def __init__(self, address_data):
    address_data = address_data.get('address')

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
    self.lpi_logical_status = AddressAttribute(address_data,
                                               'lpiLogicalStatus')
    self.confidence_score = AddressAttribute(address_data, 'confidenceScore')
    self.underlying_score = AddressAttribute(address_data, 'underlyingScore')

    # Items with their own Dict object returned should be given full response
    self.nag = AddressAttribute(address_data, 'nag')
