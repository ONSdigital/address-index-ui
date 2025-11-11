// Generate the favrouties table for each card overview
import { setGlobalValues } from '../../f_helpers/local_storage_page_helpers.mjs';
import { getFavouritesFromLocalStorage } from '/static/js/f_helpers/local_storage_page_helpers.mjs';

const keysToShow = getFavouritesFromLocalStorage();

function getFavouriteCellIdValuePairs(addressObject) {
  // Return an array of objects mapping with cellId: and value: 

  const paf = addressObject.paf || {};
  const nag = addressObject.nag || {};

  const valueCellToAddressValueMap = [

    { cellId: 'classificationCode', value: addressObject.classificationCode, labelText: 'Classification Code' },
    { cellId: 'classificationCodeList', value: addressObject.classificationCodeList, labelText: 'Classification Code List' },
    { cellId: 'confidenceScore', value: addressObject.confidenceScore, labelText: 'Confidence Score' },
    { cellId: 'countryCode', value: addressObject.countryCode, labelText: 'Country Code' },
    { cellId: 'formattedAddress', value: addressObject.formattedAddress, labelText: 'Formatted Address' },
    { cellId: 'formattedAddressNag', value: addressObject.formattedAddressNag, labelText: 'Formatted Address (NAG)' },
    { cellId: 'formattedAddressPaf', value: addressObject.formattedAddressPaf, labelText: 'Formatted Address (PAF)' },
    { cellId: 'latitude', value: addressObject.latitude, labelText: 'Latitude' },
    { cellId: 'longitude', value: addressObject.longitude, labelText: 'Longitude' },
    { cellId: 'lpiLogicalStatus', value: addressObject.lpiLogicalStatus.text, labelText: 'LPI Logical Status' },
    { cellId: 'parentUprn', value: addressObject.parentUprn, labelText: 'Parent UPRN' },
    { cellId: 'underlyingScore', value: addressObject.underlyingScore, labelText: 'Underlying Score' },
    { cellId: 'uprn', value: addressObject.uprn, labelText: 'UPRN' },
    { cellId: 'welshFormattedAddressNag', value: addressObject.welshFormattedAddressNag, labelText: 'Welsh Formatted Address (NAG)' },
    { cellId: 'welshFormattedAddressPaf', value: addressObject.welshFormattedAddressPaf, labelText: 'Welsh Formatted Address (PAF)' },


    // Now add the paf map
    { cellId: 'pafBuildingName', value: paf.buildingName, labelText: '[PAF] Building Name' },
    { cellId: 'pafBuildingNumber', value: paf.buildingNumber, labelText: '[PAF] Building Number' },
    { cellId: 'pafDeliveryPointSuffix', value: paf.deliveryPointSuffix, labelText: '[PAF] Delivery Point Suffix' },
    { cellId: 'pafDepartmentName', value: paf.departmentName, labelText: '[PAF] Department Name' },
    { cellId: 'pafDependentLocality', value: paf.dependentLocality, labelText: '[PAF] Dependent Locality' },
    { cellId: 'pafDependentThoroughfare', value: paf.dependentThoroughfare, labelText: '[PAF] Dependent Thoroughfare' },
    { cellId: 'pafDoubleDependentLocality', value: paf.doubleDependentLocality, labelText: '[PAF] Double Dependent Locality' },
    { cellId: 'pafEndDate', value: paf.endDate, labelText: '[PAF] End Date' },
    { cellId: 'pafOrganisationName', value: paf.organisationName, labelText: '[PAF] Organisation Name' },
    { cellId: 'pafPoBoxNumber', value: paf.poBoxNumber, labelText: '[PAF] PO Box Number' },
    { cellId: 'pafPostTown', value: paf.postTown, labelText: '[PAF] Post Town' },
    { cellId: 'pafPostcode', value: paf.postcode, labelText: '[PAF] Postcode' },
    { cellId: 'pafPostcodeType', value: paf.postcodeType, labelText: '[PAF] Postcode Type' },
    { cellId: 'pafStartDate', value: paf.startDate, labelText: '[PAF] Start Date' },
    { cellId: 'pafSubBuildingName', value: paf.subBuildingName, labelText: '[PAF] Sub-Building Name' },
    { cellId: 'pafThoroughfare', value: paf.thoroughfare, labelText: '[PAF] Thoroughfare' },
    { cellId: 'pafUdprn', value: paf.udprn, labelText: '[PAF] UDPRN' },
    { cellId: 'pafWelshDependentLocality', value: paf.welshDependentLocality, labelText: '[PAF] Welsh Dependent Locality' },
    { cellId: 'pafWelshDependentThoroughfare', value: paf.welshDependentThoroughfare, labelText: '[PAF] Welsh Dependent Thoroughfare' },
    { cellId: 'pafWelshDoubleDependentLocality', value: paf.welshDoubleDependentLocality, labelText: '[PAF] Welsh Double Dependent Locality' },
    { cellId: 'pafWelshPostTown', value: paf.welshPostTown, labelText: '[PAF] Welsh Post Town' },
    { cellId: 'pafWelshThoroughfare', value: paf.welshThoroughfare, labelText: '[PAF] Welsh Thoroughfare' },

    // Now add the nag map
    { cellId: 'nagAddressBasePostal', value: nag.addressBasePostal, labelText: '[NAG] Address Base Postal' },
    { cellId: 'nagLegalName', value: nag.legalName, labelText: '[NAG] Legal Name' },
    { cellId: 'nagLevel', value: nag.level, labelText: '[NAG] Level' },
    { cellId: 'nagLocalCustodianCode', value: nag.localCustodianCode, labelText: '[NAG] Local Custodian Code' },
    { cellId: 'nagLocalCustodianGeogCode', value: nag.localCustodianGeogCode, labelText: '[NAG] Local Custodian Geog Code' },
    { cellId: 'nagLocalCustodianName', value: nag.localCustodianName, labelText: '[NAG] Local Custodian Name' },
    { cellId: 'nagLocality', value: nag.locality, labelText: '[NAG] Locality' },
    { cellId: 'nagLogicalStatus', value: nag.logicalStatus, labelText: '[NAG] Logical Status' },
    { cellId: 'nagLpiEndDate', value: nag.lpiEndDate, labelText: '[NAG] LPI End Date' },
    { cellId: 'nagLpiKey', value: nag.lpiKey, labelText: '[NAG] LPI Key' },
    { cellId: 'nagLpiStartDate', value: nag.lpiStartDate, labelText: '[NAG] LPI Start Date' },
    { cellId: 'nagOfficialFlag', value: nag.officialFlag, labelText: '[NAG] Official Flag' },
    { cellId: 'nagOrganisation', value: nag.organisation, labelText: '[NAG] Organisation' },
    { cellId: 'nagPostcodeLocator', value: nag.postcodeLocator, labelText: '[NAG] Postcode Locator' },
    { cellId: 'nagStreetDescriptor', value: nag.streetDescriptor, labelText: '[NAG] Street Descriptor' },
    { cellId: 'nagTownName', value: nag.townName, labelText: '[NAG] Town Name' },
    { cellId: 'nagUprn', value: nag.uprn, labelText: '[NAG] UPRN' },
    { cellId: 'nagUsrn', value: nag.usrn, labelText: '[NAG] USRN' },

  ]

  return valueCellToAddressValueMap.filter(item => keysToShow.includes(item.cellId));
}

