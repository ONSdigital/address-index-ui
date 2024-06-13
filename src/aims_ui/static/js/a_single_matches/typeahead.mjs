// Script to adjust the parameters for typeahead whenever they're updated
export function getParamsFromPage() {
  let finalParams = '&';
  const lfForm = document.querySelector('.match-form-container');
  const inputs = lfForm.querySelectorAll('input');
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

export function setupEventListeners() {
  const typeaheadContainer = document.querySelector(
    '#address-autosuggest-container'
  );
  typeaheadContainer.setAttribute('data-query-params', getParamsFromPage());

  // Every time the typeahead is focussed on, refresh the parameters
  typeaheadContainer.addEventListener('focusin', () => {
    typeaheadContainer.setAttribute('data-query-params', getParamsFromPage());
  });
}

function init() {
  console.log('typeahead specific loaded');
  setupEventListeners();
}

window.addEventListener('load', init);
