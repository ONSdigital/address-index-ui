import { 
  setDefaultTitleChoice,
  setDefaultColumnWidths,
  setDefaultAdditionalRequestStatus,
} from './local_storage_helpers.mjs';

function setDefaultValuesIfUnset() {
  setDefaultTitleChoice();
  setDefaultColumnWidths();
  setDefaultAdditionalRequestStatus();
}

function init() {
  setDefaultValuesIfUnset();
}

window.addEventListener('load', init);




