import {
  getGlobalValues,
  setGlobalValues,
} from '/static/js/f_helpers/local_storage_page_helpers.mjs';

import { checkCheckboxByElement } from './element_manipulation.mjs';

// Setup listeners, handlers and startup for PAF or NAG title setting for address cards

function getCheckboxByFullId(persistenceContainer, checkboxId) {
  const checkboxElement = persistenceContainer.querySelector(`#${checkboxId}`);

  if (!checkboxElement) {
    console.warn('No checkbox element found for id:', checkboxId);
  }

  return checkboxElement;
}

function getIdToUseForCheckboxSelection(pageName, inputObject) {
  // Given an inputObject as stored in setup_defaults, htmlId and pageName determine 
  // the id to use to select the persistence checkbox element

  const htmlId = inputObject.htmlId;
  const checkboxHtmlId = inputObject.persistenceCheckboxHtmlId;

  // Return the override htmlId if it exists
  if (checkboxHtmlId) {
    return checkboxHtmlId;
  }

  // Otherwise return the default constructed id
  return `${pageName}-${htmlId}`;
}

export function setupPersistenceSetting() {
  // Persistence settings are global despite being for all pages. 
  // Because the values have to be accessed from more than one page
  
  // Get the container for this setting
  const persistenceContainer = document.querySelector('#input-persistence-settings-container');

  // Get the value of the current persistence settings
  const globalValues = getGlobalValues();
  const inputSettings = globalValues.inputSettings || [];
  // Array of objects {page_name, [{inputObject, ...}]}

  // Loop over each pages's input settings
  for (const inputSetting of inputSettings) {
    // Get the stored page name and inputs
    const pageName = inputSetting.page;
    const inputObjects = inputSetting.inputObjects;
    const persistenceSettingDisabled = inputSetting.persistenceSettingDisabled;

    if (persistenceSettingDisabled) {
      // Skip this page if persistence setting is not present (currently for restricted pages)
      continue;
    }

    // Loop over each input object
    for (const inputObject of inputObjects) {
      const persistenceState = inputObject.persistenceState;

      const checkboxId = getIdToUseForCheckboxSelection(pageName, inputObject);
      const checkboxElement = getCheckboxByFullId(persistenceContainer, checkboxId);

      // If the checkbox element is disabled, skip it
      if (checkboxElement.disabled) {
        continue;
      }

      // Check the checkbox if persistenceState is true
      if (persistenceState) {
        checkCheckboxByElement(checkboxElement);
      }

      // Add a listener to update global values
      checkboxElement.addEventListener('change', () => {
        // Update the global values of inputSettings, inputObjects, object with htmlId/persistenceCheckboxHtmlId
        const updatedGlobalValues = getGlobalValues().inputSettings || [];

        for (const inputSetting of updatedGlobalValues) {
          // Look for the correct page
          if (inputSetting.page === pageName) {
            // Now the correct input 
            for (const inputObject of inputSetting.inputObjects) {
              // Now check 
              // 1. for the override id 
              // 2. for the default id
              if (inputObject.persistenceCheckboxHtmlId) {
                // Set it
                inputObject.persistenceState = checkboxElement.checked;
                console.debug('Updated persistence state for', inputObject.persistenceCheckboxHtmlId);
              }  else {
                // Check default id
                const defaultId = `${pageName}-${inputObject.htmlId}`;
                if (defaultId === checkboxId) {
                  inputObject.persistenceState = checkboxElement.checked;
                  console.debug('Updated persistence state for', defaultId);
                }
              }
            }
          }
        }

        // Save the updated global values
        setGlobalValues({ inputSettings: updatedGlobalValues });
        console.debug('Saving new global values for input persistence settings:', updatedGlobalValues);
      });

    }
  }
}