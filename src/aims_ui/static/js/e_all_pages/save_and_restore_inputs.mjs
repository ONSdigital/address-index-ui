// More agressive version of the save inputs which will
// persist accross sessions

// Also uses the new storage layout and is toggleable through the settings page

import { getIdsOfInputsToPersist, getPagePreviouslySearchedValues } from './save_and_restore_input_helpers/set_and_get_data.mjs';
import { addEventListenersToTriggerSaveOnChange } from './save_and_restore_input_helpers/save_input_listeners.mjs';

function restoreValuesToInputsifExist(saveAndRestoreInputIds, pagePreviouslySearchedValues) {
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

export function init(page_name) {
  console.log('save_page_inputs loaded');

  // Get the Ids of inputs to persist for this page
  const inputIds = getIdsOfInputsToPersist(page_name);

  // Now get the page's local values (which actually contain what was last in inputs)
  // {'lat': '51.36935132147893', 'lon':'-2.3361860233264187', 'rangekm': '45'};
  const pagePreviouslySearchedValues = getPagePreviouslySearchedValues(page_name);

  // Load stored values given Ids affected (from global) as a list ['id1','id2']
  // and pagePreviouslySearchedValues (from pageLocalValues) as [{'htmlid':'value'}]
  restoreValuesToInputsifExist(inputIds, pagePreviouslySearchedValues);

  // Now attach event listeners to all the inputs with ids in saveAndRestoreInputIds
  addEventListenersToTriggerSaveOnChange(inputIds, page_name);
}
