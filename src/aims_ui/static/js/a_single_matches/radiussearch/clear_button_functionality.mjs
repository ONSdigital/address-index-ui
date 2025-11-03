// Manage the clear button functionality on the radius search page

import { syncPageWithCurrentInputs } from '/static/js/a_single_matches/radiussearch/interactive_map/map_setup.mjs';
import { getDefaultValuesForPage } from '/static/js/e_all_pages/setup_defaults.mjs';
import { setPageLocalValues } from '/static/js/f_helpers/local_storage_page_helpers.mjs';

function makeUprnResultsInvisible() {
  const uprnResultContainer = document.querySelector('#complete-container-for-uprnLookupPanelInfo');
  const uprnErrorContainer = document.querySelector('#complete-container-for-uprnLookupPanelError');

  if (uprnResultContainer) {
    uprnResultContainer.classList.add('invisible');
  }
  if (uprnErrorContainer) {
    uprnErrorContainer.classList.add('invisible');
  }

}

function resetValuesToDefaults() {
  // Get the default values for radiussearch
  const defaultValues = getDefaultValuesForPage('radiussearch');

  // Get a handle on the search inputs
  const searchInputsContainer = document.querySelector('#full-match-form-container')

  // Loop over each default value and id pair and set the input value
  for (const [id, defaultValue] of Object.entries(defaultValues)) {
    const inputElement = searchInputsContainer.querySelector('#' + id);
    if (inputElement) {
      inputElement.value = defaultValue;
    }
  }

  // Make the UPRN result invisible
  makeUprnResultsInvisible();

  // Set the 'page previously searched values' in local storage to the default values
  setPageLocalValues('radiussearch', { pagePreviouslySearchedValues: defaultValues });

  // Clear the 'most recently searched addresses' in local storage
  setPageLocalValues('radiussearch', { mostRecentlySearchedAddresses: [] });

  // Now trigger updates to the map and to search results
  syncPageWithCurrentInputs();
}

export function setupClearButtonFunctionality() {
  console.log('Setting up clear button functionality');
  // Get a handle on the clear button
  const clearButton = document.querySelector('#clear-form-data-button-id');

  if (clearButton) {
    clearButton.addEventListener('click', (e) => {
      e.preventDefault();
      resetValuesToDefaults();
    });
  }
}