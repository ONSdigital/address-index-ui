import { getPageLocalValues, setPageLocalValues } from "/static/js/f_helpers/local_storage_page_helpers.mjs";
import { getDefaultValuesForPage } from "/static/js/e_all_pages/default_helpers/setup_defaults.mjs";

function resetInputFiltersToDefaultState(page_name) {
  // Get default input state and values for this page
  const defaultValuesForPage = getDefaultValuesForPage(page_name);

  // Set the default values into local storage, then trigger a 'restore' from ls
  const pageLocalValues = getPageLocalValues(page_name);
  pageLocalValues.pagePreviouslySearchedValues = defaultValuesForPage;
  setPageLocalValues(page_name, pageLocalValues);
}

export function init(page_name) {
  // Get a handle on the clear button
  const clearButton = document.querySelector('#clear-form-data-button-id');

  // Add the action to reset the 'page previously searched values' in local storage 
  clearButton.addEventListener('click', (event) => {

    // Prevent default action of visiting a link
    event.preventDefault();

    // Remove the "mostRecentlySearchedAddresses" for this page
    const localValues = getPageLocalValues(page_name);
    localValues.mostRecentlySearchedAddresses = [];
    setPageLocalValues(page_name, localValues);

    // Reset the input filters to default values
    resetInputFiltersToDefaultState(page_name);

    // Define new event to refresh the address info cards
    const refreshAddressInfoCardsEvent = new CustomEvent('refreshAddressInfoCards', {
      bubbles: true
    });

    // Define new event to refresh the download button visiblity/state
    const refreshDownloadButtonEvent = new CustomEvent('refreshDownloadButton', {
      bubbles: true
    });

    // Define new event to reset the input filters to the default values
    const resetInputFiltersEvent = new CustomEvent('refreshInputFiltersFromLocalStorage', {
      detail: page_name,
      bubbles: true
    });

    // Define new event to refresh the "we matched" title
    const refreshWeMatchedTitleEvent = new CustomEvent('refreshWeMatchedTitle', {
      detail: page_name,
      bubbles: true
    });



    // Dispatch the events to refresh address cards, download button and reset the input filters
    console.debug('Dispatching the refresh events from clear button');
    clearButton.dispatchEvent(refreshAddressInfoCardsEvent);
    clearButton.dispatchEvent(refreshDownloadButtonEvent);
    clearButton.dispatchEvent(resetInputFiltersEvent);
    clearButton.dispatchEvent(refreshWeMatchedTitleEvent);
  });
}