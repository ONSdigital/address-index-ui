// Listeners for region inputs (dropdown)

import { saveValueOfInput } from '../save_input_listeners.mjs';


export function addListenerForDropdown(inputElement, page_name) {
  // Add event listener to save on change

  inputElement.addEventListener('change', () => {
    console.debug('Dropdown changed, saving value: ', inputElement.value);
    const selectedValue = inputElement.value;
    saveValueOfInput(inputElement.id, selectedValue, page_name);
  });
}
