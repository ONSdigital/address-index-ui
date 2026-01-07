// scripts to make the templated address info work

import { getPageLocalValues } from '/static/js/f_helpers/local_storage_page_helpers.mjs';
import { createATemplate } from '/static/js/macros/sub_components/sub_custom_attributes_table/template_helpers.mjs';

export function createTemplates(addressObjects) {
  // Get a handle on the container
  const container = document.querySelector('#container-for-address-cards');

  // Loop over all addresses and create a filled out template for each
  for (const address of addressObjects) {
    const clonedTemplate = createATemplate(address);
    container.append(clonedTemplate);
  }
}

function deleteExistingCards() {
  const container = document.querySelector('#container-for-address-cards');
  container.replaceChildren(); // Remove all existing children
}

function refreshAddressInfoCards(page_name) {
  // Clear any existing cards
  deleteExistingCards();

  // Get the addresses from local storage
  const pageLocalValues = getPageLocalValues(page_name);
  const addresses = pageLocalValues.mostRecentlySearchedAddresses || [];

  createTemplates(addresses);
}

export function init(page_name) {
  // Setup an event listener for the custom event 'refreshAddressInfoCards'
  document.addEventListener('refreshAddressInfoCards', () => {
    refreshAddressInfoCards(page_name);
  });

  // Initially also run the refresh to load any existing cards
  refreshAddressInfoCards(page_name);
}