export function applyVisibilityOfRequestStatus(additionalRequestDetails) {

  // Check each detail - if any are true, make the panel visible 
  const settingsPanel = document.querySelector('#requestOverviewStatsPanel');
  if (!settingsPanel) {
    return;
  }

  let showPanel = false;

  for (const [key, value] of Object.entries(additionalRequestDetails)) {
    if (value === true) {
      showPanel = true;
      break;
    }
  }
  
  if (showPanel) { 
    settingsPanel.classList.remove('ons-u-hidden');
  }
}


function neverCallMe() {
  const tokenisedOutputValues = settingsPanel.getAttribute('tokenisedOutput');
  const tokenisedOutputString = tokenisedOutputValues.replace(/'/g, '"');
  const tokenisedOutputJson = JSON.parse(tokenisedOutputString);

  let showPanel = false;
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

