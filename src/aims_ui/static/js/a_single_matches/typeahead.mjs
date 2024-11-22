import { saveToLocalStorage } from '/static/js/f_helpers/local_storage_helpers.mjs';

function getAllInputs() {
  const matchForm = document.querySelector('.match-form-container');
  const inputs = matchForm.querySelectorAll('input');
  return inputs
}

// Script to adjust the parameters for typeahead whenever they're updated
export function getParamsFromPage() {
  let finalParams = '&';
  const inputs = getAllInputs();
  for (const input of inputs) {
    if (input.type === 'text' && input.value !== '') {
      finalParams = finalParams + input.getAttribute('id') + '=' + input.value;
      finalParams = finalParams + '&';
    }
    if (input.type === 'radio' && input.checked) {
      finalParams = finalParams + input.name + '=' + input.id;
      finalParams = finalParams + '&';
    }
    if (input.type === 'checkbox' && input.checked) {
      finalParams = finalParams + input.id + '=' + 'true';
      finalParams = finalParams + '&';
    }
  }
  finalParams = finalParams.substring(0, finalParams.length - 1);
  return finalParams;
}

function saveParamsToLocalStorage(inputs) {
  saveToLocalStorage(inputs, 'typeahead_params');
}

export function setupEventListeners() {
  const typeaheadContainer = document.querySelector(
    '#address-autosuggest-container'
  );
  typeaheadContainer.setAttribute('data-query-params', getParamsFromPage());

  const allInputs = getAllInputs();
  for (const input of allInputs) {
    input.addEventListener('change', () => {
      // When any input is changed, update the query parameters
      typeaheadContainer.setAttribute('data-query-params', getParamsFromPage());
      // Also save the input values
      saveParamsToLocalStorage(allInputs);
    });
  }
}

function loadTypeaheadValues() {
  console.log(localStorage.getItem('typeahead_params'));
}

function init() {
  console.log('typeahead specific loaded');
  setupEventListeners();
  loadTypeaheadValues();
}

window.addEventListener('load', init);
