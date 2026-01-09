
import { saveValueOfInput } from '../save_input_listeners.mjs';

export function addInputListenersToSaveOnChange(page_name, inputHtmlId) {

  // Get the input element
  const inputElement = document.querySelector('#' + inputHtmlId);

  // Error if the element is not found
  if (!inputElement) {
    console.warn('No input element found for Id:', inputHtmlId);
    return;
  }

  // Attach the event listener, when any key is pressed
  inputElement.addEventListener('input', () => {
    saveValueOfInput(inputHtmlId, inputElement.value, page_name);
  });
}