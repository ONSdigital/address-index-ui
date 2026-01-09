
import { uncheckCheckbox, checkCheckbox } from '/static/js/d_misc_functionality/page_settings/element_manipulation.mjs';

export function restoreCheckboxValuesIfExist(page_name, inputObject, pagePreviouslySearchedValues) {
  // Given an object containing multiple checkboxes, restore their values
  const checkboxIds = inputObject.checkboxHtmlIds || [];
  
  for (const checkboxId of checkboxIds) {

    // Get checkbox element 
    const checkboxElement = document.querySelector('#' + checkboxId);
    if (!checkboxElement) {
      console.warn('No checkbox element found for checkbox Id:', checkboxId);
      continue;
    }

    // Get previous value
    const restoreState = pagePreviouslySearchedValues[checkboxId];

    // Set checkbox state
    if (restoreState) {
      checkCheckbox(checkboxElement.id);
    } else {
      uncheckCheckbox(checkboxElement.id);
    }
  }
  
}