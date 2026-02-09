
import { saveValueOfInput } from '../save_input_listeners.mjs';
import { selectInputFromHtmlIdUsingContainer } from "../component_selection.mjs";

export function addInputListenersToSaveOnChange(page_name, inputHtmlId) {
  // Get the input element
  const inputElement = selectInputFromHtmlIdUsingContainer(inputHtmlId);
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