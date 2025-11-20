
export function getPopulatedAttributeMap(addressObject) {
  // Return an array of objects mapping with cellId: and value:, labelText:

  const paf = addressObject.paf || {};
  const nag = addressObject.nag || {};

  const valueCellToAddressValueMap = [
    // Base address fields
    { 
        cellId: 'classificationCode', 
        value: addressObject.classificationCode, 
        labelText: 'Classification Code', 
        description: 'A code that describes the classification of the record.'
    },
    { 
        cellId: 'classificationCodeList', 
        value: addressObject.classificationCodeList, 
        labelText: 'Classification Code List', 
        description: 'The broken down Classifications Hierarchy of an address'
    },
    { 
        cellId: 'confidenceScore', 
        value: addressObject.confidenceScore, 
        labelText: 'Confidence Score', 
        description: 'An overall match confidence percentage obtained from a Sigmoid function that uses the search engine scores and the calculated bespoke scores of all the results in the set. Scores over 70 can be taken as the clear winner, whilst scores around 50 usually indicate some ambiguity. The API can filter out scores below a certain threshold.',
        helpLink: '/help/confidence_score'
    },
    { 
        cellId: 'formattedConfidenceScore', 
        value: addressObject.formattedConfidenceScore, 
        labelText: 'Formatted Confidence Score', 
        description: 'The "Confidence Score" with a "%" appended, rounded to 2dp.'
    },
    { 
        cellId: 'countryCode', 
        value: addressObject.countryCode, 
        labelText: 'Country Code', 
        description: 'The country in which a record can be found. This is calculated by performing an intersection with OS Boundary Line. This means records such as wind and fish farms will be assigned a value of ‘J’. E = England W = Wales S = Scotland N = Northern Ireland L = Channel Islands M = Isle of Man J = Not assigned to a country as it falls outside of the land boundaries used.'
    },
    { 
        cellId: 'formattedAddress', 
        value: addressObject.formattedAddress, 
        labelText: 'Formatted Address', 
        description: 'Capitalized address that\'s the most human readable'
    },
    { 
        cellId: 'formattedAddressNag', 
        value: addressObject.formattedAddressNag, 
        labelText: 'Formatted Address (NAG)', 
        description: 'Capitalized address that\'s the most human readable. Sourced from NAG',
    },
    { 
        cellId: 'formattedAddressPaf', 
        value: addressObject.formattedAddressPaf, 
        labelText: 'Formatted Address (PAF)', 
        description: 'Capitalized address that\'s the most human readable. Sourced from PAF',
    },
    { 
        cellId: 'latitude', 
        value: addressObject.latitude, 
        labelText: 'Latitude', 
        description: 'A value defining the Latitude location in accordance with the ETRS89 coordinate reference system.'
    },
    { 
        cellId: 'longitude', 
        value: addressObject.longitude, 
        labelText: 'Longitude', 
        description: 'A value defining the Longitude location in accordance with the ETRS89 coordinate reference system.'
    },
    { 
        cellId: 'lpiLogicalStatus', 
        value: addressObject.lpiLogicalStatus.text, 
        labelText: 'LPI Logical Status', 
        description: 'Logical status of this address record as given by the local custodian. This attribute shows whether the address is currently live provisional or historic. 1 = Approved 3 = Alternative 6 = Provisional 8 = Historical'
    },
    { 
        cellId: 'parentUprn', 
        value: addressObject.parentUprn, 
        labelText: 'Parent UPRN', 
        description: 'UPRN of the parent Record if a parent child relationship exists.'
    },
    { 
        cellId: 'underlyingScore', 
        value: addressObject.underlyingScore, 
        labelText: 'Underlying Score', 
        description: 'The raw document match score from the search engine. It is best used as a relative score so 20 is better than 5. Scores tend to be in the range 0-30.',
    },
    { 
        cellId: 'uprn', 
        value: addressObject.uprn, 
        labelText: 'UPRN', 
        description: 'Unique Property Reference Number (UPRN) assigned by the LLPG (Local Land and Property Gazetteer) Custodian or Ordnance Survey.'
    },
    { 
        cellId: 'welshFormattedAddressNag', 
        value: addressObject.welshFormattedAddressNag, 
        labelText: 'Welsh Formatted Address (NAG)', 
        description: 'Welsh translation for formatted_address_nag',
    },
    { 
        cellId: 'welshFormattedAddressPaf', 
        value: addressObject.welshFormattedAddressPaf, 
        labelText: 'Welsh Formatted Address (PAF)', 
        description: 'Welsh translation for formatted_address_paf',
    },

    // Now add the paf map
    { 
        cellId: 'pafBuildingName', 
        value: paf.buildingName, 
        labelText: '[PAF] Building Name', 
        description: 'The building name is a description applied to a single building or a small group of buildings such as Highfield House. This also includes those building numbers that contain non-numeric characters such as 44A. Some descriptive names when included with the rest of the address are sufficient to identify the property uniquely and unambiguously for example MAGISTRATES COURT. Sometimes the building name will be a blend of distinctive and descriptive naming for example RAILWAY TAVERN (PUBLIC HOUSE) or THE COURT ROYAL (HOTEL). Building Name must be present if Organisation Name or Building Number or PO Box Number are all not present.'
    },
    { 
        cellId: 'pafBuildingNumber', 
        value: paf.buildingNumber, 
        labelText: '[PAF] Building Number', 
        description: 'The building number is a number given to a single building or a small group of buildings thus identifying it from its neighbours for example 44. Building numbers that contain a range decimals or non-numeric characters do not appear in this field but will be found in the buildingName or the sub-BuildingName fields. Building Number must be present if Organisation Name or Building Name or PO Box Number are all not present.'
    },
    { 
        cellId: 'pafDeliveryPointSuffix', 
        value: paf.deliveryPointSuffix, 
        labelText: '[PAF] Delivery Point Suffix', 
        description: 'A two character code uniquely identifying an individual delivery point within a postcode.'
    },
    { 
        cellId: 'pafDepartmentName', 
        value: paf.departmentName, 
        labelText: '[PAF] Department Name', 
        description: 'For some organisations department name is indicated because mail is received by subdivisions of the main organisation at distinct delivery points. For example: Organisation Name: ABC COMMUNICATIONS RM Department Name: MARKETING DEPARTMENT If a Department Name is present an Organisation Name must also be present.'
    },
    { 
        cellId: 'pafDependentLocality', 
        value: paf.dependentLocality, 
        labelText: '[PAF] Dependent Locality', 
        description: 'Dependent locality areas define an area within a post town. These are only necessary for postal purposes and are used to aid differentiation where there are thoroughfares of the same name in the same locality. For example HIGH STREET in SHIRLEY and SWAYTHLING in this situation: HIGH STREET SHIRLEY SOUTHAMPTON and HIGH STREET SWAYTHLING SOUTHAMPTON.'
    },
    { 
        cellId: 'pafDependentThoroughfare', 
        value: paf.dependentThoroughfare, 
        labelText: '[PAF] Dependent Thoroughfare', 
        description: 'In certain places for example town centres there are named thoroughfares within other named thoroughfares for example parades of shops on a high street where different parades have their own identity. For example KINGS PARADE HIGH STREET and QUEENS PARADE HIGH STREET. If a Dependent Thoroughfare is present a Thoroughfare value must also be present.'
    },
    { 
        cellId: 'pafDoubleDependentLocality', 
        value: paf.doubleDependentLocality, 
        labelText: '[PAF] Double Dependent Locality', 
        description: 'This is used to distinguish between similar thoroughfares or the same thoroughfare within a dependent locality. For example Millbrook Industrial Estate and Cranford Estate in this situation: BRUNEL WAY MILLBROOK INDUSTRIAL ESTATE MILLBROOK SOUTHAMPTON and BRUNEL WAY CRANFORD ESTATE MILLBROOK SOUTHAMPTON. If a Double Dependent Locality is present a Dependent Locality must also be present.'
    },
    { 
        cellId: 'pafEndDate', 
        value: paf.endDate, 
        labelText: '[PAF] End Date', 
        description: 'The date on which this record ceased to exist in the Geoplace/OS database'
    },
    { 
        cellId: 'pafOrganisationName', 
        value: paf.organisationName, 
        labelText: '[PAF] Organisation Name', 
        description: 'The organisation name is the business name given to a delivery point within a building or small group of buildings. For example: TOURIST INFORMATION CENTRE This field could also include entries for churches public houses and libraries. Organisation Name must be present if Building Name or Building Number or PO Box Number are all not present.'
    },
    { 
        cellId: 'pafPoBoxNumber', 
        value: paf.poBoxNumber, 
        labelText: '[PAF] PO Box Number', 
        description: 'Post Office Box (PO Box) number. Source: Royal Mail Condition: Organisation Name or PO Box Number must be present if Building Name or Building Number are all not present.'
    },
    { 
        cellId: 'pafPostTown', 
        value: paf.postTown, 
        labelText: '[PAF] Post Town', 
        description: 'The town or city in which the Royal Mail sorting office is located which services this record. There may be more than one possibly several sorting offices in a town or city.'
    },
    { 
        cellId: 'pafPostcode', 
        value: paf.postcode, 
        labelText: '[PAF] Postcode', 
        description: 'A postcode is an abbreviated form of address made up of combinations of between five and seven alphanumeric characters. These are used by Royal Mail to help with the automated sorting of mail. A postcode may cover between 1 and 100 addresses. There are two main components of a postcode for example NW6 4DP: • The outward code (or ‘outcode’). The first two–four characters of the postcode constituting the postcode area and the postcode district for example NW6. It is the part of the postcode that enables mail to be sent from the accepting office to the correct area for delivery. The last three characters of the postcode constituting the postcode sector and the postcode unit example 4DP. It is used to sort mail at the local delivery office.'
    },
    { 
        cellId: 'pafPostcodeType', 
        value: paf.postcodeType, 
        labelText: '[PAF] Postcode Type', 
        description: 'Describes the address as a small or large user as defined by Royal Mail.'
    },
    { 
        cellId: 'pafStartDate', 
        value: paf.startDate, 
        labelText: '[PAF] Start Date', 
        description: 'Date this record was first created in the Geoplace/OS database'
    },
    { 
        cellId: 'pafSubBuildingName', 
        value: paf.subBuildingName, 
        labelText: '[PAF] Sub-Building Name', 
        description: 'The sub-building name and/or number are identifiers for subdivisions of properties. [...] If a Sub Building Name is present a Building Name or Building Number must also be present.' 
    },
    { 
        cellId: 'pafThoroughfare', 
        value: paf.thoroughfare, 
        labelText: '[PAF] Thoroughfare', 
        description: 'A thoroughfare in AddressBase is fundamentally a road track or named access route on which there are Royal Mail delivery points for example HIGH STREET.'
    },
    { 
        cellId: 'pafUdprn', 
        value: paf.udprn, 
        labelText: '[PAF] UDPRN', 
        description: 'Royal Mail\'s Unique Delivery Point Reference Number (UDPRN).'
    },
    { 
        cellId: 'pafWelshDependentLocality', 
        value: paf.welshDependentLocality, 
        labelText: '[PAF] Welsh Dependent Locality', 
        description: 'The Welsh translation of DEPENDENT_LOCALITY. Source: Royal Mail',
    },
    { 
        cellId: 'pafWelshDependentThoroughfare', 
        value: paf.welshDependentThoroughfare, 
        labelText: '[PAF] Welsh Dependent Thoroughfare', 
        description: 'The Welsh translation of DEPENDENT_THOROUGHFARE  Source: Royal Mail  Condition:  If a Welsh Dependent Thoroughfare is present  a Welsh Thoroughfare must also be present.',
    },
    { 
        cellId: 'pafWelshDoubleDependentLocality', 
        value: paf.welshDoubleDependentLocality, 
        labelText: '[PAF] Welsh Double Dependent Locality', 
        description: 'The Welsh translation of Double Dependent Locality.  Source: Royal Mail  Condition:  If a Welsh Double Dependent Locality is present  a Welsh Dependent Locality must also be present.',
    },
    { 
        cellId: 'pafWelshPostTown', 
        value: paf.welshPostTown, 
        labelText: '[PAF] Welsh Post Town', 
        description: 'The Welsh translation of post town value. Source: Royal Mail',
    },
    { 
        cellId: 'pafWelshThoroughfare', 
        value: paf.welshThoroughfare, 
        labelText: '[PAF] Welsh Thoroughfare', 
        description: 'The Welsh translation of THOROUGHFARE.  Source: Royal Mail',
    },

    // NAG Attributes
        { 
        cellId: 'nagAddressBasePostal', 
        value: nag.addressBasePostal, 
        labelText: '[NAG] Address Base Postal', 
        description: 'Identifies addresses which are believed to be capable of receiving mail as defined specifically for the AddressBase products and details their relationship with other AddressBase Postal records. N.B. this field identifies some addresses which the AddressBase product believes to be capable of receiving mail which are not contained within the Royal Mail PAF database such as flats behind a front door which has a single letter box. D = A record which is linked to PAF N = Not a postal address C = A record which is postal and has a parent record which is linked to PAF L = A record which is identified as postal based on Local Authority information'
    },
    { 
        cellId: 'nagLegalName', 
        value: nag.legalName, 
        labelText: '[NAG] Legal Name', 
        description: 'Registered legal name of the organisation.'
    },
    { 
        cellId: 'nagLevel', 
        value: nag.level, 
        labelText: '[NAG] Level', 
        description: 'Detail on the vertical position of the property if known and provided by the Local Authority Custodian.'
    },
    { 
        cellId: 'nagLocalCustodianCode', 
        value: nag.localCustodianCode, 
        labelText: '[NAG] Local Custodian Code', 
        description: 'Unique identifier for the data provider code. https://www.ordnancesurvey.co.uk/docs/classification-codes/addressBase-Products-local-custodian-codes.pdf'
    },
    { 
        cellId: 'nagLocalCustodianGeogCode', 
        value: nag.localCustodianGeogCode, 
        labelText: '[NAG] Local Custodian Geog Code', 
        description: 'The code (e.g. E07000041) of the local authority supplying the NAG entry. Usually but not always the LA the property is in.',
    },
    { 
        cellId: 'nagLocalCustodianName', 
        value: nag.localCustodianName, 
        labelText: '[NAG] Local Custodian Name', 
        description: 'The name of the local authority supplying the NAG entry. Usually but not always the LA the property is in.',
    },
    { 
        cellId: 'nagLocality', 
        value: nag.locality, 
        labelText: '[NAG] Locality', 
        description: 'A locality defines an area or geographical identifier within a town village or hamlet. Locality represents the lower level geographical area. The locality field should be used in conjunction with the town name and street description fields to uniquely identify geographic area where there may be more than one within an administrative area.'
    },
    { 
        cellId: 'nagLogicalStatus', 
        value: nag.logicalStatus, 
        labelText: '[NAG] Logical Status', 
        description: 'Logical status of this address record as given by the local custodian. This attribute shows whether the address is currently live provisional or historic. 1 = Approved 3 = Alternative 6 = Provisional 8 = Historical'
    },
    { 
        cellId: 'nagLpiEndDate', 
        value: nag.lpiEndDate, 
        labelText: '[NAG] LPI End Date', 
        description: 'The date on which this record ceased to exist in the Geoplace/OS database'
    },
    { 
        cellId: 'nagLpiKey', 
        value: nag.lpiKey, 
        labelText: '[NAG] LPI Key', 
        description: 'Unique key for the LPI'
    },
    { 
        cellId: 'nagLpiStartDate', 
        value: nag.lpiStartDate, 
        labelText: '[NAG] LPI Start Date', 
        description: 'The date on which the record was inserted into the Local Authority database.'
    },
    { 
        cellId: 'nagOfficialFlag', 
        value: nag.officialFlag, 
        labelText: '[NAG] Official Flag', 
        description: 'An indicator of whether an address record corresponds to an entry in the official Street Name and Numbering register. N: Unofficial address Y: Official Address'
    },
    { 
        cellId: 'nagOrganisation', 
        value: nag.organisation, 
        labelText: '[NAG] Organisation', 
        description: 'Name of the organisation currently occupying the address record as provided by the local authority custodian.'
    },
    { 
        cellId: 'nagPostcodeLocator', 
        value: nag.postcodeLocator, 
        labelText: '[NAG] Postcode Locator', 
        description: 'This field contains the Royal Mail Postcode Address File (PAF) postcode where the local authority address has been matched to PAF i.e. the POSTCODE field found within the Delivery Point Address table. Where a match has not been made the postcode information is sourced from the local authority in collaboration with Royal Mail. Where the local authority do not hold a current valid postcode Code-Point with Polygons® is used to spatially derive the postcode based on the position of the coordinates. This field must be used in conjunction with the RPC field to determine the accuracy of its position.'
    },
    { 
        cellId: 'nagStreetDescriptor', 
        value: nag.streetDescriptor, 
        labelText: '[NAG] Street Descriptor', 
        description: 'Name description or Street number for this record.'
    },
    { 
        cellId: 'nagTownName', 
        value: nag.townName, 
        labelText: '[NAG] Town Name', 
        description: 'Town name must be present if the Street Record Type is 1 or 2 and may be entered for type 3 4 and 9 Streets.'
    },
    { 
        cellId: 'nagUprn', 
        value: nag.uprn, 
        labelText: '[NAG] UPRN', 
        description: 'Unique Property Reference Number (UPRN) assigned by the LLPG (Local Land and Property Gazetteer) Custodian or Ordnance Survey.'
    },
    { 
        cellId: 'nagUsrn', 
        value: nag.usrn, 
        labelText: '[NAG] USRN', 
        description: 'Unique Street Reference Number (USRN) - foreign key linking the Street record to the LPI record.',
    }
  ]

  return valueCellToAddressValueMap 
}

