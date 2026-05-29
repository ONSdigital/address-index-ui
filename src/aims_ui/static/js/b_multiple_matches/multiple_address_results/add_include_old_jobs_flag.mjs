import { getDefaultGlobalValues } from '/static/js/e_all_pages/default_helpers/default_values.mjs';
import {
  getGlobalValues,
  setGlobalValues,
} from '/static/js/f_helpers/local_storage_page_helpers.mjs';

function getStoredPreferenceForIncludeOldJobsFlagFallbackToDefaultIfUnset() {
  const storedPreference = getGlobalValues().showOlderJobsInBulkMatchingPage;
  const defaultPreference = getDefaultGlobalValues().showOlderJobsInBulkMatchingPage;

  // If there is no stored preference, return the default preference
  if (typeof storedPreference === 'undefined') {
    console.debug('No stored preference for showOlderJobsInBulkMatchingPage, using default from defaults file:', defaultPreference);
    return defaultPreference;
  }

  // Otherwise, return the currently stored preference
  return storedPreference;
}

function checkIfParameterPresentInUrl(url, parameterName) {
  return url.searchParams.has(parameterName);
}

function updateLocalStorageToSetIncludeOldJobsPreference(currentUrl) {
  // Firstly get the value of the parameter in the URL
  const valueOfParameterInUrl = currentUrl.searchParams.get('include_old_jobs');

  const valueToSetInLocalStorage = valueOfParameterInUrl === 'true';
  // Update local storage to match the URL parameter
  setGlobalValues({
    ...getGlobalValues(),
    showOlderJobsInBulkMatchingPage: valueToSetInLocalStorage,
  });
}

function trueIfUrlHasParameterAndLocalStorageHasBeenUpdated(url) {
// Check to see if the parameter is present
  const parameterPresent = checkIfParameterPresentInUrl(url, 'include_old_jobs');

  // If the paramter is present, update local storage to override current preference
  if (parameterPresent) {
    updateLocalStorageToSetIncludeOldJobsPreference(url);
    return true;
  }
  return false;
}

export function addIncludeOldJobsFlagToUrlBasedOnLocalStorageSetting() {
  // Setup required info
  const url = new URL(window.location.href);

  // The order of priority is: 
  // 1. If the URL has parameter, honour it and update local storage to match
  // 2. If the URL does not have parameter and local storage does, then match the URL to local storage 

  // Step 1: Check the URL for the parameter and update local storage if it is present
  const wasLocalStorageUpdated = trueIfUrlHasParameterAndLocalStorageHasBeenUpdated(url);
  // Local storage was updated, the initial request contained a paramter so we don't need to do anything else
  if (wasLocalStorageUpdated) {
    return;
  }

  // Step 2: There was no URL paramter. 
  //   Check local storage for a preference
  //     If it's false, add the parameter but do NOT trigger a page refresh as the default is false anyway
  //     If it's true, add the paramter and trigger a page refresh
  
  // Get preference from local storage, if unset use default values in setup_defaults
  const storedPreference = getStoredPreferenceForIncludeOldJobsFlagFallbackToDefaultIfUnset();

  if (String(storedPreference) === 'false') {
    console.debug('Stored preference for showOlderJobsInBulkMatchingPage is false, adding include_old_jobs=false to URL without refreshing the page');
    // Add the param but do not trigger a refresh
    url.searchParams.set('include_old_jobs', 'false');
    window.history.pushState({}, '', url);
  } else if (String(storedPreference) === 'true') {
    console.debug('Stored preference for showOlderJobsInBulkMatchingPage is true, adding include_old_jobs=true to URL and refreshing the page');
    // Add the param and trigger a refresh
    url.searchParams.set('include_old_jobs', 'true');
    window.history.pushState({}, '', url);
    window.location.reload();
  } else {
    console.debug('Stored preference for showOlderJobsInBulkMatchingPage in Global Values is not recognised',
      'The value is:', storedPreference, 'Expected values are true, false, or unset. No changes made to URL');
  }

}

