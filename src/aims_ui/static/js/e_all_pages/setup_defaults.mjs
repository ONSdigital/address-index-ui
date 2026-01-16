import {
  getGlobalValues,
  setGlobalValues,
} from '/static/js/f_helpers/local_storage_page_helpers.mjs';

export function getDefaultValuesForPage(page_name) {
  // Return a value/key pair object for 'htmlid': 'defaultValue' for a page 

  const pageInputObjects = getDefaultInputObjectsForPage(page_name);
  const defaultValues = {};

  // Loop over each input object, extract default value and htmlId
  if (pageInputObjects.inputObjects) {
    for (const inputObject of pageInputObjects.inputObjects) {
      if (inputObject.defaultValue !== undefined) {
        defaultValues[inputObject.htmlId] = inputObject.defaultValue;
      }
    }
  } else {
    console.warn(`No input objects found for page: ${page_name}`);
  }

  return defaultValues;
}

export function getDefaultInputObjectsForPage(page_name) {

  const globalValues = getGlobalValues();
  const inputSettings = globalValues.inputSettings || [];

  for (const pageSettings of inputSettings) {
    // Loop over each pagee's setting object
    if (pageSettings.page === page_name) {
      return pageSettings;
    }
  }

  console.warn(`No default input settings found for page: ${page_name}`);
  return {};
}

function getLatestEpochNumber() {
  const globalValues = getGlobalValues();
  return globalValues['latestEpochNumber'] || '';
}

export function getDefaultGlobalValues() {
  // Values should be GLOBAL if they're accessed across multiple pages

  // Get the current Epoch Number from global values
  const latestEpochNumber = getLatestEpochNumber();

  const defaultGlobalValues = {

    // Default download format for single searches
    'singleJobDownloadFormat': 'csv',

    // Setup the attributes to include in downloads by default it will be everything
    'singleJobDownloadAttributeInclusion': 'all',

    // Setup the attribute to flag showing older jobs on the large bulk-matching pages
    'showOlderJobsInBulkMatchingPage': false,

    // Default type of title the address cards should have
    'addressCardTitleType': 'default',

    // Setup default column widths
    'columnWidths': {
      'space_col_1': '1',
      'content_col_2': '4',
      'space_col_3': '1',
      'content_col_4': '5',
    },

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
    ],

    // Setup input settings for pages, including default persistance, 
    // default values, types of input etc.
    'inputSettings': [
      {
      'page': 'singlesearch', // Page is also the id in the settings table
      'inputObjects': [
        {
          'htmlId': 'input',
          'persistanceState': true,
          'typeOfInput': 'text',
          'defaultValue': '',
        },
        {
          'htmlId': 'classificationfilter',
          'persistanceState': true,
          'typeOfInput': 'autosuggest',
          'defaultValue': '',
        },
        {
          'htmlId': 'eboost',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'wboost',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'sboost',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'nboost',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'lboost',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'mboost',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'jboost',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'epoch',
          'persistanceState': true,
          'typeOfInput': 'radio',
          'defaultValue': latestEpochNumber,
        },
        {
          'htmlId': 'matchthreshold',
          'persistanceState': true,
          'typeOfInput': 'dropdown',
          'defaultValue': '5%',
        },
        {
          'htmlId': 'limit',
          'persistanceState': true,
          'typeOfInput': 'text',
          'defaultValue': '20',
        },
        {
          'htmlId': 'historical',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        }
      ]
    },
    {
      'page': 'uprn',
      'inputObjects': [
        {
          'htmlId': 'uprn',
          'persistanceState': true,
          'typeOfInput': 'text',
          'defaultValue': '',
        },
        {
          'htmlId': 'epoch',
          'persistanceState': true,
          'typeOfInput': 'radio',
        },
        {
          'htmlId': 'historical',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        }
      ]
    },
    {
      'page': 'postcode',
      'inputObjects': [
        {
          'htmlId': 'postcode',
          'persistanceState': true,
          'typeOfInput': 'text'
        },
        {
          'htmlId': 'classificationfilter',
          'persistanceState': true,
          'typeOfInput': 'autosuggest'
        },
        {
          'htmlId': 'epoch',
          'persistanceState': true,
          'typeOfInput': 'radio'
        },
        {
          'htmlId': 'limit',
          'persistanceState': true,
          'typeOfInput': 'text'
        },
        {
          'htmlId': 'historical',
          'persistanceState': true,
          'typeOfInput': 'checkbox'
        }
      ]
    },
    {
      'page': 'typeahead',
      'inputObjects': [
        {
          'htmlId': 'address',
          'persistanceState': true,
          'typeOfInput': 'text'
        },
        {
          'htmlId': 'limit',
          'persistanceState': true,
          'typeOfInput': 'text'
        },
        {
          'htmlId': 'epoch',
          'persistanceState': true,
          'typeOfInput': 'radio',
        },
        // Add a type 'text' for eboost, wboost, sboost, nboost, lboost, mboost, jboost
        {
          'htmlId': 'eboost',
          'persistanceState': true,
          'typeOfInput': 'text',
        },
        {
          'htmlId': 'wboost',
          'persistanceState': true,
          'typeOfInput': 'text',
        },
        {
          'htmlId': 'sboost',
          'persistanceState': true,
          'typeOfInput': 'text',
        },
        {
          'htmlId': 'nboost',
          'persistanceState': true,
          'typeOfInput': 'text',  
        },
        {
          'htmlId': 'lboost',
          'persistanceState': true,
          'typeOfInput': 'text',
        },
        {
          'htmlId': 'mboost',
          'persistanceState': true,
          'typeOfInput': 'text',
        },
        {
          'htmlId': 'jboost',
          'persistanceState': true,
          'typeOfInput': 'text',
        }
      ]
    },
    {
      'page': 'radiussearch',
      'inputObjects': [
        {
          'htmlId': 'lat',
          'persistanceState': true,
          'typeOfInput': 'text',
          'defaultValue': '50.73548',
        },
        {
          'htmlId': 'lon',
          'persistanceState': true,
          'typeOfInput': 'text',
          'defaultValue': '-3.5332105',
        },
        {
          'htmlId': 'rangekm',
          'persistanceState': true,
          'typeOfInput': 'text',
          'defaultValue': '10',
        },
        {
          'htmlId': 'input',
          'persistanceState': true,
          'typeOfInput': 'text',
          'defaultValue': '',
        },
        {
          'htmlId': 'uprn',
          'persistanceState': true,
          'typeOfInput': 'text',
          'defaultValue': '',
        },
        {
          'htmlId': 'classificationfilter',
          'persistanceState': true,
          'typeOfInput': 'autosuggest',
          'defaultValue': '',
        },
        {
          'htmlId': 'limit',
          'persistanceState': true,
          'typeOfInput': 'text',
          'defaultValue': '10',
        },
        {  
          'htmlId': 'zoom',
          'defaultValue': '12',
          'typeOfInput': 'non-visible',
        }
      ]
    }
    ],
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

