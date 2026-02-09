import { setupDefaultGlobalValues } from '/static/js/e_all_pages/default_helpers/setup_defaults.mjs';
import { addMostRecentPageToStorage } from '/static/js/e_all_pages/breadcrumb_helpers/breadcrumbHelpers.mjs';

function removeResubmissionMessage() {
  if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
  }
}

export function allPagesFirstInit() {
  console.log('all_pages_first loaded');
  setupDefaultGlobalValues();
  addMostRecentPageToStorage();
  removeResubmissionMessage();
}
