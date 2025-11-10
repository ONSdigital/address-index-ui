import { getPageLocalValues, setPageLocalValues } from "/static/js/f_helpers/local_storage_page_helpers.mjs";

export function setupClearButton(page_name) {
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

    // Dispatch custom event to refresh the address info cards
    const refreshAddressInfoCardsEvent = new CustomEvent('refreshAddressInfoCards', {
      bubbles: true
    });

    const refreshDownloadButtonEvent = new CustomEvent('refreshDownloadButton', {
      bubbles: true
    });

    clearButton.dispatchEvent(refreshAddressInfoCardsEvent);
    clearButton.dispatchEvent(refreshDownloadButtonEvent);
  });
}