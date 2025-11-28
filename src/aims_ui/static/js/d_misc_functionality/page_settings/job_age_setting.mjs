import {
  getGlobalValues,
  setGlobalValues,
} from '/static/js/f_helpers/local_storage_page_helpers.mjs';
import { uncheckCheckbox, checkCheckbox } from '/static/js/d_misc_functionality/page_settings/element_manipulation.mjs';

// Setup listeners, handlers and startup for job age setting

export function setupJobAgeSetting() {
  // Get the value of the current global job age setting
  const globalValues = getGlobalValues();
  const currentJobAgeStatus = globalValues.showOlderJobsInBulkMatchingPage || false;

  // Check or uncheck the checkbox
  const checkboxId = 'show-old-jobs-checkbox';
  if (currentJobAgeStatus === true) {
    checkCheckbox(checkboxId);
  } else {
    uncheckCheckbox(checkboxId);
  }
  

  // Add listeners to change the global setting 
  const checkboxHtmlObject = document.querySelector(`#${checkboxId}`);

  // On change set the global value
  checkboxHtmlObject.addEventListener('change', () => {
    setGlobalValues({ showOlderJobsInBulkMatchingPage: checkboxHtmlObject.checked });
  });
}