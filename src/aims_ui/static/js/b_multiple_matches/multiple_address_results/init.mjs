import { allPagesFirstInit } from '/static/js/e_all_pages/all_pages_first.mjs';
import { customColumnWidthsInit } from '/static/js/e_all_pages/custom_column_widths.mjs';
import { allPagesLastInit } from '/static/js/e_all_pages/all_pages_last.mjs';
import { addIncludeOldJobsFlagToUrlBasedOnLocalStorageSetting } from './add_include_old_jobs_flag.mjs';
import { setupResultsButtonAndProcessing } from './multiple_address_results.mjs';

export function init(page_name) {
  // All pages first
  allPagesFirstInit();

  // Page specific scripts here
  addIncludeOldJobsFlagToUrlBasedOnLocalStorageSetting();
  setupResultsButtonAndProcessing();
 
  // Apply the custom column widths
  customColumnWidthsInit();

  // All pages last
  allPagesLastInit();
}

