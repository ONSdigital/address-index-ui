
import { returnCurrentPageMap } from './region_helpers.mjs';
import { uncheckCheckbox, checkCheckbox } from '/static/js/d_misc_functionality/page_settings/element_manipulation.mjs';


export function restoreRegionValuesIfExist(page_name, inputId, pagePreviouslySearchedValues) {

  // Only the suffix is saved to local storage, so use the prefix to create full ids
  // pagePreviouslySearchedValues = {eboost: false, wboost: false, sboost: false}

  const currentPageMap = returnCurrentPageMap(page_name);
  // These suffixes match keys in pagePreviouslySearchedValues
  const container_id_suffixes = currentPageMap.container_id_suffixes;

  // For each suffix in container_id_suffixes 
  for (const suffix of container_id_suffixes) {
    // Check if that suffix has a stored value in pagePreviouslySearchedValues
    if (suffix in pagePreviouslySearchedValues) {
      const prefix = currentPageMap.container_prefix;
      const fullContainerId = prefix + suffix;

      // Get the checkbox element within that container
      const checkboxElement = document.querySelector('#' + fullContainerId + ' input[type="checkbox"]');
      if (!checkboxElement) {
        console.warn('No checkbox element found for region container Id:', fullContainerId);
        continue;
      }

      const restoreState = pagePreviouslySearchedValues[suffix];
      if (restoreState) {
        checkCheckbox(checkboxElement.id);
      } else {
        uncheckCheckbox(checkboxElement.id);
      }
    }
  }
  
}