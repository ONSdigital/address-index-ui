import { crEl } from "/static/js/f_helpers/element_creation.mjs";

function removeBrElements(container) {
  const brElements = container.querySelectorAll('br');
  brElements.forEach(br => {
    br.remove();
  });
  return container;
}

// Given the generated buttons, extract them, add them to a new element that's spaced evenly,
// then return that container 
function returnGroupedButtons(inputContainer) {
  // Get all the buttons ('search' and 'clear')
  const buttons = inputContainer.querySelectorAll('.ons-btn');

  // Group buttons
  const newButtonContainer = crEl('div', 'grouped-button-container');
  buttons.forEach(button => {
    newButtonContainer.appendChild(button);
  });
  return newButtonContainer;
}

function createUprnResponseContent() {
  const uprnTitle = crEl('h3', 'uprn-lookup-results-title');
  uprnTitle.textContent = 'No UPRN lookup performed yet'; 
  const uprnInfoLn1 = crEl('h4', 'uprn-lookup-results-info-ln1');
  const uprnInfoLn2 = crEl('h4', 'uprn-lookup-results-info-ln2');
  const uprnResponseContainer = crEl('div', 'uprn-lookup-results-container');
  uprnResponseContainer.append(uprnTitle, uprnInfoLn1, uprnInfoLn2);

  return uprnResponseContainer;
}

function getUprnSearchAndUprnResultsContainer(inputContainer) {
  const uprnContainer = inputContainer.querySelector('#complete-container-for-uprn');
  const uprnResultsContainer = inputContainer.querySelector('#complete-container-for-uprnLookupPanel');
  // Get the inside of the info panel
  const insideResultsContainer = uprnResultsContainer.querySelector('.ons-panel__body');

  // Add content to the results container
  const uprnResultsContent = createUprnResponseContent();
  insideResultsContainer.append(uprnResultsContent);

  const uprnSearchAndResultsContainer = crEl('div', 'uprn-search-and-results-container', ['left-right-fifty-fifty']);
  uprnSearchAndResultsContainer.append(uprnContainer, uprnResultsContainer);

  return uprnSearchAndResultsContainer;
}

// Get the containers for UPRN and Long/Lat - organised to provide user with an option to use either
function getLatLongContainer(inputerContainer) {
  // Get the lat/long container
  const latContainer = inputerContainer.querySelector('#complete-container-for-lat');
  const lonContainer = inputerContainer.querySelector('#complete-container-for-lon');

  // Create a new container 50/50 left right
  const latLonContainer = crEl('div', 'lat-long-container', ['left-right-fifty-fifty']);
  latLonContainer.append(latContainer, lonContainer);
  return latLonContainer;
}

function getLatLonUprnContainer(inputContainer) {
  const uprnResultsAndSearchContainer = getUprnSearchAndUprnResultsContainer(inputContainer);
  const latLonContainer = getLatLongContainer(inputContainer);

  // Create a new container 50/50 UP DOWN
  const latLonUprnContainer= crEl('div', 'lat-lon-uprn-container', ['up-down-fifty-fifty']);
  latLonUprnContainer.append(latLonContainer, uprnResultsAndSearchContainer);

  return latLonUprnContainer;
}

function getRangeClassificationContainer(inputContainer) {
  const rangeContainer = inputContainer.querySelector('#complete-container-for-rangekm');
  const classificationContainer = inputContainer.querySelector('#complete-container-for-classificationfilter');

  // Create a new container 50/50 left right
  const rangeClassificationContainer = crEl('div', 'range-classification-container', ['left-right-fifty-fifty']);
  rangeClassificationContainer.append(rangeContainer, classificationContainer);
  return rangeClassificationContainer;
}

function getSearchAndLimitContainer(inputContainer) {
  const searchStringContainer = inputContainer.querySelector('#complete-container-for-input');
  const limitContainer = inputContainer.querySelector('#complete-container-for-limit');

  // Create a new container 50/50 left right
  const searchAndLimitContainer = crEl('div', 'search-and-limit-container', ['left-right-fifty-fifty']);
  searchAndLimitContainer.append(searchStringContainer, limitContainer);
  return searchAndLimitContainer;
}

// Get the layout for the range, classification, search string and limit inputs
function getSearchInputsContainer(inputContainer) {
  const rangeClassificationContainer = getRangeClassificationContainer(inputContainer);
  const searchAndLimitContainer = getSearchAndLimitContainer(inputContainer);

  // Create a new container 50/50 UP DOWN
  const searchInputsContainer = crEl('div', 'range-classification-input-limit-container', ['up-down-fifty-fifty']);
  searchInputsContainer.append(rangeClassificationContainer, searchAndLimitContainer);
  return searchInputsContainer;
}

function getFullInputContainer(inputContainer) {
  const latLonUprnContainer = getLatLonUprnContainer(inputContainer);
  const searchInputsContainer = getSearchInputsContainer(inputContainer);

  // Create a new container 50/50 left right
  const fullInputContainer = crEl('div', 'full-input-container', ['left-right-fifty-fifty']);
  fullInputContainer.append(latLonUprnContainer, searchInputsContainer);
  return fullInputContainer;
}

export function setupHorizontalInputs() {
  // The input container is where the inputs and buttons are currently
  // and also where they need to be returned to
  const inputContainer = document.querySelector('.match-form-container');
  removeBrElements(inputContainer);

  // Get the full inputs broken up into flexbox containers
  const fullInputContainer = getFullInputContainer(inputContainer);

  // Get the buttons in a container
  const newButtonContainer = returnGroupedButtons(inputContainer);

  // Add the inputs and the search buttons
  inputContainer.append(fullInputContainer, newButtonContainer);

  // Finally, remove the "invisible" class from the full-match-form-container
  const fullMatchFormContainer = document.querySelector('#full-match-form-container');
  fullMatchFormContainer.classList.remove('invisible');
}
