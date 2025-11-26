import { getPageLocalValues, getGlobalValues } from "/static/js/f_helpers/local_storage_page_helpers.mjs";
import { getPopulatedAttributeMapOnlyFavourites } from "/static/js/f_helpers/address_attribute_map.mjs";
import { triggerDownloadOfFile } from "/static/js/macros/custom_download_results_from_local_storage/download_helpers.mjs";

function getJsonFromAddressObjects(previousAddresses) {
  // Given a list of address objects, generate JSON content as a string
  
  // Start by looping over each address, and applying the map
  const jsonAddresses = [];
  for (const addressObject of previousAddresses) {
    // Populate the attribute map for this address, only favourites
    const currentAddress = getPopulatedAttributeMapOnlyFavourites(addressObject);
    jsonAddresses.push(currentAddress);
  }
  return JSON.stringify(jsonAddresses, null, 2);
}

export function downloadJsonFromLocalStorage(page_name) {
  // Get the address objects from local storage for this page
  const localPageValues = getPageLocalValues(page_name);
  const previousAddresses = localPageValues.mostRecentlySearchedAddresses || [];

  if (!previousAddresses.length) {
    console.warn('No addresses to export.');
    return;
  }

  // Generate JSON content
  const jsonContent = getJsonFromAddressObjects(previousAddresses);

  // Create JSON name
  const matchNumber = previousAddresses.length;
  const fileName = `${page_name}_results_${matchNumber}_matches.json`;

  // Trigger download
  triggerDownloadOfFile(fileName, 'json', jsonContent);
}