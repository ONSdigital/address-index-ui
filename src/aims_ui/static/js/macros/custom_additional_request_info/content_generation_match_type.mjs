import { crEl } from '/static/js/f_helpers/element_creation.mjs';

function getMatchTypeDescription(matchType) {
  // Expect 'S' 'M' 'N' for single multiple none
  if (matchType === 'S') {
    return 'S - Single match with Confidence Score above threshold';
  } else if (matchType === 'M') {
    return 'M - Multiple Matches with Confidence Score above threshold';
  } else if (matchType === 'N') {
    return 'N - No matches with Confidence Score above threshold';
  }
  return matchType;
}

export function generatePanelContentForMatchType(responseAttributes) {
  // Given the response attributes, generate the content for match type
  const matchType = responseAttributes.matchType || 'N/A';
  const matchTypeDescription = getMatchTypeDescription(matchType);

  // Create a container, title and description elements
  const matchTypeContainer = crEl('div', 'match-type-paragraph-container');
  const matchTypeTitle= crEl('em', 'match-type-paragraph-title');
  const matchTypeText = crEl('p', 'match-type-paragraph-text');

  // Set the content of elements and nest them
  matchTypeTitle.textContent = 'Match Type: ';
  matchTypeText.textContent = matchTypeDescription;
  matchTypeContainer.append(matchTypeTitle, matchTypeText);

  return matchTypeContainer;
}

