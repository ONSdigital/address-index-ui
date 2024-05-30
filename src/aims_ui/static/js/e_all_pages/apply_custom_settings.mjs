import { 
  getAddressTitlePrefference,
  getAdditionalRequestStatus,
} from '/static/js/f_helpers/local_storage_helpers.mjs';

function getMatchTypeDescription(matchType) {
  // Expect 'S' 'M' 'N' for single multiple none
  if (matchType === 'S') {
    return 'S - Single match with Confidence Score above threshold';
  } else if (matchType === 'M') {
    return 'M - Multiple Matches with Confidence Score above threshold';
  } else if (matchType === 'N') {
    return 'N - No matches with Confidence Score above threshold';
  }
}

function getRecommendationCodeDescription(code) {
  if (code === 'A') {
    return 'A - Accept the top result';
  } else if (code === 'I') {
    return 'I - Investigate results';
  }
}

function applyVisibilityOfRequestStatus() {
  const settings = getAdditionalRequestStatus();
  const settingsPanel = document.querySelector('#requestOverviewStatsPanel');
  if (!settingsPanel) {return};
  const values = settingsPanel.getAttribute('valuesofrequestattributes');
  const validJsonString = values.replace(/'/g, '"');
  const jsonObj = JSON.parse(validJsonString);

  let showPanel = false;
  let panelContents = ''; 
  if (settings.match_type === 'true') {
    showPanel = true;
    const pg = document.createElement('p');
    pg.textContent = getMatchTypeDescription(jsonObj.matchType);
    settingsPanel.append(pg);
  }
  if (settings.recommendation_code === 'true') {
    showPanel = true;
    const pg = document.createElement('p');
    pg.textContent = getRecommendationCodeDescription(jsonObj.recommendationCode);
    settingsPanel.append(pg);
  }

  if (showPanel) {
    const pg = document.createElement('p');
    pg.innerHTML = '<em>Request Details</em>';
    settingsPanel.prepend(pg);
    settingsPanel.classList.remove('ons-u-hidden');
  }

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
  console.log('apply_custom_settings loaded');
  const prefference = getAddressTitlePrefference();
  applyTitlePrefference(prefference);
  applyVisibilityOfRequestStatus();
}

window.addEventListener('load', init);


