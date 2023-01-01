import { 
  getAddressTitlePrefference,
  setDefaultTitleChoice
} from './local_storage_helpers.mjs';

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
    return 'Default Formatting'
  } else if (prefference === 'paf') {
    return 'PAF Formatting'
  } else if (prefference === 'nag') {
    return 'NAG Formatting'
  }
}

function hideUnselectedTitles(prefference) {
  const addressTitles = document.querySelectorAll('.address-titles');
  // Remove all titles if they're not the chosen one
  const chosenTitleId = getChosenTitleId(prefference);
  for (const title of addressTitles) {
    if (title.id === chosenTitleId) {
      if (title.textContent !== '') {
        title.hidden = false;
        title.textContent = 
          title.textContent 
          + ' (' + getUserFriendlyPrefference(prefference) + ')';
      } 
    }
  }
}


function init() {
  const prefference = getAddressTitlePrefference();
  hideUnselectedTitles(prefference);
  setDefaultTitleChoice();
}

window.addEventListener('load', init);


