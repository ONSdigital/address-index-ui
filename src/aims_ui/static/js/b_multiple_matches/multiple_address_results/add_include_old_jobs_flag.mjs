import {
  getGlobalValues,
  setGlobalValues,
} from '/static/js/f_helpers/local_storage_page_helpers.mjs';

export function addIncludeOldJobsFlagToUrlBasedOnLocalStorageSetting() {
  const url = new URL(window.location.href);
  const parameterName = 'include_old_jobs';
  const storedPreference = getGlobalValues().showOlderJobsInBulkMatchingPage;

  // If the URL has the parameter, honour it and update local storage.
  if (url.searchParams.has(parameterName)) {
    const urlPreference = url.searchParams.get(parameterName) === 'true';

    setGlobalValues({
      ...getGlobalValues(),
      showOlderJobsInBulkMatchingPage: urlPreference,
    });

    return;
  }

  let preferenceToUse = false;

  // If local storage has a preference, use it for the URL parameter.
  if (typeof storedPreference === 'boolean') {
    preferenceToUse = storedPreference;
  }

  // If local storage does not have a preference, use false as the default.
  url.searchParams.set(parameterName, String(preferenceToUse));

  // Forward the user to the updated URL.
  window.history.pushState({}, '', url);

  // Trigger a page reload using the updated URL.
  window.location.reload();
}