import { getPageLocalValues } from "/static/js/f_helpers/local_storage_page_helpers.mjs";

function getCsvFromAddressObjects(previousAddresses) {
  // Given a list of address objects, generate CSV content as a string

  const headers = Object.keys(previousAddresses[0]);

  // Set the fields to wrap in quotes as not to break csv
  const quotedFields = new Set(['name']); 

  // For now remove the paf and nag objcts as they require flattening (functionality is present in the favourites table generation module, but will be made available as a global helper soon)
  const excluded = new Set(['paf', 'nag']);
  const filteredHeaders = headers.filter(h => !excluded.has(h));

  const csvRows = [
    // First make the header row
    filteredHeaders.join(','), 

    // Then make each data row:
    ...previousAddresses.map(obj =>

      // For every address, check each key's value
      filteredHeaders.map(key => {
        // Blank string on falsey
        const value = obj[key] ?? '';

        // Convert to string
        const strValue = String(value);

        // Wrap fields in the 'quotedFields' set in quotes
        if (quotedFields.has(key)) {
          const escaped = strValue.replace(/"/g, '""');
          return `"${escaped}"`;
        }

        return strValue; 
      }).join(',')

    )
  ];

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