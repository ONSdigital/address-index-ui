import {
  getGlobalValues,
  setGlobalValues,
} from '/static/js/f_helpers/local_storage_page_helpers.mjs';

function checkRadioButton(documentId) {
  const radioButton = document.querySelector(`#${documentId}`);
  if (radioButton) {
    radioButton.checked = true;
  }
}

export function setupDownloadAttributesSetting() {
  // Get the value of the current global download attribute inclusion setting
  const globalValues = getGlobalValues();
  const currentFormat = globalValues.singleJobDownloadAttributeInclusion || 'all';

  // Check the appropriate radio button
  if (currentFormat === 'all') {
    checkRadioButton('download-results-full-radio');
  } else if (currentFormat === 'favourites_only') {
    checkRadioButton('download-results-favourites-radio');
  }

  // Add listeners to change the global setting 
  const allAttributesRadio = document.querySelector('#download-results-full-radio');
  const favouritesOnlyRadio = document.querySelector('#download-results-favourites-radio');

  // All attributes radio clicked - set global value to 'all'
  allAttributesRadio.addEventListener('change', () => {
    setGlobalValues({ singleJobDownloadAttributeInclusion: 'all' });
  });

  // Favourites only radio clicked - set global value to 'favourites_only'
  favouritesOnlyRadio.addEventListener('change', () => {
    setGlobalValues({ singleJobDownloadAttributeInclusion: 'favourites_only' });
  });
}