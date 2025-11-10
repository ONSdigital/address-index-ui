import { addDropdownAllInfo } from '/static/js/macros/custom_address_info_cards/template_dropdown_helpers.mjs';

// Scripts to fill the template info for each address

const keysToShow = ['lpiLogicalStatus', 'formattedAddress', 'uprn', 'confidenceScore', 'underlyingScore'];

function getTitleText(addressObject) {
  // The user might have set a preference for PAF or NAG
  // For now, just return the formattedAddress
  return addressObject.formattedAddress;
}

function setupTitleAndLink(addressCardHtmlObject, addressObject) {
  // Get a handle on the link and add href
  const link = addressCardHtmlObject.querySelector('#link-to-address-info-uprn');
  link.href = '/address_info/' + addressObject.uprn;

  // Get a handle on the title and set text
  const title = addressCardHtmlObject.querySelector('#name-of-address-user-dictated');
  title.textContent = getTitleText(addressObject);
}

function setupMapsLink(addressCardHtmlObject, addressObject) {
  // Get a handle on the maps link
  const mapLinkElement = addressCardHtmlObject.querySelector('#link-to-address-on-map');
  const mapUrl = 'https://maps.google.com/?q=' + addressObject.latitude + ',' + addressObject.longitude + '&ll=' +  addressObject.latitude + ',' + addressObject.longitude + '&z=18' +'&basemap=satellite';
  mapLinkElement.href = mapUrl;
}

function setupAttributesTable(addressCardHtmlObject, addressObject) {
  // Get a handle on the table body
  const tableBody = addressCardHtmlObject.querySelector('#table-body-for-address-attributes');

  // Copy the example row 
  const exampleRow = addressCardHtmlObject.querySelector('#example-table-row');

  for (const key of keysToShow) {
    // Clone the example row
    const rowClone = exampleRow.cloneNode(true);
    // Remove the "rowClone" id to avoid duplicates
    rowClone.removeAttribute('id');

    // Get handles on the name and value cells
    const nameCell = rowClone.querySelector('.attribute-name-placeholder');
    const valueCell = rowClone.querySelector('.attribute-value-placeholder');
    nameCell.textContent = key;
    // Default to blank if no value
    valueCell.textContent = addressObject[key] || '';

    tableBody.appendChild(rowClone);
  }

  // Remove the example row
  exampleRow.remove();
}

export function createATemplate(addressObject, page_name) {
  // Given a single address object

  // Clone the template
  const template = document.querySelector('#template-for-address-info-card');
  const addressCardHtmlObject= template.content.cloneNode(true);

  // Fill in the static details
  setupTitleAndLink(addressCardHtmlObject, addressObject);

  // Setup the maps link
  setupMapsLink(addressCardHtmlObject, addressObject);

  // Setup the attributes values table
  setupAttributesTable(addressCardHtmlObject, addressObject);

  // Setup the dropdown for all info
  addDropdownAllInfo(addressCardHtmlObject, addressObject, page_name);

  return addressCardHtmlObject;
}