import {
  getGlobalValues,
  setGlobalValues,
} from '/static/js/f_helpers/local_storage_page_helpers.mjs';

// Setup listeners and functionality for the reset settings button

function getResetSettingsContainer() {
  const resetContainer = document.querySelector('#reset-settings-container');

  if (!resetContainer) {
    console.error('Reset settings container not found in the DOM. Expected to find an element with the id "reset-settings-container".');
    return null;
  }

  return resetContainer;
}

function getResetButton(resetContainer) {
  const resetButton = resetContainer.querySelector('#reset-settings-button');

  if (!resetButton) {
    console.error('Reset settings button not found within the reset settings container:', resetContainer);
    return null;
  }

  return resetButton;
}

function getResetConfirmationInput(resetContainer) {
  const confirmationInput = resetContainer.querySelector('#reset-settings-confirmation-input');

  if (!confirmationInput) {
    console.error('Reset confirmation input not found within the reset settings container:', resetContainer);
    return null;
  }

  return confirmationInput;
}

export function setupResetSettingsButton() {
  // Get the container, reset button and confirmation input
  const resetContainer = getResetSettingsContainer();
  const resetButton = getResetButton(resetContainer);
  const confirmationInput = getResetConfirmationInput(resetContainer);

  // Add a listener to enforce caps on all input
  confirmationInput.addEventListener('input', () => {
    confirmationInput.value = confirmationInput.value.toUpperCase();
  });

  // Add a listener to the confirmationInput for each key up event to check input against 'RESET'
  confirmationInput.addEventListener('keyup', () => {
    const isContentReset = confirmationInput.value === 'RESET';
    if (isContentReset) {
      resetButton.classList.remove('ons-btn--disabled');
    } else {
      resetButton.classList.add('ons-btn--disabled');
    }
  });

}