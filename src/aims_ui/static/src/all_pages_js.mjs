import { 
  setDefaultTitleChoice,
  setDefaultColumnWidths
} from './local_storage_helpers.mjs';

function setDefaultValuesIfUnset() {
  setDefaultTitleChoice();
  setDefaultColumnWidths();
}

function init() {
  setDefaultValuesIfUnset();
  console.log(localStorage);
}

window.addEventListener('load', init);




