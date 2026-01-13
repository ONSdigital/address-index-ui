
import { saveValueOfInput } from '../save_input_listeners.mjs';

export function addCheckboxListenersToSaveOnChange(page_name, checkboxHtmlId) {
  // Given the unique html Id, add a saving event listener

  const checkboxElement = document.querySelector('#' + checkboxHtmlId);
  if (!checkboxElement) {
    console.warn('No checkbox element found for Id:', checkboxHtmlId);
    return;
  }

  // Add event listener to save on change
  checkboxElement.addEventListener('change', () => {
    const isChecked = checkboxElement.checked;
    console.debug(`Checkbox ${checkboxElement.id} changed to: ${isChecked}`);
    saveValueOfInput(checkboxHtmlId, isChecked, page_name);
  });
}

export function addCheckboxListenersToMultipleCheckboxes(page_name, inputObject) {
  const checkboxIds = inputObject.checkboxHtmlIds || [];

  for (const checkboxId of checkboxIds) {
    // Add event listener to save on change
    addCheckboxListenersToSaveOnChange(page_name, checkboxId);
  }
}