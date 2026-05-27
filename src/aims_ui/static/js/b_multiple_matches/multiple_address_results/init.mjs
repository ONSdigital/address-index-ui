import { allPagesFirstInit } from '/static/js/e_all_pages/all_pages_first.mjs';
import { allPagesLastInit } from '/static/js/e_all_pages/all_pages_last.mjs';
import { setupResultsButtonAndProcessing } from './download_and_process/setup_download_buttons.mjs';
import { addIncludeOldJobsFlagToUrlBasedOnLocalStorageSetting } from './download_and_process/add_include_old_jobs_flag.mjs';

export function init(page_name) {
  // All pages first
  allPagesFirstInit();

  // Page specific scripts here
  addIncludeOldJobsFlagToUrlBasedOnLocalStorageSetting();

  setupResultsButtonAndProcessing(page_name);

  // All pages last
  allPagesLastInit();
}

