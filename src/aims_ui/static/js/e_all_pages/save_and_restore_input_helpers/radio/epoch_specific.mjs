import { getGlobalValues } from '../../../f_helpers/local_storage_page_helpers.mjs';
import { checkRadioButtonByElement } from '/static/js/d_misc_functionality/page_settings/element_manipulation.mjs';

export function restoreToDefaultEpochOption(radioInputs) {
  // Check if the Radio is an epoch type, if it is then it should default to 
  // globally stored "latestEpochNumber" - which is always saved on epoch component render

  const globalValues = getGlobalValues();
  const latestEpochNumber = globalValues['latestEpochNumber'];

  if (!latestEpochNumber) {
    console.warn('No globally stored latestEpochNumber found to set epoch radio to.');
    return;
  }

  // Now loop through the radio inputs to find the one that matches the latestEpochNumber
  for (const radioInput of radioInputs) {
    if (radioInput.value === latestEpochNumber) {
      // Match found, check this radio
      console.debug(`No saved epoch found, defaulting to latestEpochNumber: ${latestEpochNumber}`);
      checkRadioButtonByElement(radioInput);
      return;
    }
  }

  console.warn(`No matching radio input found for latestEpochNumber: ${latestEpochNumber} in epoch radio group.`);
}