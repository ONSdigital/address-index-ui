import { 
  updateCustomResponseFormat,
  updateCustomResponseRequestType,
  getFormatPrefferenceCustomResponse,
  getRequestTypeCustomResponse,
  updateReqBodyStyle,
  getReqBodyStyle,
} from '../local_storage_helpers.mjs';


function addChangeEventListeners(radioText, radioAddObj, reqType, reqBody) {
  // Radio Listeners
  radioText.addEventListener('change', (e) => {
    updateCustomResponseFormat('response-type-text');
    makeAppropriateResponseFormatVisible('response-type-text');
  });
  radioAddObj.addEventListener('change', (e) => {
    updateCustomResponseFormat('response-type-object');
    makeAppropriateResponseFormatVisible('response-type-object');
  });

  // Dropdown (POST/GET) listeners
 reqType.addEventListener('change', (e) => {
    const requestType = e.target.value;
    updateCustomResponseRequestType(requestType);
  });

  // Save the size of the body element
  const callback = function(mutationsList, observer) {
    for(let mutation of mutationsList) {
      if (mutation.type === 'attributes' && mutation.attributeName === 'style') {
        const newStyle = reqBody.getAttribute('style');
        updateReqBodyStyle(newStyle);
      }
    }
  };

  const observer = new MutationObserver(callback); 
  const config = { attributes: true, attributeFilter: ['style'] };
  observer.observe(reqBody, config);
}

function setupStatuses(radioText, radioAddObj, reqType, reqBody) {
  // Set status of radio option
  const savedTextStatus = getFormatPrefferenceCustomResponse();
  const radioToSelect = document.querySelector('#' + savedTextStatus);
  radioToSelect.checked = true;

  // Set dropdown selected
  reqType.value = getRequestTypeCustomResponse();

  // Set style of reqBody
  const bodStyle = getReqBodyStyle();
  reqBody.setAttribute('style', bodStyle);
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
  const reqType = document.querySelector('#request-type');
  const reqBody = document.querySelector('#request-body-text-area');
  
  // Save status to local storage
  addChangeEventListeners(radioText, radioAddObj, reqType, reqBody);

  // Load from local storage
  setupStatuses(radioText, radioAddObj, reqType, reqBody);

  const savedTextStatus = getFormatPrefferenceCustomResponse();
  // Make Appropriate Option Visible
  makeAppropriateResponseFormatVisible(savedTextStatus);
}

window.addEventListener('load', init);




