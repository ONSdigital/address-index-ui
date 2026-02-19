import { getPageLocalValues } from "/static/js/f_helpers/local_storage_page_helpers.mjs";
import { crEl } from "/static/js/f_helpers/element_creation.mjs";

function getNumberOfAddressesMatchedFromLocalStorage(page_name) {
  // Get the most recent addresses for this page from local storage
  const localPageValues = getPageLocalValues(page_name);
  const addresses = localPageValues.mostRecentlySearchedAddresses || [];
  const numberOfAddresses = addresses.length;

  return numberOfAddresses;
}

function getLimitEnteredFromLocalStorage(page_name) {
  // Get the most recent addresses for this page from local storage
  const localPageValues = getPageLocalValues(page_name);
  const previouslySearchedValues = localPageValues.pagePreviouslySearchedValues || {};
  const limitEntered = previouslySearchedValues.limit || 1;

  return limitEntered;
}

function returnSingluarOrPluralAddress(numberOfAddresses) {
  if (numberOfAddresses === 1) {
    return 'address';
  }
  return 'addresses';
}

function getTitleText(limitEntered, numberOfAddresses, page_name) {
  const addressOrAddresses = returnSingluarOrPluralAddress(numberOfAddresses);
  const titleTextIfLimitReached = `We matched ${numberOfAddresses} ${addressOrAddresses}, more may exist beyond your limit.`;
  const titleTextIfUnderLimit = `We matched ${numberOfAddresses} ${addressOrAddresses}:`;
  
  if (numberOfAddresses >= limitEntered) {
    // For the UPRN page (or typeahead), we either match one or no addresses. The message should always be single, ignoring limmit
    if (page_name === 'uprn' || page_name === 'typeahead') {
      return titleTextIfUnderLimit;
    }
    return titleTextIfLimitReached;
  } else {
    return titleTextIfUnderLimit;
  }
}

function refreshTitleStatus(page_name) {
  // Remove all children of the title container
  const containerDiv = document.querySelector('#container-for-we-matched-addresses-title');
  while (containerDiv.firstChild) {
    containerDiv.removeChild(containerDiv.firstChild);
  }

  // calculated from the local storage because then it can be restored with no server interaction
  const numberOfAddresses = getNumberOfAddressesMatchedFromLocalStorage(page_name);
  const limitEntered = getLimitEnteredFromLocalStorage(page_name);

  // If there are no addresses, then don't add the title
  if (numberOfAddresses === 0) { return null; }

  // Create the title element
  const weMatchedTitle = crEl('h2', 'we-matched-addresses-title');
  const titleText = getTitleText(limitEntered, numberOfAddresses, page_name);
  weMatchedTitle.textContent = titleText;
  console.log('Title text set to: ' + titleText);

  // Add the title to the container
  containerDiv.append(weMatchedTitle);
}

export function init(page_name) {
  // Do the initial refresh of the title
  refreshTitleStatus(page_name);

  // Setup an event listener for the custom event 'refreshWeMatchedTitle'
  document.addEventListener('refreshWeMatchedTitle', () => {
    refreshTitleStatus(page_name);
  });
}

