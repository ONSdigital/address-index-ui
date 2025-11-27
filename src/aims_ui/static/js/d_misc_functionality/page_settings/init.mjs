import { setupDownloadFormatSetting } from './download_format_setting.mjs';
import { setupDownloadAttributesSetting } from './download_attributes_setting.mjs';
import { setupJobAgeSetting } from './job_age_setting.mjs';
import { setupAdditionalRequestSetting } from './additional_request_setting.mjs';
import { setupPafNagTitleSetting } from './paf_nag_title_setting.mjs';

import {
  getCustomColumnWidths,
  setNewColumnWidths,
} from '/static/js/f_helpers/local_storage_helpers.mjs';

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

  setValuesOfColumnWidthPreferences();
  setupColumnWidthCustomiserListeners();

  setupDownloadFormatSetting();
  setupDownloadAttributesSetting();
  setupJobAgeSetting();
  setupAdditionalRequestSetting();
  setupPafNagTitleSetting();
}

window.addEventListener('load', init);
