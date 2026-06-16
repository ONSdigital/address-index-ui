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
  const titleTextIfNoAddresses = `Your search returned no addresses.`;
  
  if (numberOfAddresses === 0) {
    return titleTextIfNoAddresses;
  }

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

function generateTitle(limitEntered, numberOfAddresses, page_name) {
  // Create title
  const weMatchedTitle = crEl('h2', 'we-matched-addresses-title');

  // Get the text the title should have
  const titleText = getTitleText(limitEntered, numberOfAddresses, page_name);
  // Set the title text and log change
  weMatchedTitle.textContent = titleText;
  console.debug('Title text set to: ' + titleText);

  return weMatchedTitle;
}

function generateSuplimentaryText(limitEntered, numberOfAddresses) {
  // Create supplementary text for 0 matches
  const weMatchedSuplimentaryText = crEl('h3', 'we-matched-addresses-suplimentary-text');

  // Set text for supplementry text for 0 matches
  if (numberOfAddresses === 0) {
    weMatchedSuplimentaryText.textContent = 'Changing parameters such as classification or area may yield more results.';
  }

  return weMatchedSuplimentaryText;
}

function refreshTitleStatus(page_name) {
  // Remove all children of the title container
  const containerForWeMatchedMessage= document.querySelector('#container-for-we-matched-addresses-title');
  while (containerForWeMatchedMessage.firstChild) {
    containerForWeMatchedMessage.removeChild(containerForWeMatchedMessage.firstChild);
  }

  // calculated from the local storage because then it can be restored with no server interaction
  const numberOfAddresses = getNumberOfAddressesMatchedFromLocalStorage(page_name);
  const limitEntered = getLimitEnteredFromLocalStorage(page_name);

  // Create title for addresses if more than 0 have been matched:
  const weMatchedTitle = generateTitle(limitEntered, numberOfAddresses, page_name);
  const weMatchedSuplimentaryText = generateSuplimentaryText(limitEntered, numberOfAddresses);

  // Add the title to the container
  containerForWeMatchedMessage.append(weMatchedTitle, weMatchedSuplimentaryText);
}

export function init(page_name) {
  // Do the initial refresh of the title
  refreshTitleStatus(page_name);

  // Setup an event listener for the custom event 'refreshWeMatchedTitle'
  document.addEventListener('refreshWeMatchedTitle', () => {
    refreshTitleStatus(page_name);
  });
}

