import { allPagesFirstInit } from '/static/js/e_all_pages/all_pages_first.mjs';
import { allPagesLastInit } from '/static/js/e_all_pages/all_pages_last.mjs';

export function init(page_name) {
  console.debug('Help Pages Init Running for page_name: ' + page_name);
  // All pages first
  allPagesFirstInit();

  // All pages last
  allPagesLastInit();
}