// More agressive version of the save inputs which will
// persist accross sessions

// Also uses the new storage layout and is toggleable through the settings page

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
        inputElement.dispatchEvent(new Event('change', { bubbles: true }));
        inputElement.dispatchEvent(new Event('input', { bubbles: true }));
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
  // Firstly get the current pages previously stored input values
  const previouslyStoredValues = getPreviouslyStoredValuesForThisPage(page_name);

  // Now create a new object with the inputId and input value
  const valuesToMerge = {[inputId]: inputValue};

  // Now merge with the previously stored values
  const mergedValues = {...previouslyStoredValues, ...valuesToMerge};

  // Now save the new values
  setPreviouslyStoredValuesForThisPage(mergedValues);
}

function addEventListenersToTriggerSaveOnChange(saveAndRestoreInputIds) {
  // Loop over all the ids
  for (const id of saveAndRestoreInputIds) {
    const inputElement = document.querySelector('#' + id);
    // If the element is actually found on this page 
    if (inputElement) {
      inputElement.addEventListener('input', () => {
        saveValueOfInput(inputElement.id, inputElement.value);
      });
    }
  }
}

function getPagePreviouslySearchedValues() {
  // Get the local values for this page
  const pageLocalValues = getPageLocalValues(page_name);

  // Extract the pagePreviouslySearchedValues, default to an empty object if none found
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
  const pagePreviouslySearchedValues = getPagePreviouslySearchedValues();

  // Load stored values given Ids affected (from global) as a list ['id1','id2']
  // and pagePreviouslySearchedValues (from pageLocalValues) as [{'htmlid':'value'}]
  loadStoredValuesIfExist(temporaryInputIds, pagePreviouslySearchedValues);

  // Now attach event listeners to all the inputs with ids in saveAndRestoreInputIds
  addEventListenersToTriggerSaveOnChange(temporaryInputIds);
}
window.addEventListener('load', init);
