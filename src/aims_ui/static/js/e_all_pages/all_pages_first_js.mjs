import {
  setDefaultTitleChoice,
  setDefaultColumnWidths,
  setDefaultAdditionalRequestStatus,
  setDefaultResponseFormatCustomResponse,
  setDefaultJobAgePreferences,
} from '/static/js/f_helpers/local_storage_helpers.mjs';

import { addMostRecentPageToStorage } from '/static/js/e_all_pages/breadcrumb_helpers/breadcrumbHelpers.mjs';


function setDefaultValuesIfUnset() {
  setDefaultTitleChoice();
  setDefaultColumnWidths();
  setDefaultAdditionalRequestStatus();
  setDefaultResponseFormatCustomResponse();
  setDefaultJobAgePreferences();
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

window.addEventListener('load', init);
