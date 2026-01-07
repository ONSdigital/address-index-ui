// Initialise listeners and functionality to allow the download button to 
// download addresses from local storage

import { getPageLocalValues, getGlobalValues } from "/static/js/f_helpers/local_storage_page_helpers.mjs";
import { downloadJsonFromLocalStorage } from "/static/js/macros/custom_download_results_from_local_storage/download_json.mjs";
import { downloadCsvFromLocalStorage } from "/static/js/macros/custom_download_results_from_local_storage/download_csv.mjs";

function getTheDownloadButton() {
  return document.querySelector('#download-address-results-button');  
}

function setupDownloadButtonListeners(page_name, downloadButtonSettings) {
  const downloadButton = getTheDownloadButton();

  // Get the preference for download format
  const downloadFormat = downloadButtonSettings.downloadFormat;

  downloadButton.addEventListener('click', (e) => {
    e.preventDefault();
    if (downloadFormat === 'csv') {
      downloadCsvFromLocalStorage(page_name);
    } else if (downloadFormat === 'json') {
      downloadJsonFromLocalStorage(page_name);
    }
  });
}

function makeDownloadButtonContainerVisible() {
  // Get a handle on the container
  const container = document.querySelector('#container-for-download-address-results-button');
  container.classList.remove('invisible');
}

export function makeDownloadButtonContainerInvisible() {
  // Get a handle on the container
  const container = document.querySelector('#container-for-download-address-results-button');
  container.classList.add('invisible');
}

function setupDownloadButtonVisibility(page_name) {
  const localPageValues = getPageLocalValues(page_name);
  const previousAddresses = localPageValues.mostRecentlySearchedAddresses || [];

  if (previousAddresses.length > 0) {
    makeDownloadButtonContainerVisible();
  } else {
    makeDownloadButtonContainerInvisible();
  }
}

function setupDownloadButtonText(downloadButtonSettings) {
  // The user will have a global preference for download format
  const downloadFormat = downloadButtonSettings.downloadFormat;
  const singleJobDownloadAttributeInclusion = downloadButtonSettings.singleJobDownloadAttributeInclusion;

  const downloadButton = getTheDownloadButton();
  const textContainerInsideButton = downloadButton.querySelector('.ons-btn__text');

  let buttonText = 'Download ';

  // Add the text to describe all attributes or just favourites
  if (singleJobDownloadAttributeInclusion === 'all') {
    buttonText += ' all attributes ';
  } else if (singleJobDownloadAttributeInclusion === 'favourites_only') {
    buttonText += ' only favourite attributes ';
  }

  // Add the file extension text
  if (downloadFormat === 'csv') {
    buttonText += ' as CSV';
  } else if (downloadFormat === 'json') {
    buttonText += ' as JSON';
  }

  // Set the text content of the button
  textContainerInsideButton.textContent = buttonText;
}

function getDownloadButtonSettings() {
  // Get the globally set preferences of the Download Functionality
  const globalValues = getGlobalValues();
  const downloadFormat = globalValues.singleJobDownloadFormat || 'csv';
  const singleJobDownloadAttributeInclusion = globalValues.singleJobDownloadAttributeInclusion || 'all';

  return {
    downloadFormat: downloadFormat,
    singleJobDownloadAttributeInclusion: singleJobDownloadAttributeInclusion,
  };
}

export function init(page_name) {
  // Get the globally set preferences of the Download Functionality
  const downloadButtonSettings = getDownloadButtonSettings();

  // Setup event listener for 'refreshDownloadButton'
  document.addEventListener('refreshDownloadButton', () => {
    setupDownloadButtonVisibility(page_name);
  });

  // Initially run the visibility setup
  setupDownloadButtonVisibility(page_name);

  setupDownloadButtonText(downloadButtonSettings);

  // Setup download button listeners
  setupDownloadButtonListeners(page_name, downloadButtonSettings);
}