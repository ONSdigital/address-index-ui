import { getGlobalValues } from '/static/js/f_helpers/local_storage_page_helpers.mjs';

function addJobsFlagToCurrentURL() {
  // Get the current preference
  const currentJobPreference = getGlobalValues().showOlderJobsInBulkMatchingPage;
  const currentURL = window.location.href;

  // Check to see if the flag alredy exists
  if (currentURL.includes('include_old_jobs')) {
    return;
  } else {
    const url = new URL(currentURL);
    url.searchParams.set('include_old_jobs', currentJobPreference);
    // Forward user to the new URL
    window.history.pushState({}, '', url);
    // Trigger new page load
    window.location.reload();
  }
}

export function addIncludeOldJobsFlagToUrlBasedOnLocalStorageSetting() {
  // Get the current preference
  const currentJobPreference = getGlobalValues().showOlderJobsInBulkMatchingPage;
  const currentURL = window.location.href;

  // The order of priority is:
    // 1. If the URL has parameter, honour it and update local storage to match
    // 2. If the URL does not have parameter and local storage does, then match the URL to local storage
    // 3. If the URL does not have parameter, add included_old_jobs to false (default)
  
  if (currentURL.includes('include_old_jobs')) {
    //

  if (currentURL.includes('include_old_jobs')) {
    return;
  } else {
    const url = new URL(currentURL);
    url.searchParams.set('include_old_jobs', currentJobPreference);
    // Forward user to the new URL
    window.history.pushState({}, '', url);
    // Trigger new page load
    window.location.reload();
  }
}


