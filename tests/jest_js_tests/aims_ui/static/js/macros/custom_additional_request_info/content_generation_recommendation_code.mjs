import { crEl } from '/static/js/f_helpers/element_creation.mjs';

export function getRecommendationCodeDescription(code) {
  if (code === 'A') {
    return 'A - Accept the top result';
  } else if (code === 'I') {
    return 'I - Investigate results';
  }
}

export function generatePanelContentForRecommendationCode(responseAttributes) {
  // Given the response attributes, generate the content for recommendation code 
  const recommendationCode = responseAttributes.recommendationCode || 'N/A';
  const recommendationCodeDescription = getRecommendationCodeDescription(recommendationCode);

  // Create a container, title and description elements
  const recommendationContainer = crEl('div', 'recommendation-paragraph-container');
  const recommendationTitle= crEl('em', 'recommendation-paragraph-title');
  const recommendationText = crEl('p', 'recommendation-paragraph-text');

   // Set the content of elements and nest them
  recommendationTitle.textContent = 'Recommendation Code: ';
  recommendationText.textContent = recommendationCodeDescription;
  recommendationContainer.append(recommendationTitle, recommendationText);

  return recommendationContainer;
 }

