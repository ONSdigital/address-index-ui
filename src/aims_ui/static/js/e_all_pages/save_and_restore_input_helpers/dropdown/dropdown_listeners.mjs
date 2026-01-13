
import { saveValueOfInput } from '../save_input_listeners.mjs';

export function addDropdownListenersToSaveOnChange(page_name, htmlId) {
  // Get the dropdown element
  const dropdownElement = document.querySelector('#' + htmlId);

  if (!dropdownElement) {
    console.warn('No dropdown element found for Id:', htmlId);
    return;
  }

  dropdownElement.addEventListener('change', () => {
    console.debug(`Dropdown ${dropdownElement.id} selected with value: ${dropdownElement.value}`);
    saveValueOfInput(htmlId, dropdownElement.value, page_name);
  });
}