import { restoreToDefaultEpochOption } from './epoch_specific.mjs';
import { checkRadioButtonByElement } from '/static/js/d_misc_functionality/page_settings/element_manipulation.mjs';

export function restoreRadioValuesIfExist(page_name, inputObject, pagePreviouslySearchedValues) {
  // Find the previously saved value for this radio input
  const htmlId = inputObject.htmlId;
  const savedValue = pagePreviouslySearchedValues[htmlId];

  if (!savedValue) {
    console.debug('No previously saved value for radio input with Id:', htmlId);
    return;
  }
 
  // Get the container element for this radio input
  const containerId = 'complete-container-for-' + htmlId;
  const containerElement = document.querySelector('#' + containerId);

  if (!containerElement) {
    console.warn('No container element found for radio container Id:', containerId);
    return;
  }

  // Now get a list of all radio input elements inside container
  const radioInputs = containerElement.querySelectorAll('input[type="radio"]');

  if (radioInputs.length === 0) {
    console.warn('No radio inputs found inside container for Id:', containerId);
    return;
  }

  // Now loop through the radio inputs to find the one that matches the saved value
  for (const radioInput of radioInputs) {
    if (radioInput.value === savedValue) {
      // Match found, check this radio
      console.debug(`Restored radio input ${htmlId} to value: ${savedValue}`);
      checkRadioButtonByElement(radioInput);
      return;
    } 
  }

  // There was no matching radio found
  console.warn(`No matching radio input found for saved value: ${savedValue} in radio group with Id: ${htmlId}`);

  // If this is an epoch radio, restore to default epoch option
  if (htmlId === 'epoch') {
    restoreToDefaultEpochOption(radioInputs);
  }
}