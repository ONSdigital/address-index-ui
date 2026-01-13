
import { saveValueOfInput } from '../save_input_listeners.mjs';

export function addRadioListenersToMultipleRadios(page_name, inputObject) {
  // Get the ids of the epoch options inside the Radio Container
  const containerId = 'complete-container-for-' + inputObject.htmlId;
  const containerElement = document.querySelector('#' + containerId);

  if (!containerElement) {
    console.warn('No container element found for radio container Id:', containerId);
    return;
  }

  // Now get a list of all radio input ids inside container
  const radioInputs = containerElement.querySelectorAll('input[type="radio"][name="' + inputObject.htmlId + '"]');

  if (radioInputs.length === 0) {
    console.warn('No radio inputs found inside container for Id:', containerId);
    return;
  }

  // Now add event listeners to each radio input
  for (const radioInput of radioInputs) {
    console.debug('Adding radio listener to radio Id:', radioInput.id);
    radioInput.addEventListener('change', () => {
      if (radioInput.checked) {
        console.debug(`Radio ${radioInput.id} selected with value: ${radioInput.value}`);
        saveValueOfInput(radioInput.name, radioInput.value, page_name);
      }
    });
  }
}