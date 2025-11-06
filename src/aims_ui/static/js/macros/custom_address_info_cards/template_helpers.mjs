// Scripts to fill the template info for each address

const keysToShow = ['lpiLogicalStatus', 'formattedAddress', 'uprn', 'confidenceScore', 'underlyingScore'];

function getTitleText(addressObject) {
  // The user might have set a preference for PAF or NAG
  // For now, just return the formattedAddress
  return addressObject.formattedAddress;
}

function setupTitleAndLink(addressCard, addressObject) {
  // Get a handle on the link and add href
  const link = addressCard.querySelector('#link-to-address-info-uprn');
  link.href = '/address_info/' + addressObject.uprn;

  // Get a handle on the title and set text
  const title = addressCard.querySelector('#name-of-address-user-dictated');
  title.textContent = getTitleText(addressObject);
}

function setupMapsLink(addressCard, addressObject) {
  // Get a handle on the maps link
  const mapLinkElement = addressCard.querySelector('#link-to-address-on-map');
  const mapUrl = 'https://maps.google.com/?q=' + addressObject.latitude + ',' + addressObject.longitude + '&ll=' +  addressObject.latitude + ',' + addressObject.longitude + '&z=18' +'&basemap=satellite';
  mapLinkElement.href = mapUrl;
}

function setupAttributesTable(addressCard, addressObject) {
  // Get a handle on the table body
  const tableBody = addressCard.querySelector('#table-body-for-address-attributes');

  // Copy the example row 
  const exampleRow = addressCard.querySelector('#example-table-row');

  for (const key of keysToShow) {
    // Clone the example row
    const rowClone = exampleRow.cloneNode(true);

    // Get handles on the name and value cells
    const nameCell = rowClone.querySelector('#attribute-name-placeholder');
    const valueCell = rowClone.querySelector('#attribute-value-placeholder');
    nameCell.textContent = key;
    // Default to blank if no value
    valueCell.textContent = addressObject[key] || '';

    tableBody.appendChild(rowClone);
  }

  // Remove the example row
  exampleRow.remove();
}

export function createATemplate(addressObject) {
  // Given a single address object

  // Clone the template
  const template = document.querySelector('#template-for-address-info-card');
  const addressCard = template.content.cloneNode(true);

  // Fill in the static details
  setupTitleAndLink(addressCard, addressObject);

  // Setup the maps link
  setupMapsLink(addressCard, addressObject);

  // Setup the attributes values table
  setupAttributesTable(addressCard, addressObject);

  return addressCard;
}