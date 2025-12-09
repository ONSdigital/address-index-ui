// More agressive version of the save inputs which will
// persist accross sessions

// Also uses the new storage layout and is toggleable through the settings page

import { getDefaultValuesForPage } from './setup_defaults.mjs';
import {
  getGlobalValues,
  getPageLocalValues,
  setPageLocalValues
} from '/static/js/f_helpers/local_storage_page_helpers.mjs';

function loadStoredValuesIfExist(saveAndRestoreInputIds, pagePreviouslySearchedValues) {
  for (const id of saveAndRestoreInputIds) {
    // Check to see if this id has a previously stored value
    if (pagePreviouslySearchedValues[id]) {
      const inputElement = document.querySelector('#' + id);
      if (inputElement) {
        inputElement.value = pagePreviouslySearchedValues[id];
      }
    }
  }
}

function getPreviouslyStoredValuesForThisPage(page_name) {
  // Get the local values for this page
  const pageLocalValues = getPageLocalValues(page_name);

  // Extract the pagePreviouslySearchedValues, default to an empty object if none found
  return pageLocalValues.pagePreviouslySearchedValues || {};
}

function setPreviouslyStoredValuesForThisPage(inputValues, page_name) {
  // Set the pagePreviouslySearchedValues to the new inputValues
  setPageLocalValues(page_name, { pagePreviouslySearchedValues: inputValues });
}

function saveValueOfInput(inputId, inputValue, page_name) {
  console.log(`Saving value of input ${inputId}: ${inputValue}`);

  // Firstly get the current pages previously stored input values
  const previouslyStoredValues = getPreviouslyStoredValuesForThisPage(page_name);

  // Now create a new object with the inputId and input value
  const valuesToMerge = {[inputId]: inputValue};

  // Now merge with the previously stored values
  const mergedValues = {...previouslyStoredValues, ...valuesToMerge};

  // Now save the new values
  setPreviouslyStoredValuesForThisPage(mergedValues, page_name);
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

function addEventListenerToTriggerSaveOnChangeForAutosuggestComponent(inputElement, page_name) {
  // Given an input element that's an ONS autosuggest component
  // the event listener must be on the *Suggestions* not the element
  // as the element itself triggers events like input, change, blur before the value is changed
  const completeContainerForClassificationFilter = document.querySelector('#complete-container-for-classificationfilter');

  const classNameForSuggestionContainer = "ons-autosuggest__results";
  const suggestionContainer = completeContainerForClassificationFilter.querySelector('.' + classNameForSuggestionContainer);

  if (!suggestionContainer) { 
    console.log('No suggestion container found for autosuggest component');
    return;
  }

  suggestionContainer.addEventListener('click', event => {
    const clickedEl = event.target.closest('li');

    if (clickedEl) {
      const textFromAutosuggest = removeMarkupFromInsideElement(clickedEl);

      // Now save this value
      saveValueOfInput(inputElement.id, textFromAutosuggest, page_name);
      console.log('Saved value from autosuggest:', textFromAutosuggest);
    } else {
      console.log('Clicked outside of a suggestion <li>');
    }
  });

  // Add an event listener for keyboard selection (Enter key)
  completeContainerForClassificationFilter.addEventListener('keydown', event => {
    if (event.key === 'Enter') {
      // The suggestion that is currently focused will have ons-autosuggest__option--focused
      const focusedSuggestion = suggestionContainer.querySelector('.ons-autosuggest__option--focused');
      if (focusedSuggestion) {
        const textFromAutosuggest = removeMarkupFromInsideElement(focusedSuggestion);

        // Now save this value
        saveValueOfInput(inputElement.id, textFromAutosuggest, page_name);
        console.log('Saved value from autosuggest (keyboard):', textFromAutosuggest);
      }
    }
  });
}

function addEventListenersToTriggerSaveOnChange(saveAndRestoreInputIds, page_name) {
  // Loop over all the ids
  for (const id of saveAndRestoreInputIds) {
    const inputElement = document.querySelector('#' + id);

    // If the element not found, skip it
    if (!inputElement) { return; }

    // If it's an autosuggest component, use a different event listener
    if (inputElement.classList.contains('ons-js-autosuggest-input')) {
      // Add an event listener to save from a suggestion - STILL REQUIRES A REGULAR INPUT LISTENER
      addEventListenerToTriggerSaveOnChangeForAutosuggestComponent(inputElement, page_name);
    } 
    inputElement.addEventListener('input', () => {
      saveValueOfInput(inputElement.id, inputElement.value, page_name);
    });
  }
}

function getPagePreviouslySearchedValues(page_name) {
  // Get the local values for this page
  const pageLocalValues = getPageLocalValues(page_name);

  // Inject default values if the pagePreviouslySearchedValues doesn't exist
  const defaultValuesForPage = getDefaultValuesForPage(page_name);
  if (!pageLocalValues.pagePreviouslySearchedValues) {
    // If we have to setup the defaults, then we should also save them to local storage as the "previously searched values"
    pageLocalValues.pagePreviouslySearchedValues = defaultValuesForPage;
    setPreviouslyStoredValuesForThisPage(pageLocalValues.pagePreviouslySearchedValues, page_name);
  }

  // Extract the pagePreviouslySearchedValues, default to an empty object if no defaults defined
  return pageLocalValues.pagePreviouslySearchedValues || {};
}

function getPersistanceSettingsOfPage(page_name) {
  // Will return an array of input Ids, setup in global storage
  const globalValues = getGlobalValues();
  // An array of objects like [ {'page_name':'radiussearch', {object of settings}
  const persistanceSettings = globalValues['persistanceSettings'] || [];

  // Find the object for this page
  for (const pageSetting of persistanceSettings) {
    if (pageSetting.page === page_name) {
      return pageSetting;
    }
  }

  // If not found, log an error
  console.error('No persistance settings found for page:', page_name);
}

function getIdsOfInputsToPersist(page_name) {
  // Get the persistance settings for this page
  const pagePersistanceSettings = getPersistanceSettingsOfPage(page_name);
  const inputPersistanceSettings = pagePersistanceSettings.input_persistance_settings || {};
  
  // Now extract the Ids of inputs that should be persisted {'inputId': true/false}
  const idsToPersist = [];
  for (const [inputId, shouldPersist] of Object.entries(inputPersistanceSettings)) {
    if (shouldPersist) {
      idsToPersist.push(inputId);
    }
  }

  return idsToPersist;
}

export function init(page_name) {
  console.log('save_page_inputs loaded');

  // Get the object 'save_and_restore_input_ids' from page values - TODO with all page customisation
  // const saveAndRestoreInputIds = globalValues['save_and_restore_input_ids'] || [];

  // Use just ones expected for radius search for now, future updates will allow all pages to do this
  console.log('Page name for save and restore inputs:', page_name);
  const inputIds = getIdsOfInputsToPersist(page_name);

  // Now get the page's local values (which actually contain what was last in inputs)
  // {'lat': '51.36935132147893', 'lon':'-2.3361860233264187', 'rangekm': '45'};
  const pagePreviouslySearchedValues = getPagePreviouslySearchedValues(page_name);

  // Load stored values given Ids affected (from global) as a list ['id1','id2']
  // and pagePreviouslySearchedValues (from pageLocalValues) as [{'htmlid':'value'}]
  loadStoredValuesIfExist(inputIds, pagePreviouslySearchedValues);

  // Now attach event listeners to all the inputs with ids in saveAndRestoreInputIds
  addEventListenersToTriggerSaveOnChange(inputIds, page_name);
}
