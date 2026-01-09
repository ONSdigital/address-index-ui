
import { saveValueOfInput } from '../save_input_listeners.mjs';

export function addCheckboxListenersToMultipleCheckboxes(page_name, inputObject) {
  const checkboxIds = inputObject.checkboxHtmlIds || [];

  for (const checkboxId of checkboxIds) {
    const checkbox = document.querySelector('#' + checkboxId);
    if (!checkbox) {
      console.warn('No container element found for region container Id:', checkboxId);
      continue;
    }

    // Add event listener to save on change
    console.log('Adding checkbox listener to checkbox Id:', checkboxId);
    checkbox.addEventListener('change', () => {
      const isChecked = checkbox.checked;
      console.log(`Checkbox ${checkbox.id} changed to: ${isChecked}`);
      saveValueOfInput(checkbox.id, isChecked, page_name);
    });
  }
}