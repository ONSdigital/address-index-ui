import {
  getGlobalValues,
  getPageLocalValues,
  setPageLocalValues,
} from '/static/js/f_helpers/local_storage_page_helpers.mjs';


import { getDefaultValuesForPage } from '../setup_defaults.mjs';

export function setPreviouslyStoredValuesForThisPage(inputValues, page_name) {
  // Set the pagePreviouslySearchedValues to the new inputValues
  setPageLocalValues(page_name, { pagePreviouslySearchedValues: inputValues });
}

export function getPagePreviouslySearchedValues(page_name) {
  // Get the local values for this page
  const pageLocalValues = getPageLocalValues(page_name);

  // Inject default values if the pagePreviouslySearchedValues doesn't exist
  const defaultValuesForPage = getDefaultValuesForPage(page_name);
  if (!pageLocalValues.pagePreviouslySearchedValues) {
    // If we have to setup the defaults, then we should also save them to local storage as the "previously searched values"
    pageLocalValues.pagePreviouslySearchedValues = defaultValuesForPage;
    setPreviouslyStoredValuesForThisPage(pageLocalValues.pagePreviouslySearchedValues, page_name);
  }

  // Extract the pagePreviouslySearchedValues, default to an empty object if no defaults defined
  return pageLocalValues.pagePreviouslySearchedValues || {};
}

function getPersistanceSettingsOfPage(page_name) {
  // Will return an array of input Ids, setup in global storage
  const globalValues = getGlobalValues();
  // An array of objects like [ {'page_name':'radiussearch', {object of settings}
  const persistanceSettings = globalValues['persistanceSettings'] || [];

  // Find the object for this page
  for (const pageSetting of persistanceSettings) {
    if (pageSetting.page === page_name) {
      return pageSetting;
    }
  }

  // If not found, log an error
  console.error('No persistance settings found for page:', page_name);
}

export function getIdsOfInputsToPersist(page_name) {
  // Get the persistance settings for this page
  const pagePersistanceSettings = getPersistanceSettingsOfPage(page_name);
  const inputPersistanceSettings = pagePersistanceSettings.input_persistance_settings || {};
  
  // Now extract the Ids of inputs that should be persisted {'inputId': true/false}
  const idsToPersist = [];
  for (const [inputId, shouldPersist] of Object.entries(inputPersistanceSettings)) {
    if (shouldPersist) {
      idsToPersist.push(inputId);
    }
  }

  return idsToPersist;
}