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
    },
    'singlesearch': {
      'input': '',
      'classificationfilter': '',
      'epoch': '',
      'minimummatch': '1%',
      'limit': '20',
      'includehistorical': false,
    },
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

    // Default type of title the address cards should have
    'addressCardTitleType': 'default',

    // Setup default column widths
    'columnWidths': {
      'space_col_1': '1',
      'content_col_2': '4',
      'space_col_3': '1',
      'content_col_4': '5',
    },

    // Setup persistance settings for pages
    'persistanceSettings': [
      {
      'page': 'singlesearch', // Page is also the id in the settings table
      'input_persistance_settings': [
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
          'htmlId': 'region',
          'persistanceState': true,
          'typeOfInput': 'checkboxes',
          'checkboxHtmlIds': ['eboost', 'wboost', 'sboost', 'nboost', 'lboost', 'mboost', 'jboost'],
          'defaultValue': true, // "Checkboxes" affect all boxes
        },
        {
          'htmlId': 'epoch',
          'persistanceState': true,
          'typeOfInput': 'radio',
        },
        {
          'htmlId': 'matchthreshold',
          'persistanceState': true,
          'typeOfInput': 'dropdown',
          'defaultValue': '1%',
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
      'input_persistance_settings': [
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
      'input_persistance_settings': [
        {
          'htmlId': 'input',
          'persistanceState': true,
          'typeOfInput': ''
        },
        {
          'htmlId': 'classification',
          'persistanceState': true,
          'typeOfInput': ''
        },
        {
          'htmlId': 'epoch',
          'persistanceState': true,
          'typeOfInput': ''
        },
        {
          'htmlId': 'limit',
          'persistanceState': true,
          'typeOfInput': ''
        },
        {
          'htmlId': 'includehistorical',
          'persistanceState': true,
          'typeOfInput': ''
        }
      ]
    },
    {
      'page': 'typeahead',
      'input_persistance_settings': [
        {
          'htmlId': 'region',
          'persistanceState': true,
          'typeOfInput': ''
        },
        {
          'htmlId': 'epoch',
          'persistanceState': true,
          'typeOfInput': ''
        },
        {
          'htmlId': 'limit',
          'persistanceState': true,
          'typeOfInput': ''
        }
      ]
    },
    {
      'page': 'radiussearch',
      'input_persistance_settings': [
        {
          'htmlId': 'lat',
          'persistanceState': true,
          'typeOfInput': ''
        },
        {
          'htmlId': 'lon',
          'persistanceState': true,
          'typeOfInput': ''
        },
        {
          'htmlId': 'rangekm',
          'persistanceState': true,
          'typeOfInput': ''
        },
        {
          'htmlId': 'input',
          'persistanceState': true,
          'typeOfInput': ''
        },
        {
          'htmlId': 'classificationfilter',
          'persistanceState': true,
          'typeOfInput': ''
        },
        {
          'htmlId': 'limit',
          'persistanceState': true,
          'typeOfInput': ''
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

