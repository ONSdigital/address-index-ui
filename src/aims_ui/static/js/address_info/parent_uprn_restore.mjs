import { crEl } from "/static/js/f_helpers/element_creation.mjs";
import { getCellFromTable, getCurrentAddress } from '/static/js/address_info/helpers.mjs';

function replaceOverviewTableParentUprnValue(parentUprn) {
  // Now find the cell next to "parent_urpn" in the overview table
  const overviewTable = document.querySelector('#overviewTable');
  const parentUprnLabelCell = getCellFromTable(overviewTable, 'parent_uprn');
  const parentUprnValueCell = parentUprnLabelCell.nextElementSibling;

  // Now change the text content to be a link to the parent UPRN
  const parentUprnLink = crEl('a');
  parentUprnLink.href = '/address_info/' + parentUprn;
  parentUprnLink.textContent = parentUprn;

  // Clear the existing content of the cell and add the link
  parentUprnValueCell.textContent = '';
  parentUprnValueCell.appendChild(parentUprnLink);
}

export function changeParentUprnToLink(mostRecentlySearchedAddresses) {
  // Get the address json for the UPRN in the URL
  const currentAddress = getCurrentAddress(mostRecentlySearchedAddresses);
  const parentUprn = currentAddress.parentUprn;

  // If the parent UPRN is not '0' or 'NA', replace the cell content with a link
  if (parentUprn && String(parentUprn) !== '0' && String(parentUprn).toUpperCase() !== 'NA') {
    replaceOverviewTableParentUprnValue(parentUprn);
  }
}