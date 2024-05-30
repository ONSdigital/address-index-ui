import {
  saveToLocalStorage,
  wipeLocalStorage,
} from '/static/js/f_helpers/local_storage_helpers.mjs';

// Add all the inputs into an array, ignoring dropdowns
function getInputObjects() {
  const inps = document.querySelectorAll('.ons-input');
  const final = [];
  for (const a of inps) {
    if (!a.classList.contains('ons-input--select')) {
      if (!a.classList.contains('nocache')) {
        final.push(a);
      }
    }
  }
  return final;
}

function getInputObjectValues() {
  const inputs = getInputObjects();
  const input_obj = {};
  for (const a of inputs) {
    input_obj[a.id] = a.value;
  }
  return input_obj;
}

function setupEventListeners(loc) {
  // Add event listener to save data when the form is submitted
  const form = document.querySelector('form');
  form.addEventListener('submit', (e) => {
    const inputObjectValues = getInputObjectValues();
    saveToLocalStorage(inputObjectValues, loc);
  });

  const clear_button = document.querySelector('#clear-form-data-button-id');
  clear_button.addEventListener('click', (e) => {
    wipeLocalStorage(loc);
  });
}

function loadStoredValuesIfExist(loc) {
  const inputs = getInputObjects();
  // Load values on page load if they exist
  const stored_vals = localStorage.getItem(loc);
  if (stored_vals) {
    const parsed_vals = JSON.parse(stored_vals);
    for (const inp of inputs) {
      const current_val = parsed_vals[inp.id];
      if (current_val) {
        inp.value = current_val;
      }
    }
  }
}

function init() {
  console.log('save_inputs loaded');
  const loc = window.location.href;
  loadStoredValuesIfExist(loc);
  setupEventListeners(loc);
}

window.addEventListener('load', init);
