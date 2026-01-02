import {
  setDefaultResponseFormatCustomResponse,
} from '/static/js/f_helpers/local_storage_helpers.mjs';

import { setupDefaultGlobalValues } from '/static/js/e_all_pages/setup_defaults.mjs';

import { addMostRecentPageToStorage } from '/static/js/e_all_pages/breadcrumb_helpers/breadcrumbHelpers.mjs';


function setDefaultValuesIfUnset() {
  setDefaultResponseFormatCustomResponse();

  setupDefaultGlobalValues();
}

function removeResubmissionMessage() {
  if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
  }
}

function init() {
  console.log('all_pages_first loaded');
  setDefaultValuesIfUnset();
  addMostRecentPageToStorage();
  removeResubmissionMessage();
}

// Immedaitely run to enforce first execution
init();