import { getPageLocalValues, getGlobalValues } from "/static/js/f_helpers/local_storage_page_helpers.mjs";
import { getPopulatedAttributeMapOnlyFavourites } from "/static/js/f_helpers/address_attribute_map.mjs";

function getCsvHeaderRow() {
  // Get the global favourite keys to use as headers
  const globalValues = getGlobalValues();
  const favouriteKeys = globalValues.favouriteAddressAttributes || [];

  // Create header row string
  const headerRowValues = favouriteKeys.map( (key) => {
    return `"${key}"`;
  });

  const headerRowString = headerRowValues.join(',');
  return headerRowString;
}

function getCsvFromAddressObjects(previousAddresses) {
  // Given a list of address objects, generate CSV content as a string

  // Start by looping over each address, and applying the map
  const csvRows = [getCsvHeaderRow()];
  for (const addressObject of previousAddresses) {
    // Populate the attribute map for this address, only favourites
    const currentAddress = getPopulatedAttributeMapOnlyFavourites(addressObject);

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

function triggerDownloadOfCsvFile(fileName, csvContent) {
  // Create CSV Blob and trigger download
  const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
  const url = URL.createObjectURL(blob);

  const link = document.createElement('a');
  link.href = url;
  link.setAttribute('download', fileName);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);

  // Cleanup URL object
  URL.revokeObjectURL(url);
}

export function downloadCsvFromLocalStorage(page_name) {
  // Get the address objects from local storage for this page
  const localPageValues = getPageLocalValues(page_name);
  const previousAddresses = localPageValues.mostRecentlySearchedAddresses || [];

  if (!previousAddresses.length) {
    console.warn('No addresses to export.');
    return;
  }

  // Generate CSV content
  const csvContent = getCsvFromAddressObjects(previousAddresses);

  // Create CSV name
  const matchNumber = previousAddresses.length;
  const fileName = `${page_name}_results_${matchNumber}_matches.csv`;

  // Trigger download
  triggerDownloadOfCsvFile(fileName, csvContent);
}