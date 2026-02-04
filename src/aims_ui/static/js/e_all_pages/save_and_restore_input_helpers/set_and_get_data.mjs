import {
  getGlobalValues,
  getPageLocalValues,
  setPageLocalValues,
} from '/static/js/f_helpers/local_storage_page_helpers.mjs';


import { getDefaultValuesForPage } from '../default_helpers/setup_defaults.mjs';

export function setPreviouslyStoredValuesForThisPage(inputValues, page_name) {
  // Set the pagePreviouslySearchedValues to the new inputValues
  setPageLocalValues(page_name, { pagePreviouslySearchedValues: inputValues });
}

export function getPagePreviouslySearchedValues(page_name) {
  // Get the local values for this page
  const pageLocalValues = getPageLocalValues(page_name);

  // Inject default values if the pagePreviouslySearchedValues doesn't exist
  const defaultValuesForPage = getDefaultValuesForPage(page_name);
  console.debug('default values are:', defaultValuesForPage);

  if (!pageLocalValues.pagePreviouslySearchedValues) {
    // If we have to setup the defaults, then we should also save them to local storage as the "previously searched values"
    pageLocalValues.pagePreviouslySearchedValues = defaultValuesForPage;
    console.debug('Setting up default previously searched values for page:', page_name, 'as:', pageLocalValues.pagePreviouslySearchedValues);
    setPreviouslyStoredValuesForThisPage(pageLocalValues.pagePreviouslySearchedValues, page_name);
  }

  // Extract the pagePreviouslySearchedValues, default to an empty object if no defaults defined
  return pageLocalValues.pagePreviouslySearchedValues || {};
}

function getPersistanceSettingsOfPage(page_name) {
  const globalValues = getGlobalValues();

  // An array of objects like [ {'page_name':'radiussearch', 'inputObjects': [ {'htmlId': 'input', 'persistance_state': true}, ... ]}]
  const persistanceSettings = globalValues['inputSettings'] || [];

  // Find the object for this page
  for (const pageSetting of persistanceSettings) {
    if (pageSetting.page === page_name) {
      return pageSetting;
    }
  }

  // If not found, log an error
  console.error('No persistance settings found for page: "', page_name, '" in global values.');
  return [];
}

export function getPageInputObjects(page_name) {
  // For the page provided, return the locally stored input objects

  // Get the persistance settings for this page
  const pageInputSettings = getPersistanceSettingsOfPage(page_name);
  const inputObjects = pageInputSettings.inputObjects || [];

  return inputObjects;
}