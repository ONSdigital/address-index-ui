import { setupDownloadFormatSetting } from './download_format_setting.mjs';
import { setupDownloadAttributesSetting } from './download_attributes_setting.mjs';
import { setupJobAgeSetting } from './job_age_setting.mjs';
import { setupAdditionalRequestSetting } from './additional_request_setting.mjs';

import {
  getAddressTitlePreference,
  updateAddressFormatPreference,
  getCustomColumnWidths,
  setNewColumnWidths,
} from '/static/js/f_helpers/local_storage_helpers.mjs';

function updateAddressTitlePreference(e) {
  updateAddressFormatPreference(e);
}

// Paf and Nag Preferences
function setupNagAndPafStatus() {
  const current_status = getAddressTitlePreference();
  if (current_status === 'paf') {
    const pafRadio = document.querySelector('#paf-radio');
    pafRadio.checked = true;
  } else if (current_status === 'nag') {
    const nagRadio = document.querySelector('#nag-radio');
    nagRadio.checked = true;
  } else if (current_status === 'def') {
    const defRadio = document.querySelector('#default-radio');
    defRadio.checked = true;
  }
}

function setupNagAndPafListeners() {
  const pafRadio = document.querySelector('#paf-radio');
  const nagRadio = document.querySelector('#nag-radio');
  const defRadio = document.querySelector('#default-radio');

  pafRadio.addEventListener('change', (e) => {
    updateAddressTitlePreference('paf');
  });

  nagRadio.addEventListener('change', (e) => {
    updateAddressTitlePreference('nag');
  });

  defRadio.addEventListener('change', (e) => {
    updateAddressTitlePreference('def');
  });
}

// Column Width Preferences
function setValuesOfColumnWidthPreferences() {
  const colWidths = getCustomColumnWidths();
  for (const [key, width] of Object.entries(colWidths)) {
    const colInput = document.querySelector('#selector_' + key);
    colInput.value = width;
  }
}

function saveWidthValues(widthSelectors) {
  const newWidthValues = {};
  for (const selector of widthSelectors) {
    const selectorName = selector.id.replace('selector_', '');
    newWidthValues[selectorName] = selector.value;
  }
  setNewColumnWidths(newWidthValues);
}

function setupColumnWidthCustomiserListeners() {
  const widthSelectors = document.querySelectorAll('.columnWidthCustomiser');
  for (const selector of widthSelectors) {
    selector.addEventListener('change', (e) => {
      saveWidthValues(widthSelectors);
    });
  }
}

function init() {
  console.log('Page Settings Init Running');

  setupNagAndPafListeners();
  setupNagAndPafStatus();
  setValuesOfColumnWidthPreferences();
  setupColumnWidthCustomiserListeners();

  setupDownloadFormatSetting();
  setupDownloadAttributesSetting();
  setupJobAgeSetting();
  setupAdditionalRequestSetting();
}

window.addEventListener('load', init);
