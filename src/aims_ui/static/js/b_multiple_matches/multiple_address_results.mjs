import { getJobAgePreference } from '../f_helpers/local_storage_helpers.mjs';

export function getAllLinks() {
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

function getAddressesFromResponse(apiResponse) {
  // Given an API response (string), extract a list of all matched addresses, confidence score, document score
  // Extract the list of matched addresses
  const matchedAddresses = [];
  if (apiResponse.toString() === '') {
    return [];
  }
  const jsonResponse = JSON.parse(apiResponse);
  const response = jsonResponse['response'];
  const addresses = response['addresses'];
  // Get the values needed for each address (each address comes from one submitted address)
  let i = 0;
  for (const address of addresses) {
    i = i + 1;
    const formattedAddress = address['formattedAddress'];
    const uprn = address['uprn'];
    const matchType = response.matchtype;
    const confidenceScore = address['confidenceScore'];
    const documentScore = address['underlyingScore'];
    const rank = i;
    const addressTypePafNag = findIfPafOrNagWasUsed(address);
    const airRating = address['airRating'];
    const addressToAdd = [
      formattedAddress,
      uprn,
      matchType,
      confidenceScore,
      documentScore,
      rank,
      addressTypePafNag,
      airRating,
    ];
    matchedAddresses.push(addressToAdd);
  }
  return matchedAddresses;
}

function returnNewlineIfNotBlank(testString) {
  if (/^[\s\n]*$/.test(testString)) {
    return '';
  } else {
    return '\n';
  }
}

function arrayToCSV(data) {
  const csvRows = data.map((row) =>
    row
      .map((cell) => {
        // Escape double quotes in CSV data
        const cellString = String(cell).replace(/"/g, '""');
        // Wrap values containing commas or double quotes in double quotes
        return /,|"/.test(cellString) ? `"${cellString}"` : cellString;
      })
      .join(',')
  );

  return csvRows.join('\r\n') + returnNewlineIfNotBlank(csvRows);
}

function processRow(row) {
  // Process [id, inputAddress, APIresponse]
  // to be in same format as <5k match
  // console.log(row);['119113', '5 SOWTON EX8 9DD', '{"apiVersion":"1.0.1

  // Check not blank or header row
  if (row.length !== 3) {
    return '';
  }
  if (row[2].toString() === 'response') {
    return '';
  }

  // Get info for a single row
  const id = row[0];
  const inputAddress = row[1];
  const matchedAddresses = getAddressesFromResponse(row[2]);

  // Expand (same id and input address for each matched address)
  const finalMatches = [];
  for (const matchedAddress of matchedAddresses) {
    // Add each address with quotes for csv parsing
    const final_row = [
      id,
      inputAddress,
      matchedAddress[0],
      matchedAddress[1],
      matchedAddress[2],
      matchedAddress[3],
      matchedAddress[4],
      matchedAddress[5],
      matchedAddress[6],
      matchedAddress[7],
    ];
    finalMatches.push(final_row);
  }

  // If 5 addresses match, finalMatches contains an array of 5 items, each containing [ id, search address, matched address, confidence score, document score, rank]
  const csvFormat = arrayToCSV(finalMatches);
  return csvFormat;
}

async function downloadAndProcess(url, headerStatus) {
  let final_csv = '';
  if (headerStatus.toString() !== 'False') {
    final_csv =
      'id,inputAddress,matchedAddress,uprn,matchType,confidenceScore,documentScore,rank,addressType(Paf/Nag),airRating\n';
  }
  const response = await fetch(url);
  const arrayBuffer = await response.arrayBuffer();
  // eslint-disable-next-line no-undef
  const inflated = await pako.inflate(arrayBuffer);
  const csvString = new TextDecoder().decode(inflated);
  // eslint-disable-next-line no-undef
  const parsedCSV = Papa.parse(csvString).data;

  parsedCSV.forEach((row) => {
    // Row = [id, inputAddress, APIresponse]
    final_csv = final_csv + processRow(row);
  });

  return await final_csv;
}

async function changeLinkToButton(linkParentMetadata) {
  // Make the Download Button
  const originalButton = document.querySelector('#downloadButtonTemplate');
  const clonedButton = originalButton.cloneNode(true);

  const cell = linkParentMetadata.parent;

  linkParentMetadata.parent.append(clonedButton);

  clonedButton.addEventListener('click', async function () {
    // Make Spin Load
    clonedButton.classList.add('ons-is-loading');

    // Get header option status
    const headerStatus = linkParentMetadata.headerRowCell.textContent
      .trim()
      .replace(/\s+/g, ' ');

    // Get CSV content
    const csv = await downloadAndProcess(
      linkParentMetadata.link.href,
      headerStatus
    );

    // Make a new blob
    const blob = new Blob([csv], { type: 'text/csv' });

    // Make 'a' with link to finalised csv content, then download
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    const fileName = getNameOfJobFromCell(
      cell,
      linkParentMetadata.link.textContent
    );
    a.download = fileName + '.csv';
    a.click();
    clonedButton.classList.remove('ons-is-loading');
  });
  linkParentMetadata.link.remove();
}

function getNameOfJobFromCell(cell, backupName) {
  const row = cell.closest('tr');
  const cells = row.querySelectorAll('td');
  const secondCellText = cells[1].textContent;
  const strippedText = secondCellText.trim();
  const result = strippedText === '' ? backupName : strippedText;

  return result;
}

function addJobsFlagToCurrentURL() {
  // Get the current preference
  const currentJobPreference = getJobAgePreference();
  const currentURL = window.location.href;
  // Check to see if the flag alredy exists
  if (currentURL.includes('include_old_jobs')) {
    return;
  } else {
    const url = new URL(currentURL);
    url.searchParams.set('include_old_jobs', currentJobPreference);
    // Forward user to the new URL
    window.history.pushState({}, '', url);
    // Trigger new page load
    window.location.reload();
  }
}

window.addEventListener('load', async function () {
  // Check the jobs flag - this is a fallback check as it should already be appended to the URL
  addJobsFlagToCurrentURL();

  // Change all links to "download" buttons
  const linksAndParents = getAllLinks();
  for (const l of linksAndParents) {
    await changeLinkToButton(l);
  }
});
