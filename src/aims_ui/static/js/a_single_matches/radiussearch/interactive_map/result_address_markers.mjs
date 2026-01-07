// Code to get the address info from local storage and add
// markers to the map for each address


import { getPageLocalValues } from '/static/js/f_helpers/local_storage_page_helpers.mjs';
import { makePinIcon } from '/static/js/a_single_matches/radiussearch/interactive_map/map_pin_icons.mjs';

const resultsMarkerIcon = makePinIcon("#a8bd3a");

// Store the markers so we can remove them if needed
const searchMarkers = [];

export function refreshSearchMarkersFromLocalStorage(map) {
  // First delete any existing markers
  deleteSearchMarkers(map);

  // Now add the markers afresh
  addMatchedAddressMarkersToMap(map);
}

export function addMatchedAddressMarkersToMap(map) {
  const addresses = getMatchedAddressesFromLocalStorage();

  for (const address of addresses) {
    // Addresses in the format {name: '', uprn: '', longitude: '', latitude: ''}
    const { formattedAddress, uprn, longitude: long, latitude: lat } = address;

    // The marker should be ONS colours and link to /address_info/{uprn}
    const marker = L.marker([lat, long], {icon: resultsMarkerIcon} ).addTo(map).bindPopup(`${formattedAddress} <br> <a href="/address_info/${uprn}">View Details</a>`);

    searchMarkers.push(marker);
  }
}

function getMatchedAddressesFromLocalStorage() {
  // Get the most recent addresses from local storage
  const localPageValues = getPageLocalValues('radiussearch');

  // Default to an empty array if not found
  const addresses = localPageValues.mostRecentlySearchedAddresses || [];
  return addresses;
}

function deleteSearchMarkers(map) {
  for (const marker of searchMarkers) {
    map.removeLayer(marker);
  }

  searchMarkers.length = 0;
}
