import { getPagePreviouslySearchedValues,
 setPreviouslyStoredValuesForThisPage } from './set_and_get_data.mjs'

import { addEventListenerToTriggerSaveOnChangeForAutosuggestComponent } from './autosuggest_listeners.mjs';
import { addEventListenerToRegionInputs } from './region/region_listeners.mjs';
import { addListenerForDropdown } from './minimummatch/minimummatch_listeners.mjs';

export function saveValueOfInput(inputId, inputValue, page_name) {
  console.log(`Saving value of input ${inputId}: ${inputValue}`);

  // Firstly get the current pages previously stored input values
  // fallback to default values if none found
  const previouslyStoredValues = getPagePreviouslySearchedValues(page_name);

  // Now create a new object with the inputId and input value
  const valuesToMerge = {[inputId]: inputValue};

  // Now merge with the previously stored values
  const mergedValues = {...previouslyStoredValues, ...valuesToMerge};

  // Now save the new values
  setPreviouslyStoredValuesForThisPage(mergedValues, page_name);
}

export function addEventListenersToTriggerSaveOnChange(saveAndRestoreInputIds, page_name) {
  // Loop over all the ids
  for (const id of saveAndRestoreInputIds) {

    // Handle geo (which has mutliple IDs per input)
    if (id === 'region') {
      addEventListenerToRegionInputs(page_name);
      continue;
    } 

    // Not geo, so handle regular input fields
    const inputElement = document.querySelector('#' + id);
    // If the element not found, skip it
    if (!inputElement) { return; }

    // If it's an autosuggest component, add extra listeners
    if (inputElement.classList.contains('ons-js-autosuggest-input')) {
      // Add event listener to save from a suggestion - STILL REQUIRES A REGULAR INPUT LISTENER
      addEventListenerToTriggerSaveOnChangeForAutosuggestComponent(inputElement, page_name);
    } 

    // Handle 'select' dropdowns
    console.log('id is', id);
    if (id === 'minimummatch') {
      console.log('Adding dropdown listener for minimummatch');
      addListenerForDropdown(inputElement, page_name);
    }

    // Handle regular text 'input's
    inputElement.addEventListener('input', () => {
      saveValueOfInput(inputElement.id, inputElement.value, page_name);
    });


  }
}