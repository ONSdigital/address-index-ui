import {
  getGlobalValues,
  setGlobalValues,
} from '/static/js/f_helpers/local_storage_page_helpers.mjs';
import { checkCheckboxById } from './element_manipulation.mjs';

// Setup listeners, handlers and startup for showing additional request info

function updateAdditionalRequestSettingsInGlobalValues(detailKey, isChecked) {
  const globalValues = getGlobalValues();
  const currentDetailSettings = globalValues.additionalRequestDetails || {};

  const updatedSettings = {
    ...currentDetailSettings,
    [detailKey]: isChecked,
  };

  setGlobalValues({ additionalRequestDetails: updatedSettings });
}

export function setupAdditionalRequestSetting() {
  // Get the value of the current additional request details setting
  const globalValues = getGlobalValues();
  const currentDetailSettings = globalValues.additionalRequestDetails || {};

  // Check the appropriate checkboxes
  const matchTypeId = 'additional-request-details-match-type';
  const recommendationCodeId = 'additional-request-details-recommendation-code';
  const tokenisedOutputId = 'additional-request-details-tokenised-output';

  if (currentDetailSettings.match_type === true) {
    checkCheckboxById(matchTypeId);
  } 
  if (currentDetailSettings.recommendation_code === true) {
    checkCheckboxById(recommendationCodeId);
  }
  if (currentDetailSettings.tokenised_output === true) {
    checkCheckboxById(tokenisedOutputId);
  }

  // Add listeners to change the global setting 
  const matchTypeHtmlObject = document.querySelector(`#${matchTypeId}`);
  const recommendationCodeHtmlObject = document.querySelector(`#${recommendationCodeId}`);
  const tokenisedOutputHtmlObject = document.querySelector(`#${tokenisedOutputId}`);

  // When clicked update the global value
  matchTypeHtmlObject.addEventListener('change', () => {
    updateAdditionalRequestSettingsInGlobalValues('match_type', matchTypeHtmlObject.checked);
  });

  recommendationCodeHtmlObject.addEventListener('change', () => {
    updateAdditionalRequestSettingsInGlobalValues('recommendation_code', recommendationCodeHtmlObject.checked);
  });

  tokenisedOutputHtmlObject.addEventListener('change', () => {
    updateAdditionalRequestSettingsInGlobalValues('tokenised_output', tokenisedOutputHtmlObject.checked);
  });
}