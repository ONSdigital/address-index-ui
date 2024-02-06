import { 
  updateCustomResponseFormat,
  getFormatPrefferenceCustomResponse,
} from '../local_storage_helpers.mjs';


function addChangeEventListeners(radioText, radioAddObj) {
  radioText.addEventListener('change', (e) => {
    updateCustomResponseFormat('response-type-text');
    makeAppropriateResponseFormatVisible('response-type-text');
  });

  radioAddObj.addEventListener('change', (e) => {
    updateCustomResponseFormat('response-type-object');
    makeAppropriateResponseFormatVisible('response-type-object');
  });
}

function setupRadioStatuses(radioText, radioAddObj) {
  const savedTextStatus = getFormatPrefferenceCustomResponse();
  const radioToSelect = document.querySelector('#' + savedTextStatus);
  radioToSelect.checked = true;
}

function makeAppropriateResponseFormatVisible(responseFormatPrefference) {
  const addressObjectContainer = document.querySelector('#address-object-container');
  const formattedTextContainer = document.querySelector('#formatted-text-container');
  const codeResponseElement = document.querySelector('#code-response-element');

  if (responseFormatPrefference === 'response-type-object') {
    addressObjectContainer.classList.remove('ons-u-hidden');
    formattedTextContainer.classList.add('ons-u-hidden');
  } else {
    // Only show if the response isn't blank 
    if (codeResponseElement.textContent !== '') {
      formattedTextContainer.classList.remove('ons-u-hidden');
      addressObjectContainer.classList.add('ons-u-hidden');
    }
  }
}

function init() {
  const radioText = document.querySelector('#response-type-text');
  const radioAddObj = document.querySelector('#response-type-object');
  
  // Save status to local storage
  addChangeEventListeners(radioText, radioAddObj);

  // Load from local storage
  setupRadioStatuses(radioText, radioAddObj);

  const savedTextStatus = getFormatPrefferenceCustomResponse();
  // Make Appropriate Option Visible
  makeAppropriateResponseFormatVisible(savedTextStatus);
}

window.addEventListener('load', init);




