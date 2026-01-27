import {
  getFormatPreferenceCustomResponse,
  getRequestTypeCustomResponse,
  updateReqBodyStyle,
  getReqBodyStyle,
} from '/static/js/f_helpers/local_storage_helpers.mjs';

function addChangeEventListeners(
  radioText,
  radioAddObj,
  reqType,
  reqBody,
  reqBodyContainer
) {
  // Radio Listeners
  radioText.addEventListener('change', () => {
    makeAppropriateResponseFormatVisible('response-type-text');
  });
  radioAddObj.addEventListener('change', () => {
    makeAppropriateResponseFormatVisible('response-type-object');
  });

  // Dropdown (POST/GET) listeners
  reqType.addEventListener('change', (e) => {
    // show/hide the body input (only required for POSTing)
    if (e.target.value === 'POST') {
      reqBodyContainer.classList.remove('ons-u-hidden');
    } else if (e.target.value === 'GET') {
      reqBodyContainer.classList.add('ons-u-hidden');
    }
  });

  // Save the size of the body element
  const callback = function (mutationsList, observer) {
    for (let mutation of mutationsList) {
      if (
        mutation.type === 'attributes' &&
        mutation.attributeName === 'style'
      ) {
        const newStyle = reqBody.getAttribute('style');
        updateReqBodyStyle(newStyle);
      }
    }
  };

  const observer = new MutationObserver(callback);
  const config = { attributes: true, attributeFilter: ['style'] };
  observer.observe(reqBody, config);
}

function setupStatuses(
  radioText,
  radioAddObj,
  reqType,
  reqBody,
  reqBodyConatiner
) {
  // Set style of reqBody
  const bodStyle = getReqBodyStyle();
  reqBody.setAttribute('style', bodStyle);

  // Set visibility of ReqBodyConatiner (hide if GET)
  if (reqType.value === 'GET') {
    reqBodyConatiner.classList.add('ons-u-hidden');
  } else if (reqType.value === 'POST') {
    reqBodyConatiner.classList.remove('ons-u-hidden');
  }
}

function makeAppropriateResponseFormatVisible(responseFormatPreference) {
  const addressObjectContainer = document.querySelector(
    '#address-object-container'
  );
  const formattedTextContainer = document.querySelector(
    '#formatted-text-container'
  );
  const codeResponseElement = document.querySelector('#code-response-element');

  if (responseFormatPreference === 'response-type-object') {
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
  const reqBodyContainer = document.querySelector(
    '#text-area-label-and-input-container'
  );

  const savedTextStatus = getFormatPreferenceCustomResponse();

  // Make Appropriate Option Visible
  makeAppropriateResponseFormatVisible(savedTextStatus);
}

window.addEventListener('load', init);
