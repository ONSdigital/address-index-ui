

import { uncheckCheckbox, checkCheckbox } from '/static/js/d_misc_functionality/page_settings/element_manipulation.mjs';

export function restoreCheckboxValuesIfExist(page_name, htmlId, pagePreviouslySearchedValues) {
  // Given a single checkbox, restore its value

  // Get checkbox element 
  const checkboxElement = document.querySelector('#' + htmlId);

  if (!checkboxElement) {
    console.warn('No checkbox element found for Id:', htmlId);
    return;
  }

  // Get previous value
  const restoreState = pagePreviouslySearchedValues[htmlId];

  // Set checkbox state
  if (restoreState) {
    checkCheckbox(checkboxElement.id);
  } else {
    uncheckCheckbox(checkboxElement.id);
  }
}
