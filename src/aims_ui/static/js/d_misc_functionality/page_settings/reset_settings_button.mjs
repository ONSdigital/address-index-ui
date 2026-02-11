import { getDefaultGlobalValues } from '/static/js/e_all_pages/default_helpers/default_values.mjs';
import {
  setGlobalValues,
} from '/static/js/f_helpers/local_storage_page_helpers.mjs';

// Setup listeners and functionality for the reset settings button

function resetSettingsToDefaultValues() {
  // Get the default global settings
  const defaultGlobalValues = getDefaultGlobalValues();
  console.debug('Resetting settings to default values. Default global values to be set:', defaultGlobalValues);

  // Set the global values as the default values
  setGlobalValues(defaultGlobalValues);
}

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
      resetButton.disabled = false;
      resetButton.classList.remove('ons-btn--disabled');
    } else {
      resetButton.disabled = true;
      resetButton.classList.add('ons-btn--disabled');
    }
  });

  // Add click listener to reset button
  resetButton.addEventListener('click', () => {
    console.log('Reset settings button clicked. Checking confirmation input and button state before resetting settings.');
    if (confirmationInput.value !== 'RESET') {
      console.warn('Reset settings button clicked but confirmation input does not match "RESET". Action will not be performed.');
      return;
    }

    // Check the css for the button doesnt have ons-btn--disabled
    if (resetButton.classList.contains('ons-btn--disabled')) {
      console.warn('Reset settings button clicked but button is disabled. Action will not be performed.');
      return;
    }

    // Run the reset local storage script, refresh page
    resetSettingsToDefaultValues();

    // Refresh the page to apply the default settings
    location.reload();
  });
}