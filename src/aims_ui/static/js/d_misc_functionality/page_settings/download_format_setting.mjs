import {
  getGlobalValues,
  setGlobalValues,
} from '/static/js/f_helpers/local_storage_page_helpers.mjs';
import { checkRadioButton } from '/static/js/d_misc_functionality/page_settings/element_manipulation.mjs';

// Setup listeners, handlers and startup for download settings on the preferences page

export function setupDownloadFormatSetting() {
  // Get the value of the current global download format setting
  const globalValues = getGlobalValues();
  const currentFormat = globalValues.singleJobDownloadFormat || 'csv';

  // Check the appropriate radio button
  if (currentFormat === 'csv') {
    checkRadioButton('download-results-csv-radio');
  } else if (currentFormat === 'json') {
    checkRadioButton('download-results-json-radio');
  }

  // Add listeners to change the global setting 
  const csvRadio = document.querySelector('#download-results-csv-radio');
  const jsonRadio = document.querySelector('#download-results-json-radio');

  // Csv radio clicked - set global value to 'csv'
  csvRadio.addEventListener('change', () => {
    setGlobalValues({ singleJobDownloadFormat: 'csv' });
  });

  // Json radio clicked - set global value to 'json'
  jsonRadio.addEventListener('change', () => {
    setGlobalValues({ singleJobDownloadFormat: 'json' });
  });
}