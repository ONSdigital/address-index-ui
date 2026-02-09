import { setupDownloadFormatSetting } from './download_format_setting.mjs';
import { setupDownloadAttributesSetting } from './download_attributes_setting.mjs';
import { setupJobAgeSetting } from './job_age_setting.mjs';
import { setupAdditionalRequestSetting } from './additional_request_setting.mjs';
import { setupPafNagTitleSetting } from './paf_nag_title_setting.mjs';
import { setupColumnWidthSetting } from './column_width_setting.mjs';
import { setupPersistenceSetting } from './persistence_setting.mjs';

function init() {
  console.log('Page Settings Init Running');

  // Every segement of the settings page has its own setup function 
  // restoring the values and adding listeners to set them
  setupDownloadFormatSetting();
  setupDownloadAttributesSetting();
  setupJobAgeSetting();
  setupAdditionalRequestSetting();
  setupPafNagTitleSetting();
  setupColumnWidthSetting();
  setupPersistenceSetting();
}

window.addEventListener('load', init);
