// scripts to make the templated address info work

import { getPageLocalValues, getGlobalValues } from '/static/js/f_helpers/local_storage_page_helpers.mjs';
import { applyVisibilityOfRequestStatus } from './panel_visibility.mjs';
import { generatePanelContentForMatchType } from './content_generation_match_type.mjs';
import { generatePanelContentForRecommendationCode } from './content_generation_recommendation_code.mjs';
import { getPanelContentForTokenisedOutput } from './content_generation_parser_breakdown.mjs';

function generatePanelContents(enabledRequestDetails, page_name) {
  // Firstly get a handle on the container that will have content added to it
  const contentContainer = document.querySelector('#requestOverviewStatsPanel');
  const localValuesForPage = getPageLocalValues(page_name);
  const responseAttributes = localValuesForPage.responseAttributes || {};

  // Now we add match type if it's enabled
  if (enabledRequestDetails.match_type === true) {
    const matchTypeContentContainer = document.createElement('div');
    matchTypeContentContainer.append(generatePanelContentForMatchType(responseAttributes));
    contentContainer.append(matchTypeContentContainer);
  }

  // Now we add recommendation code if it's enabled
  if (enabledRequestDetails.recommendation_code === true) {
    const recommendationCodeParagraph = generatePanelContentForRecommendationCode(responseAttributes);
    contentContainer.append(recommendationCodeParagraph);
  }

  // Now we add tokenised output if it's enabled
  if (enabledRequestDetails.tokenised_output === true) {
    const tokenisedOutput = getPanelContentForTokenisedOutput(responseAttributes);
    contentContainer.append(tokenisedOutput);
  }
}

export function init(page_name) {
  console.log('Initialising Additional Request Info component');

  // Get the object with true/false for each detail
  const globalValues = getGlobalValues();
  const enabledRequestDetails = globalValues.additionalRequestDetails || {};

  // Now we want to generate the panel contents based on the settings
  generatePanelContents(enabledRequestDetails, page_name);

  // Last thing we do is make it visible if needed
  applyVisibilityOfRequestStatus(enabledRequestDetails);
}