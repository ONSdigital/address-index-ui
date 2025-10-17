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

function getTitleText(numberOfAddresses) {
  const limitEntered = getLimitEnteredFromLocalStorage('radiussearch');

  const titleTextIfLimitReached = `We matched ${numberOfAddresses} addresses, more may exist beyond your limit.`;
  const titleTextIfUnderLimit = `We matched ${numberOfAddresses} addresses:`;

  if (numberOfAddresses >= limitEntered) {
    return titleTextIfLimitReached;
  } else {
    return titleTextIfUnderLimit;
  }
}

export function generateMatchedMessage(page_name) {
  // calculated from the local storage because then it can be restored with no server inteaction
  const numberOfAddresses = getNumberOfAddressesMatchedFromLocalStorage(page_name);

  // If there are no addresses, then don't add the title
  if (numberOfAddresses === 0) { return null; }

  // Create the title element
  const weMatchedTitle = crEl('h2', 'we-matched-addresses-title');
  weMatchedTitle.textContent = getTitleText(numberOfAddresses);

  // Add the title to the container
  const containerDiv = document.querySelector('#container-for-we-matched-addresses-title');
  containerDiv.append(weMatchedTitle);
}

