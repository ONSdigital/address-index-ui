import { setupAttributesTable } from '/static/js/macros/sub_components/sub_custom_attributes_table/favourite_table_generation.mjs';
import { getGlobalValues } from '/static/js/f_helpers/local_storage_page_helpers.mjs';

// Scripts to fill the template info for each address

function getTitleText(addressObject) {
  // Check the global value for addressCardTitleType
  const globalValues = getGlobalValues();
  const titlePreference = globalValues.addressCardTitleType || 'default';

  const formattedAddressPaf = addressObject.formattedAddressPaf;
  const formattedAddressNag = addressObject.formattedAddressNag;
  const formattedAddressDefault = addressObject.formattedAddress;

  if (titlePreference === 'paf' && formattedAddressPaf) {
    // If the user has selected paf, and the paf version exists, use that
    return formattedAddressPaf;
  } else if (titlePreference === 'nag' && formattedAddressNag) {
    // If the user has selected nag, and the nag version exists, use that
    return formattedAddressNag;
  } 

  // If the user has selected default, or the preferred format does not exist, use the formatted address
  return formattedAddressDefault;
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

  // Setup the attributes values table (only show favourites)
  const showAllAttributes = false;
  setupAttributesTable(addressCardHtmlObject, addressObject, showAllAttributes);

  return addressCardHtmlObject;
}