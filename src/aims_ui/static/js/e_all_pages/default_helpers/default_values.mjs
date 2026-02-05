import {
  getGlobalValues,
} from '/static/js/f_helpers/local_storage_page_helpers.mjs';


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
        'page': 'multiple_address_original',
        'inputObjects': [
        {
          'htmlId': 'limit',
          'persistanceState': true,
          'typeOfInput': 'text',
          'defaultValue': '5',
        },
        {
          'htmlId': 'classificationfilter',
          'persistanceState': true,
          'typeOfInput': 'autosuggest',
          'defaultValue': '',
        },
        {
          'htmlId': 'epoch',
          'persistanceState': true,
          'typeOfInput': 'radio',
          'defaultValue': latestEpochNumber,
        },
        {
          'htmlId': 'historical',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        },
        {
          'htmlId': 'matchthreshold',
          'persistanceState': true,
          'typeOfInput': 'dropdown',
          'defaultValue': '1%',
        },
        {
          'htmlId': 'header_row_export',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true,
        },
        {
          'htmlId': 'eboost',
          'persistanceCheckboxHtmlId': 'multiple-address-match-original-region',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'wboost',
          'persistanceCheckboxHtmlId': 'multiple-address-match-original-region',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'sboost',
          'persistanceCheckboxHtmlId': 'multiple-address-match-original-region',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'nboost',
          'persistanceCheckboxHtmlId': 'multiple-address-match-original-region',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'lboost',
          'persistanceCheckboxHtmlId': 'multiple-address-match-original-region',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'mboost',
          'persistanceCheckboxHtmlId': 'multiple-address-match-original-region',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'jboost',
          'persistanceCheckboxHtmlId': 'multiple-address-match-original-region',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'display-type',
          'typeOfInput': 'radio',
          'defaultValue': 'Download',
          'persistanceState': true,
        },
        {
          'htmlId': 'paf-nag-preference',
          'typeOfInput': 'radio',
          'defaultValue': 'PAF',
          'persistanceState': true,
        },
      ]
    },
    {
      'page': 'multiple_address',
      'inputObjects': [
        {
          'htmlId': 'limitperaddress',
          'persistanceState': true,
          'typeOfInput': 'text',
          'defaultValue': '1',
        },
        {
          'htmlId': 'name',
          'persistanceState': false,
          'typeOfInput': 'text',
          'defaultValue': '',
        },
        {
          'htmlId': 'paf-nag-preference',
          'typeOfInput': 'radio',
          'defaultValue': 'PAF',
          'persistanceState': true,
        },
        {
          'htmlId': 'header_row_export',
          'typeOfInput': 'checkbox',
          'persistanceState': true,
          'defaultValue': true,
        }
      ],
    },
    {
      'page': 'multiple_address_attributes',
      'inputObjects': [
        {
          'htmlId': 'parent_uprn',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        },
        {
          'htmlId': 'latitude',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        },
        {
          'htmlId': 'longitude',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        },
        {
          'htmlId': 'easting',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        },
        {
          'htmlId': 'northing',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        },
        {
          'htmlId': 'classification_code',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        },
        {
          'htmlId': 'lpi_logical_status',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        },
        {
          'htmlId': 'country_code',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        },
        {
          'htmlId': 'formatted_address_nag',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        },
        {
          'htmlId': 'formatted_address_paf',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        },
        {
          'htmlId': 'welsh_formatted_address_nag',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        },
        {
          'htmlId': 'welsh_formatted_address_paf',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        },
      ],
    },
    {
      'page': 'singlesearch', // Page is also the id in the settings table
      'inputObjects': [
        {
          'htmlId': 'input',
          'persistanceState': false,
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
          'persistanceCheckboxHtmlId': 'singlesearch-region',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'wboost',
          'persistanceCheckboxHtmlId': 'singlesearch-region',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'sboost',
          'persistanceCheckboxHtmlId': 'singlesearch-region',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'nboost',
          'persistanceCheckboxHtmlId': 'singlesearch-region',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'lboost',
          'persistanceCheckboxHtmlId': 'singlesearch-region',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'mboost',
          'persistanceCheckboxHtmlId': 'singlesearch-region',
          'persistanceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'jboost',
          'persistanceCheckboxHtmlId': 'singlesearch-region',
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
          'defaultValue': latestEpochNumber,
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
          'htmlId': 'epoch',
          'persistanceState': true,
          'typeOfInput': 'radio',
          'defaultValue': latestEpochNumber,
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
      'page': 'typeahead',
      'inputObjects': [
        {
          'htmlId': 'address',
          'persistanceState': true,
          'typeOfInput': 'text',
          'defaultValue': '',
        },
        {
          'htmlId': 'limit',
          'persistanceState': true,
          'typeOfInput': 'text',
          'defaultValue': '10',
        },
        {
          'htmlId': 'epoch',
          'persistanceState': true,
          'typeOfInput': 'radio',
          'defaultValue': latestEpochNumber,
        },
        // Add a type 'text' for eboost, wboost, sboost, nboost, lboost, mboost, jboost
        {
          'htmlId': 'eboost',
          'persistanceState': true,
          'persistanceCheckboxHtmlId': 'typeahead-region',
          'typeOfInput': 'text',
          'defaultValue': '0',
        },
        {
          'htmlId': 'wboost',
          'persistanceState': true,
          'persistanceCheckboxHtmlId': 'typeahead-region',
          'typeOfInput': 'text',
          'defaultValue': '0',
        },
        {
          'htmlId': 'sboost',
          'persistanceState': true,
          'persistanceCheckboxHtmlId': 'typeahead-region',
          'typeOfInput': 'text',
          'defaultValue': '0',
        },
        {
          'htmlId': 'nboost',
          'persistanceState': true,
          'persistanceCheckboxHtmlId': 'typeahead-region',
          'typeOfInput': 'text',  
          'defaultValue': '0',
        },
        {
          'htmlId': 'lboost',
          'persistanceState': true,
          'persistanceCheckboxHtmlId': 'typeahead-region',
          'typeOfInput': 'text',
          'defaultValue': '0',
        },
        {
          'htmlId': 'mboost',
          'persistanceState': true,
          'persistanceCheckboxHtmlId': 'typeahead-region',
          'typeOfInput': 'text',
          'defaultValue': '0',
        },
        {
          'htmlId': 'jboost',
          'persistanceState': true,
          'persistanceCheckboxHtmlId': 'typeahead-region',
          'typeOfInput': 'text',
          'defaultValue': '0',
        }
      ]
    },
    {
      'page': 'custom_response',
      'persistanceSettingDisabled': true,
      'inputObjects': [
        {
          'htmlId': 'request-type',
          'persistanceState': true,
          'typeOfInput': 'dropdown',
          'defaultValue': 'GET',
        },
        {
          'htmlId': 'url-input',
          'persistanceState': true,
          'typeOfInput': 'autosuggest',
          'defaultValue': '',
        },
        {
          'htmlId': 'response-type',
          'persistanceState': true,
          'typeOfInput': 'radio',
          'defaultValue': 'plaintext',
        },
        {
          'htmlId': 'request-body-text-area',
          'persistanceState': true,
          'typeOfInput': 'text-area',
          'defaultValue': '{}',
        },
        {
          'htmlId': 'post-request-body-style',
          'typeOfInput': 'non-visible',
          'defaultValue': '',
        }
      ]
    },
    {
      'page': 'radiussearch',
      'persistanceSettingDisabled': true,
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
          'typeOfInput': 'non-visible',
          'defaultValue': '12',
        }
      ]
    }
    ],
  };

  return defaultGlobalValues;
}
