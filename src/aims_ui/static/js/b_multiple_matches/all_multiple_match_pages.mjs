import { getGlobalValues } from '/static/js/f_helpers/local_storage_page_helpers.mjs';

function updateResultsUrl() {
  // Get the current preference
  const current_job_preference = getGlobalValues().showOlderJobsInBulkMatchingPage;

  // Get all URLs on a page
  const allUrls = document.querySelectorAll('a');

  // Loop through all URLs, check if href is '/multiple_address_results'
  for (const url of allUrls) {
    if (url.href.includes('/multiple_address_results')) {
      // If it is, check if the URL already contains the flag
      if (url.href.includes('include_old_jobs')) {
        return;
      } else {
        // If it doesn't, add the flag
        const urlObj = new URL(url.href);
        urlObj.searchParams.set('include_old_jobs', current_job_preference);
        url.href = urlObj.href;
      }
    }
  }
}

function init() {
  console.log('update_results_url loaded');
  // Update the URL to include the flag in the localstorage
  updateResultsUrl();
}

window.addEventListener('load', init);
