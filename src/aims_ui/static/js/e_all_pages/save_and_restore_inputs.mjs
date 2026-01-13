// Persistnace is per page, each togglable on the settings page

import { getPageInputObjects, getPagePreviouslySearchedValues } from './save_and_restore_input_helpers/set_and_get_data.mjs';

// Checkbox save and restore
import { addCheckboxListenersToMultipleCheckboxes } from './save_and_restore_input_helpers/checkbox/checkbox_listeners.mjs';
import { restoreCheckboxValuesIfExist } from './save_and_restore_input_helpers/checkbox/checkbox_restorers.mjs';

// Input save and restore
import { addInputListenersToSaveOnChange } from './save_and_restore_input_helpers/input/input_listeners.mjs';
import { restoreValuesToTextInput } from './save_and_restore_input_helpers/input/input_restorers.mjs';

// Autosuggest save and restore
import { restoreValuesToAutosuggestInput } from './save_and_restore_input_helpers/autosuggest/autosuggest_restorers.mjs';
import { addAutosuggestListenersToSaveOnChange } from './save_and_restore_input_helpers/autosuggest/autosuggest_listeners.mjs';

// Radio save and restore
import { addRadioListenersToMultipleRadios } from './save_and_restore_input_helpers/radio/radio_listeners.mjs';
import { restoreRadioValuesIfExist } from './save_and_restore_input_helpers/radio/radio_restorers.mjs';

// Dropdown save and restore
import { addDropdownListenersToSaveOnChange, } from './save_and_restore_input_helpers/dropdown/dropdown_listeners.mjs';
import { restoreDropdownValuesIfExist } from './save_and_restore_input_helpers/dropdown/dropdown_restorers.mjs';

// Function that handles all restoring of values
function restoreValuesToInputsIfExist(page_name, inputObjects, pagePreviouslySearchedValues) {

  for (const inputObject of inputObjects) {
    // Setup all three variables
    const { htmlId, persistanceState, typeOfInput} = inputObject;

    // If persistance is off, skip it
    if (!persistanceState) { continue; }

    // Direct to correct restored, based on type of input
    if (typeOfInput === 'checkboxes') {
      // For multiple checkboxes in one object
      restoreCheckboxValuesIfExist(page_name, inputObject, pagePreviouslySearchedValues);
      continue;
    }

    if (typeOfInput === 'radio') {
      // For radio inputs
      restoreRadioValuesIfExist(page_name, inputObject, pagePreviouslySearchedValues);
      continue;
    }

    if (typeOfInput === 'text') {
      // For text inputs
      restoreValuesToTextInput(page_name, htmlId, pagePreviouslySearchedValues);
      continue;
    }

    if (typeOfInput === 'autosuggest') {
      // For Autosuggest inputs
      restoreValuesToAutosuggestInput(page_name, htmlId, pagePreviouslySearchedValues);
      continue;
    }

    if (typeOfInput === 'dropdown') {
      // For Dropdown inputs
      restoreDropdownValuesIfExist(page_name, htmlId, pagePreviouslySearchedValues);
      continue;
    }

  }

}

function addEventListenersToTriggerSaveOnChange(inputObjects, page_name) {
  // Given a list of input objects, add event listeners based on input type and persitance state

  for (const inputObject of inputObjects) {
    const { htmlId, persistanceState, typeOfInput} = inputObject;

    // If persistance is off, skip this input
    if (!persistanceState) { 
      console.log(`Skipping input ${htmlId} as persistance is off`);
      continue;
    }

    // Now add the event listener based on type of input

    // Add 'multiple' 'input' listeners (for a single input with multiple elements, like checkboxes or radios)
    if (typeOfInput === 'checkboxes') {
      // For multiple checkboxes in one object
      addCheckboxListenersToMultipleCheckboxes(page_name, inputObject);
      continue;
    }

    if (typeOfInput === 'radio') {
      // For radio inputs
      addRadioListenersToMultipleRadios(page_name, inputObject);
      continue;
    }

    // Add listeners to individual inputs on a page
    if (typeOfInput === 'text') {
      // Handle regular text inputs (and numerical ones!)
      addInputListenersToSaveOnChange(page_name, htmlId);
      continue;
    }

    if (typeOfInput === 'autosuggest') {
      // For Autosuggest inputs
      addAutosuggestListenersToSaveOnChange(page_name, htmlId);
      continue;
    }

    if (typeOfInput === 'dropdown') {
      // For Dropdown inputs
      addDropdownListenersToSaveOnChange(page_name, htmlId);
      continue;
    }
  }

  return;

}

export function init(page_name) {
  console.log('save_and_restore_inputs loaded');

  // Get the objects for each input - containing a "toPersist" and "htmlId"
  const inputObjects = getPageInputObjects(page_name);
  console.log('Input objects', page_name, ':', inputObjects);

  // Now get the page's local values (which actually contain what was last in inputs)
  // {'lat': '51.36935132147893', 'lon':'-2.3361860233264187', 'rangekm': '45'};
  const pagePreviouslySearchedValues = getPagePreviouslySearchedValues(page_name);
  restoreValuesToInputsIfExist(page_name, inputObjects, pagePreviouslySearchedValues);

  // Now attach event listeners to all the inputs that are set to persist
  addEventListenersToTriggerSaveOnChange(inputObjects, page_name);
}
