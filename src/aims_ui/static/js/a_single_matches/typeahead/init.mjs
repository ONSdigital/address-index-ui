import { allPagesFirstInit } from '/static/js/e_all_pages/all_pages_first.mjs';
import { saveAndRestoreInputsInit } from '/static/js/e_all_pages/save_and_restore_inputs.mjs';
import { customColumnWidthsInit } from '/static/js/e_all_pages/custom_column_widths.mjs';
import { allPagesLastInit } from '/static/js/e_all_pages/all_pages_last.mjs';
import { setupEventListenersToChangeTypeaheadParams } from './typeahead_parameters_functionality.mjs';

export function init(page_name) {
  // All pages first
  allPagesFirstInit();

  // Setup save and restore inputs
  saveAndRestoreInputsInit(page_name);

  // Page specific scripts here
  setupEventListenersToChangeTypeaheadParams();
 
  // Apply the custom column widths
  customColumnWidthsInit();

  // All pages last
  allPagesLastInit();
}

