
function getCurrentUprn() {
  // Get the UPRN from the URL (... /address_info/1234567890123)
  const urlParts = window.location.pathname.split('/');
  const uprn = urlParts[urlParts.length - 1];

  return uprn;
}

// Get the address json for the UPRN in the URL
export function getCurrentAddress(mostRecentlySearchedAddresses) {
  const uprn = getCurrentUprn();

  for (const address of mostRecentlySearchedAddresses) {
    if (String(address.uprn) === String(uprn)) {
      return address;
    } 
  }
}

export function getCellFromTable(table, rowText) {
  const rows = table.getElementsByTagName('tr');
  for (let i = 0; i < rows.length; i++) {
    const cells = rows[i].getElementsByTagName('td');
    for (let j = 0; j < cells.length; j++) {
      if ( String(cells[j].textContent).includes(rowText) ) {
        return cells[j];
      }
    }
  }
  return null;
}