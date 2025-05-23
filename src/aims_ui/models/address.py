from .utilities.classifications import get_classification_list
from .utilities.logicalStatusUtils import getTextLogicalStatus
from .utilities.sibling_lookup import getHierarchy


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
    nag = nag[0] if nag else {}

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
    self.pao = Pao(nag.get('pao', {}))
    self.sao = Sao(nag.get('sao', {}))
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
      classification_code=None,
      underlying_score=None,
      confidence_score=None,
  ):
    self.name = name
    self.address_data = address_data
    self.raw_value = address_data.get(name)
    self.value = self.format_special(self.raw_value, classification_code,
                                     underlying_score, confidence_score)
    self.show = False

    # Set values to show in small overview of an address
    values_to_show = [
        'uprn',
        'classificationCode',
        'confidenceScoreFormatted',
        'lpiLogicalStatus',
    ]

    # Values to show in the 'full info' page on a particular address
    full_values_to_show = [
        'uprn',
        'classificationCode',
        'classificationCodeList',
        'confidenceScoreFormatted',
        'parentUprn',
    ]

    # CHANGE HERE TODO above for hybrid
    # Decide on behaviour between normal or hybrid approach to
    # attribute selection (Leave blank for complete control)
    values_to_show = []

    if name in full_values_to_show:
      self.full_show = True

    if name in values_to_show:
      self.show = True

  def format_special(self,
                     value,
                     classification_code=None,
                     underlying_score=None,
                     confidence_score=None):
    # Special formatting for some values
    if self.name == 'confidenceScoreFormatted':
      if confidence_score:
        confidence_score_formatted = str(round(float(confidence_score),
                                               2)) + '% Match'
        return confidence_score_formatted
      return ''

    if self.name == 'confidenceScore':
      if confidence_score != None:
        return confidence_score
      else:
        return value

    if self.name == 'underlyingScore':
      if underlying_score != None:
        return underlying_score
      else:
        return value

    if self.name == 'geo':
      if value:
        return {
            'latitude': str(value.get('latitude')),
            'longitude': str(value.get('longitude'))
        }
      return {'latitude': 'na', 'longitude': 'na'}
    if self.name == 'classificationCodeList':
      return get_classification_list(classification_code)
    if self.name == 'nag':
      return Nag(self.raw_value)
    if self.name == 'paf':
      return Paf(self.raw_value)
    if self.name == 'lpiLogicalStatus':
      return getTextLogicalStatus(self.raw_value)
    if self.name == 'hierarchy':
      return getHierarchy(self.address_data)
    if self.name == 'parentUprn':
      if str(value) != '0':
        return f'<a href="/address_info/{value}">{value}<a>'
      else:
        return 'NA'

    return f'{value}'


class Address():

  def __init__(self,
               address_data,
               include_hierarchy=False,
               underlying_score=None,
               confidence_score=None):
    address_data = address_data.get('address')

    # Essentially all atributes of an expected address from AIMS API (Verbose)
    self.uprn = AddressAttribute(address_data, 'uprn')
    self.formatted_address = AddressAttribute(address_data, 'formattedAddress')
    self.parent_uprn = AddressAttribute(address_data, 'parentUprn')
    self.formatted_address_nag = AddressAttribute(address_data,
                                                  'formattedAddressNag')
    self.formatted_address_paf = AddressAttribute(address_data,
                                                  'formattedAddressPaf')
    self.welsh_formatted_address_nag = AddressAttribute(
        address_data, 'welshFormattedAddressNag')
    self.welsh_formatted_address_paf = AddressAttribute(
        address_data, 'welshFormattedAddressPaf')
    self.geo = AddressAttribute(address_data, 'geo')
    self.classification_code = AddressAttribute(address_data,
                                                'classificationCode')
    self.classification_code_list = AddressAttribute(
        address_data,
        'classificationCodeList',
        classification_code=self.classification_code.value)
    self.country_code = AddressAttribute(address_data, 'countryCode')
    self.lpi_logical_status = AddressAttribute(address_data,
                                               'lpiLogicalStatus')
    self.confidence_score = AddressAttribute(address_data,
                                             'confidenceScore',
                                             confidence_score=confidence_score)
    self.formatted_confidence_score = AddressAttribute(
        address_data,
        'confidenceScoreFormatted',
        confidence_score=self.confidence_score.value)
    self.underlying_score = AddressAttribute(address_data,
                                             'underlyingScore',
                                             underlying_score=underlying_score)
    if include_hierarchy:
      self.hierarchy = AddressAttribute(address_data, 'hierarchy')
    else:
      self.hierarchy = None

    # Items with their own Dict object returned should be given full response
    self.nag = AddressAttribute(address_data, 'nag')
    self.paf = AddressAttribute(address_data, 'paf')
