import {
  setDefaultTitleChoice,
  setDefaultColumnWidths,
  setDefaultAdditionalRequestStatus,
  setDefaultResponseFormatCustomResponse,
  setDefaultJobAgePreferences,
} from '/static/js/f_helpers/local_storage_helpers.mjs';

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
  removeResubmissionMessage();
}

window.addEventListener('load', init);
