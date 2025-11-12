import {
  getAdditionalRequestStatus,
} from '../f_helpers/local_storage_helpers.mjs';

export function getMatchTypeDescription(matchType) {
  // Expect 'S' 'M' 'N' for single multiple none
  if (matchType === 'S') {
    return 'S - Single match with Confidence Score above threshold';
  } else if (matchType === 'M') {
    return 'M - Multiple Matches with Confidence Score above threshold';
  } else if (matchType === 'N') {
    return 'N - No matches with Confidence Score above threshold';
  }
}

export function getRecommendationCodeDescription(code) {
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

  const tokenisedOutputValues = settingsPanel.getAttribute('tokenisedOutput');
  const tokenisedOutputString = tokenisedOutputValues.replace(/'/g, '"');
  const tokenisedOutputJson = JSON.parse(tokenisedOutputString);

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
  if (settings.tokenised_output === 'true') {
    showPanel = true;

    // Now create the "title" and 'p' elements to break down the tokens
    const titleForTokens = document.createElement('p');
    const emphaisedTitle = document.createElement('em');
    emphaisedTitle.textContent = 'Breakdown from Address Parser:';
    titleForTokens.append(emphaisedTitle);
    settingsPanel.append(titleForTokens);

    // For each of the tokens identified by the parser, append a 'p' element containing the token
    for (const key in tokenisedOutputJson) {
      const pg = document.createElement('p');
      pg.textContent = `${key}: ${tokenisedOutputJson[key]}`;
      settingsPanel.append(pg);
    }
  }

  if (showPanel) {
    // By default the panel is hidden, this removes the hidden class if the above criteria are met
    const pg = document.createElement('p');
    pg.innerHTML = '<em>Request Details</em>';
    settingsPanel.prepend(pg);
    settingsPanel.classList.remove('ons-u-hidden');
  }
}

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
  applyVisibilityOfRequestStatus();
}

window.addEventListener('load', init);
