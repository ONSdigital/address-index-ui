import { getGlobalValues } from "../f_helpers/local_storage_page_helpers.mjs";
import { restoreConfidenceScoreAndUnderlyingScore } from "./populate_confidence_scores.mjs";

function updateConfidenceScores() {
  // Get the most recent addresses from local storage, default to blank array if undefined
  const mostRecentlySearchedAddresses = getGlobalValues().mostRecentlySearchedAddresses || [];

  restoreConfidenceScoreAndUnderlyingScore(mostRecentlySearchedAddresses);

}

function init() {
  // Firstly update confidence scores
  updateConfidenceScores();

//  replaceOverviewTableConfidenceScoreValues();
  console.log('address_info init loaded');
}

window.addEventListener('load', init);