import { 
  setDefaultTitleChoice,
  setDefaultColumnWidths,
  setDefaultAdditionalRequestStatus,
  setDefaultResponseFormatCustomResponse,
} from '/static/js/f_helpers/local_storage_helpers.mjs';

function setDefaultValuesIfUnset() {
  setDefaultTitleChoice();
  setDefaultColumnWidths();
  setDefaultAdditionalRequestStatus();
  setDefaultResponseFormatCustomResponse();
}

function init() {
  console.log('all_pages_first loaded');
  setDefaultValuesIfUnset();
}

window.addEventListener('load', init);




