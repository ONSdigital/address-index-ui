// Initialise listeners and functionality to allow the download button to 
// download addresses from local storage

import { getPageLocalValues } from "/static/js/f_helpers/local_storage_page_helpers.mjs";
import { downloadCsvFromLocalStorage } from "/static/js/macros/custom_download_results_from_local_storage/download_helpers.mjs";

function getTheDownloadButton() {
  return document.querySelector('#download-address-results-button');  
}

function setupDownloadButtonListeners(page_name) {
  const downloadButton = getTheDownloadButton();

  downloadButton.addEventListener('click', (e) => {
    e.preventDefault();
    downloadCsvFromLocalStorage(page_name);
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

function setupDownloadButton(page_name) {
  const localPageValues = getPageLocalValues(page_name);
  const previousAddresses = localPageValues.mostRecentlySearchedAddresses || [];

  if (previousAddresses.length > 0) {
    setupDownloadButtonListeners(page_name);
    makeDownloadButtonContainerVisible();
  } else {
    makeDownloadButtonContainerInvisible();
  }
}

export function init(page_name) {
  // Setup event listener for 'refreshDownloadButton'
  document.addEventListener('refreshDownloadButton', () => {
    setupDownloadButton(page_name);
  });

  // Initially also run setup of download button
  setupDownloadButton(page_name);
}