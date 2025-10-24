// Code to get the address info from local storage and add
// markers to the map for each address


import { getPageLocalValues } from '/static/js/f_helpers/local_storage_page_helpers.mjs';
import { makePinIcon } from '/static/js/a_single_matches/radiussearch/interactive_map/map_pin_icons.mjs';

const resultsMarkerIcon = makePinIcon("#a8bd3a");

function getMatchedAddressesFromLocalStorage() {
  // Get the most recent addresses from local storage
  const localPageValues = getPageLocalValues('radiussearch');

  // Default to an empty array if not found
  const addresses = localPageValues.mostRecentlySearchedAddresses || [];
  return addresses;
}

export function addMatchedAddressMarkersToMap(map) {
  const addresses = getMatchedAddressesFromLocalStorage();

  for (const address of addresses) {
    // Addresses in the format {name: '', uprn: '', longitude: '', latitude: ''}
    const { name, uprn, longitude: long, latitude: lat } = address;

    // The marker should be ONS colours and link to /address_info/{uprn}
    L.marker([lat, long], {icon: resultsMarkerIcon} ).addTo(map).bindPopup(`${name} <br> <a href="/address_info/${uprn}">View Details</a>`);
  }
}
