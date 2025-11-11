import { setupAttributesTable } from '/static/js/macros/custom_address_info_cards/favourite_table_generation.mjs';

// Scripts to fill the template info for each address

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

export function createATemplate(addressObject) {
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

  return addressCardHtmlObject;
}