// This should be called if the Nunucks Macro has been called without "results_page == True"
// As it's not expected to be "fresh" results, we should load previous results from local storage

import { getPageLocalValues } from "/static/js/f_helpers/local_storage_page_helpers.mjs";
import { crEl } from "/static/js/f_helpers/element_creation.mjs";

function generateRow(singleAddressObject) {
  // Create the row DOM elements
  const row = crEl('tr', null, ['ons-table__row']);

  // Name cell contains a link to the UPRN and the text of the formatted cell
  const nameCell = crEl('td', null, ['ons-table__cell']);
  const nameLink = crEl('a');
  nameLink.href = '/address_info/' + singleAddressObject.uprn;
  nameLink.textContent = singleAddressObject.name;

  nameCell.append(nameLink);

  // Lat 
  const latCell = crEl('td', null, ['ons-table__cell']);
  latCell.textContent = singleAddressObject.latitude;

  // Lon
  const longCell = crEl('td', null, ['ons-table__cell']);
  longCell.textContent = singleAddressObject.longitude;

  // Distance (content should be created automatically with the class 'distance_attribute')
  const distanceCell = crEl('td', null, ['ons-table__cell', 'distance_attribute']);
  // Set custom attribute of "myLat"
  distanceCell.setAttribute('myLat', singleAddressObject.latitude);
  distanceCell.setAttribute('myLon', singleAddressObject.longitude);

  row.append(nameCell, latCell, longCell, distanceCell);
  return row;
}

function loadPreviousValuesForCompressedTableView() {
  // For the compressed view (where only Name, lat, long, distance are shown in a table)

  // Get the values of the addresses
  const localPageValues = getPageLocalValues('radiussearch');
  const previousAddresses = localPageValues.radiusSearchMostRecentAddresses || [];

  // Get a handle on the table element that we're to attach rows to
  const tableBody = document.querySelector('.ons-table__body');

  // For every address in the previous addresses, create a row and add it
  for (const address of previousAddresses) {
    const row = generateRow(address);
    tableBody.append(row);
  }
}

loadPreviousValuesForCompressedTableView();