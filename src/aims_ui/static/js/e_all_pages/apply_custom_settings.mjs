import {
  getAddressTitlePreference,
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
  if (!settingsPanel) {
    return;
  }
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
    pg.textContent = getRecommendationCodeDescription(
      jsonObj.recommendationCode
    );
    settingsPanel.append(pg);
  }

  if (showPanel) {
    const pg = document.createElement('p');
    pg.innerHTML = '<em>Request Details</em>';
    settingsPanel.prepend(pg);
    settingsPanel.classList.remove('ons-u-hidden');
  }
}

function getChosenTitleId(preference) {
  // Convert the preference into HTML Ids
  if (preference === 'paf') {
    return 'formattedAddressPaf';
  } else if (preference === 'nag') {
    return 'formattedAddressNag';
  }
  return 'formattedAddress';
}

function getUserFriendlyPreference(preference) {
  if (preference === 'def') {
    return '';
  } else if (preference === 'paf') {
    return ' (PAF Formatting)';
  } else if (preference === 'nag') {
    return ' (NAG Formatting)';
  }
}

function getAddressTitle(preference, addressTitles) {
  const chosenTitleId = getChosenTitleId(preference);

  // Given 3 titles from a card, loop through and find the one that matches the preference
  for (const title of addressTitles) {
    if (title.id === chosenTitleId) {
      return title;
    }
  }
}

function applyTitlePreference(preference) {
  // Select every result short form
  const resultCards = document.querySelectorAll('.result-short-form');

  // For every result card, check if the title preference is blank.
  // If it is blank, show the default one, otherwise show the prefered one
  for (const card of resultCards) {
    const currentTitles = card.querySelectorAll('.address-titles');
    const preferedTitle = getAddressTitle(preference, currentTitles);
    const preferedTitleTextContent = preferedTitle.textContent.replace(
      /\s+/g,
      ''
    );

    if (preferedTitleTextContent === '') {
      // Blank prefered title? Show the default format of title
      const backupTitle = getAddressTitle('def', currentTitles);
      backupTitle.hidden = false;
      backupTitle.textContent =
        backupTitle.textContent + ' (Default Formatting)';
    } else {
      preferedTitle.hidden = false;
      preferedTitle.textContent =
        preferedTitle.textContent + getUserFriendlyPreference(preference);
    }
  }
}

function init() {
  console.log('apply_custom_settings loaded');
  const preference = getAddressTitlePreference();
  applyTitlePreference(preference);
  applyVisibilityOfRequestStatus();
}

window.addEventListener('load', init);
