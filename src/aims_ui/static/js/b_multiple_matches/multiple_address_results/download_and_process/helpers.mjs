import { getPageLocalValues } from '/static/js/f_helpers/local_storage_page_helpers.mjs';

export function getAllLinksAndParents() {
  const tableLinks = [];
  const table = document.querySelector('#adjustLinksTable');
  const links = table.querySelectorAll('a');
  for (const link of links) {
    const linkElement = link;
    const linkParent = link.parentNode;

    const headerCellIndex = linkParent.cellIndex - 2;
    const row = linkParent.parentNode;
    const headerRowCell = row.cells[headerCellIndex];

    tableLinks.push({
      link: linkElement,
      parent: linkParent,
      headerRowCell: headerRowCell,
    });
  }
  return tableLinks;
}

export function findIfPafOrNagWasUsed(address) {
  // Receiving a single "address" from a response, return PAF or NAG
  const formattedAddress = address['formattedAddress'];
  const pafAddress = address['formattedAddressPaf'];
  const nagAddress = address['formattedAddressNag'];
  if (formattedAddress === pafAddress) {
    return 'PAF';
  } else if (formattedAddress === nagAddress) {
    return 'NAG';
  } else {
    return 'N/A';
  }
}

export function getAddressAttributesSelectedByUserFromMultipleAddressAttributesPage() {
  const customAttributesPageData = getPageLocalValues('multiple_address_attributes')
  const attributesSelectedByUser = customAttributesPageData.pagePreviouslySearchedValues;

  console.debug('User selected custom attributes from multiple_address_attributes page:', attributesSelectedByUser);
  return attributesSelectedByUser;
}

export function returnNewlineIfNotBlank(testString) {
  if (/^[\s\n]*$/.test(testString)) {
    return '';
  } else {
    return '\n';
  }
}

export function getNameOfJobFromCell(cell, backupName) {
  const row = cell.closest('tr');
  const cells = row.querySelectorAll('td');
  const secondCellText = cells[1].textContent;
  const strippedText = secondCellText.trim();
  const result = strippedText === '' ? backupName : strippedText;

  return result;
}

