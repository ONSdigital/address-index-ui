import {
  getGlobalValues,
  setGlobalValues,
} from '/static/js/f_helpers/local_storage_page_helpers.mjs';

import { checkRadioButtonByElement } from './element_manipulation.mjs';

// Setup listeners, handlers and startup for PAF or NAG title setting for address cards

export function setupPersistanceSetting() {
  // Persistance settings are global despite being for all pages. 
  // Because the values have to be accessed from more than one page
  
  // Get the container for this setting
  const persistanceContainer = document.querySelector('#input-persistance-settings-container');

  // Get the value of the current persistance settings
  const globalValues = getGlobalValues();
  const currentPersistanceSettings = globalValues.persistanceSettings || [];
  // Array of objects

  // Setup the current checkbox states
  // Firstly get a handle on each checkbox
  for (const pagePersistanceSetting of currentPersistanceSettings) {
    // Page name is used in each checkbox id
    const pageName = pagePersistanceSetting.page;
    const inputPersistanceSettings = pagePersistanceSetting.input_persistance_settings;

    // The inputPersistanceSettings is an object with key as input name and value as boolean
    for (const [inputName, isPersisted] of Object.entries(inputPersistanceSettings)) {
      const checkboxId = `${pageName}-${inputName}-checkbox`;
      const checkboxElement = persistanceContainer.querySelector(`#${checkboxId}`);

      // If the checkbox element doesn't exist, skip it
      if (!checkboxElement) {
        console.warn('No checkbox element found for id:', checkboxId);
        continue;
      }

      // If the checkbox element is enabled
      if (!checkboxElement.disabled) {
        if (isPersisted) {
          checkRadioButtonByElement(checkboxElement);
        }

        // Add a listener to update the global values when changed
        checkboxElement.addEventListener('change', () => {
          // Update the relevant value in the global persistance settings
          const updatedPersistanceSettings = getGlobalValues().persistanceSettings || [];

          // Loop through and find the right page and input to update
          for (const setting of updatedPersistanceSettings) {
            if (setting.page === pageName) {
              setting.input_persistance_settings[inputName] = checkboxElement.checked;
            }
          }

          // Save the updated settings back to global values
          setGlobalValues({ persistanceSettings: updatedPersistanceSettings });
        });
      }
    }
  }
}