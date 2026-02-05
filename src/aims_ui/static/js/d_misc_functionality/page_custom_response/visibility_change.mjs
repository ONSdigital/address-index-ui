import { getPostBodyTextBoxStyleFromLocalStorage } from "./local_storage.mjs";

export function makePostTextBodyVisible() {
  const reqBodyContainer = document.querySelector('#text-area-label-and-input-container');
  reqBodyContainer.classList.remove('ons-u-hidden');
}

export function makePostTextBodyHidden() {
  const reqBodyContainer = document.querySelector('#text-area-label-and-input-container');
  reqBodyContainer.classList.add('ons-u-hidden');
}

export function setGetPostTextboxVisibilityBasedOnDropdown(selectHtmlObject) {
  // Set visibility of ReqBodyConatiner (hide if GET)
  if (selectHtmlObject.value === 'GET') {
    makePostTextBodyHidden();
  } else if (selectHtmlObject.value === 'POST') {
    makePostTextBodyVisible();
  }
}

function getTextObjectErrorContainers() {
  const addressObjectContainer = document.querySelector('#address-object-container');
  const formattedTextContainer = document.querySelector('#formatted-text-container');
  const errorCodeVisualContainer = document.querySelector('#error-response-container');

  return {
    addressObjectContainer,
    formattedTextContainer,
    errorCodeVisualContainer
  };
}

function removeHiddenClass(element) {
  element.classList.remove('ons-u-hidden');
}

function addHiddenClass(element) {
  element.classList.add('ons-u-hidden');
}

export function showResponseAsText() {
  // Show the formatted-text-container, hide address object and code response
  const { addressObjectContainer, formattedTextContainer, errorCodeVisualContainer } = getTextObjectErrorContainers();
  removeHiddenClass(formattedTextContainer);
  addHiddenClass(addressObjectContainer);
  addHiddenClass(errorCodeVisualContainer);
}

export function showResponseAsObject() {
  // Show the address-object-container and error code (formatted), hide formatted text 
  const { addressObjectContainer, formattedTextContainer, errorCodeVisualContainer } = getTextObjectErrorContainers();

  // Check if there is an error inside the code
  const childrenOfErrorContainer = errorCodeVisualContainer.children;

  if (childrenOfErrorContainer.length > 0) {
    // There is an error, so show that without the address object 
    removeHiddenClass(errorCodeVisualContainer);
    addHiddenClass(addressObjectContainer);
    addHiddenClass(formattedTextContainer);
    return;
  } else {
    // No error, show the address object, hide the error container and text container
    removeHiddenClass(addressObjectContainer);
    addHiddenClass(errorCodeVisualContainer);
    addHiddenClass(formattedTextContainer);
  }
}

export function setTextObjectBasedOnRadioButtons() {
  const radioText = document.querySelector('#response-type-text');
  const radioObj = document.querySelector('#response-type-object');

  if (radioText.checked) {
    showResponseAsText();
  } else if (radioObj.checked) {
    showResponseAsObject();
  }
}

export function setSizeOfPostBodyTextBoxFromLocalStorage() {
  const postBodyTextArea = document.querySelector('#post-body-text-area');
  const savedStyle = getPostBodyTextBoxStyleFromLocalStorage();
  if (savedStyle) {
    postBodyTextArea.setAttribute('style', savedStyle);
  }
}

