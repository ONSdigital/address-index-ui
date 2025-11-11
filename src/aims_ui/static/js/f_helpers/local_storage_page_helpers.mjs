import { getDefaultFavourites } from '/static/js/e_all_pages/setup_defaults.mjs';

// A page should only request the global attributes stored in 
// localStorage.global_values
// or from it's own named pages:
// localStorage.local_page_values.page_name

// This file is to setup and manage local storage in the structure below:
// localStorage.local_page_values = {  "page_name": {"value": "key"}  }


// Given the name of a page, retrieve its values as an object
export function getPageLocalValues(page_name) {
  let allPageValues = getAllPageValues();

  // Access property directly, fallback to {}
  const singlePageValues = allPageValues[page_name] || {};

  return singlePageValues;
}

// Given values to save/update, stringify and save them to local storage
export function setPageLocalValues(page_name, page_values) {
  // Firstly, get all of the values for all the pages
  const allPageValues = getAllPageValues();

  // Compare the new values, update/add them to "allPageValues"
  allPageValues[page_name] = { ...(allPageValues[page_name] || {}), ...page_values };

  // Stringify and save the updated allPageValues back to local storage
  const stringAllPageValues = JSON.stringify(allPageValues);
  localStorage.setItem('local_page_values', stringAllPageValues);
}

// Get local_page_values, default to a blank object if undefined
function getAllPageValues() {
  let allPageValues = localStorage.getItem('local_page_values');

  if (!allPageValues) {
    allPageValues = '{}';
  }
  allPageValues = JSON.parse(allPageValues);

  return allPageValues;
}

// Get global values, default to a blank object if undefined
export function getGlobalValues() {
  let globalValues = localStorage.getItem('global_values');
  if (!globalValues) {
    globalValues = '{}';
  }
  globalValues = JSON.parse(globalValues);
  return globalValues;
}

// Set global values, merging with existing values 
// setGlobalValues({'new_key': 'new_value'}) or
// setGlobalValues({'existing_key': 'new_value'})
export function setGlobalValues(newValues) {
  // Get the current values
  const currentValues = getGlobalValues();

  // Merge with newValues provided in the format { key: value, ...}
  const updatedValues = { ...currentValues, ...newValues };

  localStorage.setItem('global_values', JSON.stringify(updatedValues));
}

export function getFavouritesFromLocalStorage() {
  const globalValues = getGlobalValues();
  const favourites = globalValues.favouriteAddressAttributes || getDefaultFavourites();
  return favourites;
}
