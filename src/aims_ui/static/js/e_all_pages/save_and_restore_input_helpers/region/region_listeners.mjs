// Helpers for saving the value of an autosuggest - more duifficult than a regular input,
// as it needs to save on click, enter selection, change etc

import { saveValueOfInput } from '../save_input_listeners.mjs';
import { returnCurrentPageMap, getFullIdsOfEachRegionContainer } from './region_helpers.mjs';

function addCheckboxListenersToEachcheckbox(regionContainerIds, page_name) {
  for (const containerId of regionContainerIds) {
    const containerElement = document.querySelector('#' + containerId);
    if (!containerElement) {
      console.warn('No container element found for region container Id:', containerId);
      continue;
    }

    // Find the checkbox input inside this container
    const checkboxInput = containerElement.querySelector('input[type="checkbox"]');
    if (!checkboxInput) {
      console.warn('No checkbox input found inside container:', containerId);
      continue;
    }

    // Add event listener to save on change
    checkboxInput.addEventListener('change', () => {
      const isChecked = checkboxInput.checked;
      saveValueOfInput(checkboxInput.id, isChecked, page_name);
    });
  }

}

function addInputListenersToEachInput(regionContainerIds, page_name) {
  // Called when the region inputs are text inputs rather than checkboxes

  for (const containerId of regionContainerIds) {
    const containerElement = document.querySelector('#' + containerId);
    if (!containerElement) {
      console.warn('No container element found for region container Id:', containerId);
      continue;
    }
    
    // Find the text input inside this container
    const textInput = containerElement.querySelector('input[type="text"]');
    if (!textInput) {
      console.warn('No text input found inside container:', containerId);
      continue;
    } 

    // Add event listener to save on input
    textInput.addEventListener('input', () => {
      const inputValue = textInput.value;
      saveValueOfInput(textInput.id, inputValue, page_name);
    });
  }
}

export function addEventListenerToRegionInputs(page_name) {
  // Called to find and add listeners to Geo checkboxes/boosts depending on page

  // Get the info on the current region inputs
  const currentPageMap = returnCurrentPageMap(page_name);

  // Get the ids of each container for the input to add a listener to
  const regionContainerIds = getFullIdsOfEachRegionContainer(currentPageMap);

  // If the regions are checkboxes then run the checkbox listeners function
  if (currentPageMap.region_type === 'checkboxes') {
    addCheckboxListenersToEachcheckbox(regionContainerIds, page_name);
    return;
  }

  if (currentPageMap.region_type === 'inputs') {
    addInputListenersToEachInput(regionContainerIds, page_name);
    return;
  }

  console.warn('Unknown region type or missing config:', currentPageMap.region_type);
}
