import {
  getGlobalValues,
  setGlobalValues,
} from '/static/js/f_helpers/local_storage_page_helpers.mjs';

import { checkRadioButton } from '/static/js/d_misc_functionality/page_settings/element_manipulation.mjs';

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

      // If the checkbox element is enabled
      if (!checkboxElement.disabled) {
        if (isPersisted) {
          checkRadioButton(checkboxId);
        }
      }
    }
  }
  
  return;
  // Add listeners to change the global setting 
  const pafRadio = document.querySelector(`#${pafRadioId}`);
  const nagRadio = document.querySelector(`#${nagRadioId}`);
  const defaultRadio = document.querySelector(`#${defaultRadioId}`);

  // Set the preference to 'paf' when the paf radio is clicked
  pafRadio.addEventListener('change', () => {
    setGlobalValues({ addressCardTitleType: 'paf' });
  });

  // Set the preference to 'nag' when the nag radio is clicked
  nagRadio.addEventListener('change', () => {
    setGlobalValues({ addressCardTitleType: 'nag' });
  });

  // Set the preference to 'default' when the default radio is clicked
  defaultRadio.addEventListener('change', () => {
    setGlobalValues({ addressCardTitleType: 'default' });
  });

}