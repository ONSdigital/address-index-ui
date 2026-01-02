
import { returnCurrentPageMap } from './region_helpers.mjs';
import { uncheckCheckbox, checkCheckbox } from '/static/js/d_misc_functionality/page_settings/element_manipulation.mjs';


export function restoreRegionValuesIfExist(page_name, inputId, pagePreviouslySearchedValues) {

  // Only the suffix is saved to local storage, so use the prefix to create full ids
  // pagePreviouslySearchedValues = {eboost: false, wboost: false, sboost: false}

  const currentPageMap = returnCurrentPageMap(page_name);

  // Check to see if the region_type is 'checkboxes' or 'inputs'
  const region_type = currentPageMap.region_type || 'checkboxes';

  console.log('Region type for page', page_name, ':', region_type);
  if (region_type === 'inputs') {
    restoreRegionInputValuesIfExist(page_name, currentPageMap, pagePreviouslySearchedValues);
  } else if (region_type === 'checkboxes') {
    restoreCheckboxValuesIfExist(page_name, currentPageMap, pagePreviouslySearchedValues);
  } else {
    console.warn('Unknown region_type for page:', page_name, 'region_type:', region_type);
  }
}

function restoreRegionInputValuesIfExist(page_name, currentPageMap, pagePreviouslySearchedValues) {
  // If the region is to be restored and is "input boxes" (like on the typeahead), restore here
  const container_id_suffixes = currentPageMap.container_id_suffixes;
  const prefix = currentPageMap.container_prefix;

  // Loop over the suffixes
  for (const suffix of container_id_suffixes) {
    // Check if that suffix has a stored value in pagePreviouslySearchedValues
    if (suffix in pagePreviouslySearchedValues) {
      const inputContainerId = prefix + suffix;
      const inputContainer = document.querySelector('#' + inputContainerId);

      // Get the input element
      const inputElement = inputContainer.querySelector('input[type="text"]');
      if (!inputElement) {
        console.warn('No input element found for region input Id:', inputContainerId);
        continue;
      }

      // Set the value
      const restoreValue = pagePreviouslySearchedValues[suffix];
      inputElement.value = restoreValue;
    }
  }
}

function restoreCheckboxValuesIfExist(page_name, currentPageMap, pagePreviouslySearchedValues) {
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