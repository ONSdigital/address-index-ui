// scripts to make the templated address info work

import { getPageLocalValues } from '/static/js/f_helpers/local_storage_page_helpers.mjs';
import { createATemplate } from '/static/js/macros/custom_address_info_cards/template_helpers.mjs';

function createTemplates(addressObjects) {
  // Get a handle on the container
  const container = document.querySelector('#container-for-address-cards');

  // Loop over all addresses and create a filled out template for each
  for (const address of addressObjects) {
    const clonedTemplate = createATemplate(address);
    container.append(clonedTemplate);
  }
}

export function init(page_name) {
  const pageLocalValues = getPageLocalValues(page_name);
  const addresses = pageLocalValues.mostRecentlySearchedAddresses || [];

  createTemplates(addresses);
}