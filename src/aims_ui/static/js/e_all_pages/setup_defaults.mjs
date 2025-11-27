import {
  getGlobalValues,
  setGlobalValues,
} from '/static/js/f_helpers/local_storage_page_helpers.mjs';

export function getDefaultValuesForPage(page_name) {
  const defaultValues = {
    'radiussearch': {
      'lat': 50.73548,
      'lon': -3.5332105,
      'zoom': 8,
      'rangekm': '10',
      'limit': '50',
      'classificationfilter': '',
      'uprn': '',
      'input': '',
    }
  };

  if (page_name in defaultValues) {
    return defaultValues[page_name];
  }

  return {};
}

export function getDefaultGlobalValues() {
  // Values should be GLOBAL if they're accessed across multiple pages

  const defaultGlobalValues = {

    // Default download format for single searches
    'singleJobDownloadFormat': 'csv',

    // Setup the attributes to include in downloads by default it will be everything
    'singleJobDownloadAttributeInclusion': 'all',

    // Setup the attribute to flag showing older jobs on the large bulk-matching pages
    'showOlderJobsInBulkMatchingPage': false,

    // Setup the default values for Additional Request Details
    'additionalRequestDetails': {
      match_type: true,
      recommendation_code: true,
      tokenised_output: false,
    },

    // Default address attributes to show (based on original requirements)
    'favouriteAddressAttributes': [
      'uprn',
      'parentUprn',
      'classificationCode',
      'classificationCodeList',
      'formattedConfidenceScore',
      'nagLocalCustodianName',
    ]
  };
  return defaultGlobalValues;
}

export function setupDefaultGlobalValues() {
  // Set default values for global values if they don't already exist
  const currentGlobalValues = getGlobalValues();

  const defaultGlobalValues = getDefaultGlobalValues();

  const updatedValues = { ...defaultGlobalValues, ...currentGlobalValues };

  setGlobalValues(updatedValues);
}

