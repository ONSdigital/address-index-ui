import { getPageLocalValues, getGlobalValues } from "/static/js/f_helpers/local_storage_page_helpers.mjs";
import { getPopulatedAttributeMap, getPopulatedAttributeMapOnlyFavourites } from "/static/js/f_helpers/address_attribute_map.mjs";
import { triggerDownloadOfFile } from "/static/js/macros/custom_download_results_from_local_storage/download_helpers.mjs";

function getKeysToBecomeHeader(attributeInclusionSetting) {
  const globalValues = getGlobalValues();

  // If the setting is only for favourites, return those keys
  if (attributeInclusionSetting === 'favourites_only') {
    return globalValues.favouriteAddressAttributes || [];
  }

  // If the setting is for all attributes, return all possible keys
  if (attributeInclusionSetting === 'all') {
    // Get a populated attribute map for an empty object to get all keys
    const allAttributesMap = getPopulatedAttributeMap({});
    const allKeys = allAttributesMap.map( (attribute) => attribute.cellId );
    return allKeys;
  }
}

function getCsvHeaderRow(attributeInclusionSetting) {
  // Get the global favourite keys to use as headers

  const keysToBecomeHeader = getKeysToBecomeHeader(attributeInclusionSetting);

  // Create header row string
  const headerRowValues = keysToBecomeHeader.map( (key) => {
    return `"${key}"`;
  });

  const headerRowString = headerRowValues.join(',');
  return headerRowString;
}

function getCsvFromAddressObjects(previousAddresses, attributeInclusionSetting) {
  // Given a list of address objects, generate CSV content as a string

  // Start by looping over each address, and applying the map
  const csvRows = [getCsvHeaderRow(attributeInclusionSetting)];
  for (const addressObject of previousAddresses) {

    // Populate the attribute map for this address - checking for the global setting to see if all attributes are included 
    let currentAddress = {};
    if (attributeInclusionSetting === 'favourites_only') {
      currentAddress = getPopulatedAttributeMapOnlyFavourites(addressObject);
    } else {
      currentAddress = getPopulatedAttributeMap(addressObject);
    }

    const rowValues = currentAddress.map( (valuePair) => {
      // Escape double quotes in values
      const safeValue = String(valuePair.value).replace(/"/g, '""');
      return `"${safeValue}"`;
    });

    // Join as a string and push to csvRows
    const rowString = rowValues.join(',');
    csvRows.push(rowString);
  }

  // Join the rows together
  const csvContent = csvRows.join('\r\n');
  return csvContent;
}

export function downloadCsvFromLocalStorage(page_name) {
  // Get the user preferences for the download
  const globalValues = getGlobalValues();
  const attributeInclusionSetting = globalValues.singleJobDownloadAttributeInclusion || 'all';

  // Get the address objects from local storage for this page
  const localPageValues = getPageLocalValues(page_name);
  const previousAddresses = localPageValues.mostRecentlySearchedAddresses || [];

  if (!previousAddresses.length) {
    console.warn('No addresses to export.');
    return;
  }

  // Generate CSV content
  const csvContent = getCsvFromAddressObjects(previousAddresses, attributeInclusionSetting);

  // Create CSV name
  const matchNumber = previousAddresses.length;
  const fileName = `${page_name}_results_${matchNumber}_matches.csv`;

  // Trigger download
  triggerDownloadOfFile(fileName, 'csv', csvContent);
}