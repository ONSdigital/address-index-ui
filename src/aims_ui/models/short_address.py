from .utilities.classifications import get_classification_list
from .utilities.logicalStatusUtils import getTextLogicalStatus
from .utilities.sibling_lookup import getHierarchy


class AddressAttribute():

  def __init__(
      self,
      address_data,
      name,
      classification_code=None,
      confidence_score=None,
  ):
    self.name = name
    self.address_data = address_data
    self.raw_value = address_data.get(name.partition('.')[0])
    self.value = self.format_special(self.raw_value, classification_code,
                                     confidence_score)
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
                     confidence_score=None):
    # Special formatting for some values
    if self.name == 'confidenceScoreFormatted':
      confidence_score_formatted = str(round(float(confidence_score),
                                             2)) + '% Match'
      return confidence_score_formatted

    if self.name == 'confidenceScore':
      if confidence_score != None:
        return confidence_score
      else:
        return value
    # geo can be returned as a block or as separate values
    if self.name == 'geo':
      new_d = {
          'latitude': str(value.get('latitude')),
          'longitude': str(value.get('longitude')),
          'easting': str(value.get('easting')),
          'northing': str(value.get('northing')),
      }
      return new_d
    if self.name == 'geo.latitude':
      return str(value.get('latitude'))
    if self.name == 'geo.longitude':
      return str(value.get('longitude'))
    if self.name == 'geo.easting':
      return str(value.get('easting'))
    if self.name == 'geo.northing':
      return str(value.get('northing'))
    if self.name == 'classificationCodeList':
      return get_classification_list(classification_code)
    if self.name == 'lpiLogicalStatus':
      #return getTextLogicalStatus(self.raw_value)
      return value
    if self.name == 'hierarchy':
      return getHierarchy(self.address_data)
    if self.name == 'parentUprn':
      return value

    return f'{value}'


class ShortAddress():

  def __init__(self,
               address_data,
               include_hierarchy=False,
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
    self.latitude = AddressAttribute(address_data, 'geo.latitude')
    self.longitude = AddressAttribute(address_data, 'geo.longitude')
    self.easting = AddressAttribute(address_data, 'geo.easting')
    self.northing = AddressAttribute(address_data, 'geo.northing')
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
    self.underlying_score = AddressAttribute(address_data, 'underlyingScore')
    self.airRating = AddressAttribute(address_data, 'airRating')
    if include_hierarchy:
      self.hierarchy = AddressAttribute(address_data, 'hierarchy')
    else:
      self.hierarchy = None
