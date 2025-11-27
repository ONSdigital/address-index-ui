export function getChosenTitleId(preference) {
  // Convert the preference into HTML Ids
  if (preference === 'paf') {
    return 'formattedAddressPaf';
  } else if (preference === 'nag') {
    return 'formattedAddressNag';
  }
  return 'formattedAddress';
}

export function getUserFriendlyPreference(preference) {
  if (preference === 'def') {
    return '';
  } else if (preference === 'paf') {
    return ' (PAF Formatting)';
  } else if (preference === 'nag') {
    return ' (NAG Formatting)';
  }
}

export function getAddressTitle(preference, addressTitles) {
  const chosenTitleId = getChosenTitleId(preference);

  // Given 3 titles from a card, loop through and find the one that matches the preference
  for (const title of addressTitles) {
    if (title.id === chosenTitleId) {
      return title;
    }
  }
}

function init() {
  console.log('apply_custom_settings loaded');
}

window.addEventListener('load', init);
