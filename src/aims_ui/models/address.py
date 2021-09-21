from dataclasses import dataclass, field, fields
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


class BasicValue():
  def __init__(self, nag_paf, name, default_blank=''):
    self.value = nag_paf.get(name, default_blank)


class Nag():
  def __init__(self, nag):
    nag = nag[0]

    # Values to show in the 'full info' page on a particular address
    self.full_values_to_show = [
        'localCustodianName',
    ]

    self.clerical_values = [
        'uprn',
        'postcodeLocator',
        'addressBasePostal',
        'usrn',
        'lpiKey',
        'level',
        'officialFlag',
        'logicalStatus',
        'streetDescriptor',
        'townName',
        'locality',
        'organisation',
        'legalName',
        'localCustodianCode',
        'localCustodianName',
        'localCustodianGeogCode',
        'lpiEndDate',
        'lpiStartDate',
    ]

    self.uprn = BasicValue(nag, 'uprn')
    self.postcodeLocator = BasicValue(nag, 'postcodeLocator')
    self.addressBasePostal = BasicValue(nag, 'addressBasePostal')
    self.usrn = BasicValue(nag, 'usrn')
    self.lpiKey = BasicValue(nag, 'lpiKey')
    self.pao = Pao(nag.get('pao'))
    self.sao = Sao(nag.get('sao'))
    self.level = BasicValue(nag, 'level')
    self.officialFlag = BasicValue(nag, 'officialFlag')
    self.logicalStatus = BasicValue(nag, 'logicalStatus')
    self.streetDescriptor = BasicValue(nag, 'streetDescriptor')
    self.townName = BasicValue(nag, 'townName')
    self.locality = BasicValue(nag, 'locality')
    self.organisation = BasicValue(nag, 'organisation')
    self.legalName = BasicValue(nag, 'legalName')
    self.localCustodianCode = BasicValue(nag, 'localCustodianCode')
    self.localCustodianName = BasicValue(nag, 'localCustodianName')
    self.localCustodianGeogCode = BasicValue(nag, 'localCustodianGeogCode')
    self.lpiEndDate = BasicValue(nag, 'lpiEndDate')
    self.lpiStartDate = BasicValue(nag, 'lpiStartDate')


class Paf():
  def __init__(self, paf):
    if not paf:
      paf = {}

    # Values to show in the 'full info' page on a particular address
    self.full_values_to_show = []

    self.clerical_values = [
        'udprn',
        'organisationName',
        'departmentName',
        'subBuildingName',
        'buildingName',
        'buildingNumber',
        'dependentThoroughfare',
        'thoroughfare',
        'doubleDependentLocality',
        'dependentLocality',
        'postTown',
        'postcode',
        'postcodeType',
        'deliveryPointSuffix',
        'welshDependentThoroughfare',
        'welshThoroughfare',
        'welshDoubleDependentLocality',
        'welshDependentLocality',
        'welshPostTown',
        'poBoxNumber',
        'startDate',
        'endDate',
    ]

    self.udprn = BasicValue(paf, 'udprn')
    self.organisationName = BasicValue(paf, 'organisationName')
    self.departmentName = BasicValue(paf, 'departmentName')
    self.subBuildingName = BasicValue(paf, 'subBuildingName')
    self.buildingName = BasicValue(paf, 'buildingName')
    self.buildingNumber = BasicValue(paf, 'buildingNumber')
    self.dependentThoroughfare = BasicValue(paf, 'dependentThoroughfare')
    self.thoroughfare = BasicValue(paf, 'thoroughfare')
    self.doubleDependentLocality = BasicValue(paf, 'doubleDependentLocality')
    self.dependentLocality = BasicValue(paf, 'dependentLocality')
    self.postTown = BasicValue(paf, 'postTown')
    self.postcode = BasicValue(paf, 'postcode')
    self.postcodeType = BasicValue(paf, 'postcodeType')
    self.deliveryPointSuffix = BasicValue(paf, 'deliveryPointSuffix')
    self.welshDependentThoroughfare = BasicValue(paf,
                                                 'welshDependentThoroughfare')
    self.welshThoroughfare = BasicValue(paf, 'welshThoroughfare')
    self.welshDoubleDependentLocality = BasicValue(
        paf, 'welshDoubleDependentLocality')
    self.welshDependentLocality = BasicValue(paf, 'welshDependentLocality')
    self.welshPostTown = BasicValue(paf, 'welshPostTown')
    self.poBoxNumber = BasicValue(paf, 'poBoxNumber')
    self.startDate = BasicValue(paf, 'startDate')
    self.endDate = BasicValue(paf, 'endDate')


class AddressAttribute():
  def __init__(
      self,
      address_data,
      name,
  ):
    self.name = name
    self.address_data = address_data 
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
    if self.name == 'paf':
      return Paf(self.raw_value)

    return f'{value}'


@dataclass
class Address():
  uprn: AddressAttribute
  formattedAddress:AddressAttribute 
  parentUprn:AddressAttribute 
  formattedAddressNag:AddressAttribute 
  formattedAddressPaf:AddressAttribute
  formattedAddressNisra:AddressAttribute 
  welshFormattedAddressNag:AddressAttribute 
  welshFormattedAddressPaf:AddressAttribute
  geo: AddressAttribute
  classificationCode:AddressAttribute 
  classificationCodeList:AddressAttribute 
  censusAddressType:AddressAttribute 
  censusEstabType:AddressAttribute 
  countryCode:AddressAttribute 
  lpiLogicalStatus:AddressAttribute 
  confidenceScore:AddressAttribute 
  underlyingScore:AddressAttribute

  # Items with their own Dict object returned should be given full response
  nag: AddressAttribute 
  paf :AddressAttribute  

  @classmethod
  def from_dict(cls, d):
    d  = d.get('address')
    args = [
        AddressAttribute(d, 'uprn'),
        AddressAttribute(d, 'formattedAddress'),
        AddressAttribute(d, 'parentUprn'),
        AddressAttribute(d, 'formattedAddressNag'),
        AddressAttribute(d, 'formattedAddressPaf'),
        AddressAttribute(d, 'formattedAddressNisra'),
        AddressAttribute(d, 'welshFormattedAddressNag'),
        AddressAttribute(d, 'welshFormattedAddressPaf'),
        AddressAttribute(d, 'geo'),
        AddressAttribute(d, 'classificationCode'),
        AddressAttribute(d, 'classificationCodeList'),
        AddressAttribute(d, 'censusAddressType'),
        AddressAttribute(d, 'censusEstabType'),
        AddressAttribute(d, 'countryCode'),
        AddressAttribute(d, 'lpiLogicalStatus'),
        AddressAttribute(d, 'confidenceScore'),
        AddressAttribute(d, 'underlyingScore'), 
        AddressAttribute(d, 'nag'),
        AddressAttribute(d, 'paf'),
       ]

    return Address(*args)
