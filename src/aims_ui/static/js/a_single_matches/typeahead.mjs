
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
  const valuesToSave = [];
  for (const input of inputs) {
    const valueKeyPair = {};
    valueKeyPair[input.getAttribute('id')] = input.value;
    valuesToSave.push(valueKeyPair);
  }
  localStorage.setItem('typeaheadParams', JSON.stringify(valuesToSave));
}

function loadTypeaheadValues() {
  const typeaheadParams = JSON.parse(localStorage.getItem('typeaheadParams'));
  if (typeaheadParams) {
    const inputs = getAllInputs();
    for (const input of inputs) {
      for (const param of typeaheadParams) {
        if (input.getAttribute('id') in param) {
          input.value = param[input.getAttribute('id')];
        }
      }
    }
  }
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

function init() {
  console.log('typeahead specific loaded');
  setupEventListeners();
  loadTypeaheadValues();
}

window.addEventListener('load', init);
