import {
  getGlobalValues,
  setGlobalValues,
} from '/static/js/f_helpers/local_storage_page_helpers.mjs';

import { checkRadioButton } from '/static/js/d_misc_functionality/page_settings/element_manipulation.mjs';

// Setup listeners, handlers and startup for PAF or NAG title setting for address cards

export function setupPafNagTitleSetting() {
  // Get the value of the current global download format setting
  const globalValues = getGlobalValues();
  const currentTitlePreference = globalValues.addressCardTitleType || 'default';

  // Set the ids for the radio buttons
  const pafRadioId = 'address-card-title-paf-radio';
  const nagRadioId = 'address-card-title-nag-radio';
  const defaultRadioId = 'address-card-title-default-radio';

  // Check the appropriate radio button
  if (currentTitlePreference === 'paf') {
    checkRadioButton(pafRadioId);
  } else if (currentTitlePreference === 'nag') {
    checkRadioButton(nagRadioId);
  } else if (currentTitlePreference === 'default') {
    checkRadioButton(defaultRadioId);
  }

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