export function addOrRemoveAttributeFromFavourites(cellIdNameOfAttribute) {
  // Get the current favourites from local storage
  const currentFavourites = getFavouritesFromLocalStorage();

  let updatedFavourites = [];
  if (currentFavourites.includes(cellIdNameOfAttribute)) {
    updatedFavourites = currentFavourites.filter(item => item !== cellIdNameOfAttribute);
  } else {
    updatedFavourites = [...currentFavourites, cellIdNameOfAttribute];
  }

  // Save back to local storage
  setGlobalValues( { favouriteAddressAttributes: updatedFavourites } );
}

function generateRowFromTemplate(rowClone, valuePair) {
  // Remove the "rowClone" id to avoid duplicates
  rowClone.removeAttribute('id');

  // Get handles on the name and value cells and favourite checkbox
  const nameCell = rowClone.querySelector('.attribute-name-placeholder');
  const valueCell = rowClone.querySelector('.attribute-value-placeholder');
  const favouriteCheckbox = rowClone.querySelector('.favourite-checkbox');

  // Add the class to each row for styling and handles
  valueCell.classList.add(`attribute-value-${valuePair.cellId}`);
  nameCell.classList.add(`attribute-name-${valuePair.cellId}`);
  favouriteCheckbox.classList.add(`favourite-checkbox-${valuePair.cellId}`);

  // Set the name and value for each row
  nameCell.textContent = valuePair.labelText;
  valueCell.textContent = valuePair.value || '';

  // Set the HTML attribute "checked" to "true"
  favouriteCheckbox.setAttribute('checked', 'true');

  // Add an event listener to the checkbox to handle adding/removing from favourites
  favouriteCheckbox.addEventListener('change', () => {
    addOrRemoveAttributeFromFavourites(valuePair.cellId);
  });

  return rowClone;
}

export function setupAttributesTable(addressCardHtmlObject, addressObject) {
  // Get a handle on the table body
  const tableBody = addressCardHtmlObject.querySelector('#table-body-for-address-attributes');

  // Copy the example row 
  const exampleRow = addressCardHtmlObject.querySelector('#example-table-row');

  // Return { cellId: , value:  } pairs for FAVOURITE KEYS
  const favouritePairs = getFavouriteCellIdValuePairs(addressObject);

  for (const valuePair of favouritePairs) {
    // Clone the example row
    const rowClone = exampleRow.cloneNode(true);

    // Generate a new row from the template
    const newRow = generateRowFromTemplate(rowClone, valuePair);

    // Add the row to the table
    tableBody.appendChild(newRow);
  }

  // Remove the example row
  exampleRow.remove();
}