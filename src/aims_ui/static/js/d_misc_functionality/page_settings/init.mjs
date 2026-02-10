import { setupDownloadFormatSetting } from './download_format_setting.mjs';
import { setupDownloadAttributesSetting } from './download_attributes_setting.mjs';
import { setupJobAgeSetting } from './job_age_setting.mjs';
import { setupAdditionalRequestSetting } from './additional_request_setting.mjs';
import { setupPafNagTitleSetting } from './paf_nag_title_setting.mjs';
import { setupColumnWidthSetting } from './column_width_setting.mjs';
import { setupPersistenceSetting } from './persistence_setting.mjs';
import { allPagesLastInit } from '/static/js/e_all_pages/all_pages_last.mjs';
import { allPagesFirstInit } from '/static/js/e_all_pages/all_pages_first.mjs';

export function init() {
  console.log('Page Settings Init Running');

  // All pages first
  allPagesFirstInit();


  // Every segement of the settings page has its own setup function 
  // restoring the values and adding listeners to set them
  setupDownloadFormatSetting();
  setupDownloadAttributesSetting();
  setupJobAgeSetting();
  setupAdditionalRequestSetting();
  setupPafNagTitleSetting();
  setupColumnWidthSetting();
  setupPersistenceSetting();


  // All pages last
  allPagesLastInit();
}

