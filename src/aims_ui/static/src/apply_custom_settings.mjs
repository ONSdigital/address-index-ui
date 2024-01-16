import { 
  getAddressTitlePrefference,
  getAdditionalRequestStatus,
} from './local_storage_helpers.mjs';

function applyVisibilityOfRequestStatus() {
  const settings = getAdditionalRequestStatus();
}

function getChosenTitleId(prefference) {
  // Convert the prefference into HTML Ids
  if (prefference === 'paf') {
    return 'formattedAddressPaf'
  } else if (prefference === 'nag') {
    return 'formattedAddressNag'
  } 
  return 'formattedAddress'
}

function getUserFriendlyPrefference(prefference) {
  if (prefference === 'def') {
    return ''
  } else if (prefference === 'paf') {
    return ' (PAF Formatting)'
  } else if (prefference === 'nag') {
    return ' (NAG Formatting)'
  }
}

function getAddressTitle(prefference, addressTitles) {
  const chosenTitleId = getChosenTitleId(prefference);

  // Given 3 titles from a card, loop through and find the one that matches the prefference
  for (const title of addressTitles) {
    if (title.id === chosenTitleId) {
      return title
    }
  }
}

function applyTitlePrefference(prefference) {
  // Select every result short form
  const resultCards = document.querySelectorAll('.result-short-form');
  
  // For every result card, check if the title prefference is blank.
  // If it is blank, show the default one, otherwise show the preffered one
  for (const card of resultCards) {
    const currentTitles = card.querySelectorAll('.address-titles');
    const prefferedTitle = getAddressTitle(prefference, currentTitles);
    const prefferedTitleTextContent = prefferedTitle.textContent.replace(/\s+/g, '');
    
    if (prefferedTitleTextContent === '') {
      // Blank preffered title? Show the default format of title
      const backupTitle = getAddressTitle('def', currentTitles);
      backupTitle.hidden = false;
      backupTitle.textContent = backupTitle.textContent + ' (Default Formatting)';
    } else {
      prefferedTitle.hidden = false;
      prefferedTitle.textContent = prefferedTitle.textContent + getUserFriendlyPrefference(prefference) ;
    }
  }
}

function init() {
  const prefference = getAddressTitlePrefference();
  applyTitlePrefference(prefference);
  applyVisibilityOfRequestStatus();
}

window.addEventListener('load', init);


