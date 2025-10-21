// More agressive version of the save inputs which will
// persist accross sessions

// Also uses the new storage layout and is toggleable through the settings page

import { getDefaultValuesForPage } from './setup_defaults.mjs';
import {
  getGlobalValues,
  getPageLocalValues,
  setPageLocalValues
} from '/static/js/f_helpers/local_storage_page_helpers.mjs';

let page_name;

function loadStoredValuesIfExist(saveAndRestoreInputIds, pagePreviouslySearchedValues) {
  for (const id of saveAndRestoreInputIds) {
    // Check to see if this id has a previously stored value
    if (pagePreviouslySearchedValues[id]) {
      const inputElement = document.getElementById(id);
      if (inputElement) {
        inputElement.value = pagePreviouslySearchedValues[id];
      }
    }
  }
}

function getPreviouslyStoredValuesForThisPage() {
  // Get the local values for this page
  const pageLocalValues = getPageLocalValues(page_name);

  // Extract the pagePreviouslySearchedValues, default to an empty array if none found
  return pageLocalValues.pagePreviouslySearchedValues || [];
}

function setPreviouslyStoredValuesForThisPage(inputValues) {
  // Set the pagePreviouslySearchedValues to the new inputValues
  setPageLocalValues(page_name, { pagePreviouslySearchedValues: inputValues });
}

function saveValueOfInput(inputId, inputValue) {
  console.log(`Saving value of input ${inputId}: ${inputValue}`);

  // Firstly get the current pages previously stored input values
  const previouslyStoredValues = getPreviouslyStoredValuesForThisPage(page_name);

  // Now create a new object with the inputId and input value
  const valuesToMerge = {[inputId]: inputValue};

  // Now merge with the previously stored values
  const mergedValues = {...previouslyStoredValues, ...valuesToMerge};

  // Now save the new values
  setPreviouslyStoredValuesForThisPage(mergedValues);
}

// Remove markup from inside an element (i.e for the autosuggest suggestions)
function removeMarkupFromInsideElement(element) {
  if (!element) return '';

  const clone = element.cloneNode(true);

  // Replace <strong> with just its text content
  clone.querySelectorAll('strong').forEach(strongEl => {
    const textNode = document.createTextNode(strongEl.textContent);
    strongEl.replaceWith(textNode);
  });

  // Remove all <span>s entirely
  clone.querySelectorAll('span').forEach(spanEl => {
    spanEl.remove();
  });

  // Return the pure text
  return clone.textContent.trim();
}

function addEventListenerToTriggerSaveOnChangeForAutosuggestComponent(inputElement) {
  // Given an input element that's an ONS autosuggest component
  // the event listener must be on the *suggesgions* not the element
  // as the element itself triggers events like input, change, blur before the value is changed
  const completeContainerForClassificationFilter = document.querySelector('#complete-container-for-classificationfilter');

  const classNameForSuggesgionContainer = "ons-autosuggest__results";
  const suggestionContainer = completeContainerForClassificationFilter.querySelector('.' + classNameForSuggesgionContainer);

  if (!suggestionContainer) { 
    console.log('No suggestion container found for autosuggest component');
    return;
  }
  console.log('Suggestion container found:', suggestionContainer);

  suggestionContainer.addEventListener('click', event => {
    const clickedEl = event.target.closest('li');

    if (clickedEl) {
      const textFromAutosuggest= removeMarkupFromInsideElement(clickedEl);

      // Now save this value
      saveValueOfInput(inputElement.id, textFromAutosuggest);
      console.log('Saved value from autosuggest:', textFromAutosuggest);
    } else {
      console.log('Clicked outside of a suggestion <li>');
    }
  });
}

function addEventListenersToTriggerSaveOnChange(saveAndRestoreInputIds) {
  // Loop over all the ids
  for (const id of saveAndRestoreInputIds) {
    const inputElement = document.querySelector('#' + id);

    // If the element not found, skip it
    if (!inputElement) { return; }

    // If it's an autosuggest component, use a different event listener
    if (inputElement.classList.contains('ons-js-autosuggest-input')) {
      // Add an event listener to save from a suggestion - STILL REQUIRES A REGULAR INPUT LISTENER
      addEventListenerToTriggerSaveOnChangeForAutosuggestComponent(inputElement);
    } 
    inputElement.addEventListener('input', () => {
      saveValueOfInput(inputElement.id, inputElement.value);
    });
  }
}

function getPagePreviouslySearchedValues() {
  // Get the local values for this page
  const pageLocalValues = getPageLocalValues(page_name);

  // Inject default values if the pagePreviouslySearchedValues doesn't exist
  const defaultValuesForPage = getDefaultValuesForPage(page_name);
  if (!pageLocalValues.pagePreviouslySearchedValues) {
    // If we have to setup the defaults, then we should also save them to local storage as the "previously searched values"
    pageLocalValues.pagePreviouslySearchedValues = defaultValuesForPage;
    setPreviouslyStoredValuesForThisPage(pageLocalValues.pagePreviouslySearchedValues);
  }

  // Extract the pagePreviouslySearchedValues, default to an empty object if no defaults defined
  return pageLocalValues.pagePreviouslySearchedValues || {};
}

function init() {
  console.log('save_page_inputs loaded');
  page_name = 'radiussearch';

  // Get the object 'save_and_restore_input_ids' from page values - TODO with all page customisation
  // const saveAndRestoreInputIds = globalValues['save_and_restore_input_ids'] || [];

  // Use just ones expected for radius search for now, future updates will allow all pages to do this
  const temporaryInputIds = ['lat', 'lon', 'rangekm', 'input', 'classificationfilter', 'limit'];

  // Now get the page's local values (which actually contain what was last in inputs)
  // {'lat': '51.36935132147893', 'lon':'-2.3361860233264187', 'rangekm': '45'};
  const pagePreviouslySearchedValues = getPagePreviouslySearchedValues(page_name);

  // Load stored values given Ids affected (from global) as a list ['id1','id2']
  // and pagePreviouslySearchedValues (from pageLocalValues) as [{'htmlid':'value'}]
  loadStoredValuesIfExist(temporaryInputIds, pagePreviouslySearchedValues);

  // Now attach event listeners to all the inputs with ids in saveAndRestoreInputIds
  addEventListenersToTriggerSaveOnChange(temporaryInputIds);
}

init();