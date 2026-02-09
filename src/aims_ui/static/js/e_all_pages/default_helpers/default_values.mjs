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

    // Setup input settings for pages, including default persistence, 
    // default values, types of input etc.
    'inputSettings': [
      {
        'page': 'multiple_address_original',
        'persistenceSettingDisabled': true,
        'inputObjects': [
        {
          'htmlId': 'limit',
          'persistenceState': true,
          'typeOfInput': 'text',
          'defaultValue': '5',
        },
        {
          'htmlId': 'classificationfilter',
          'persistenceState': true,
          'typeOfInput': 'autosuggest',
          'defaultValue': '',
        },
        {
          'htmlId': 'epoch',
          'persistenceState': true,
          'typeOfInput': 'radio',
          'defaultValue': latestEpochNumber,
        },
        {
          'htmlId': 'historical',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        },
        {
          'htmlId': 'matchthreshold',
          'persistenceState': true,
          'typeOfInput': 'dropdown',
          'defaultValue': '1%',
        },
        {
          'htmlId': 'header_row_export',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true,
        },
        {
          'htmlId': 'eboost',
          'persistenceCheckboxHtmlId': 'multiple-address-match-original-region',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'wboost',
          'persistenceCheckboxHtmlId': 'multiple-address-match-original-region',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'sboost',
          'persistenceCheckboxHtmlId': 'multiple-address-match-original-region',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'nboost',
          'persistenceCheckboxHtmlId': 'multiple-address-match-original-region',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'lboost',
          'persistenceCheckboxHtmlId': 'multiple-address-match-original-region',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'mboost',
          'persistenceCheckboxHtmlId': 'multiple-address-match-original-region',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'jboost',
          'persistenceCheckboxHtmlId': 'multiple-address-match-original-region',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'display-type',
          'typeOfInput': 'radio',
          'defaultValue': 'Download',
          'persistenceState': true,
        },
        {
          'htmlId': 'paf-nag-preference',
          'typeOfInput': 'radio',
          'defaultValue': 'PAF',
          'persistenceState': true,
        },
      ]
    },
    {
      'page': 'multiple_address',
      'persistenceSettingDisabled': true,
      'inputObjects': [
        {
          'htmlId': 'limitperaddress',
          'persistenceState': true,
          'typeOfInput': 'text',
          'defaultValue': '1',
        },
        {
          'htmlId': 'name',
          'persistenceState': false,
          'typeOfInput': 'text',
          'defaultValue': '',
        },
        {
          'htmlId': 'paf-nag-preference',
          'typeOfInput': 'radio',
          'defaultValue': 'PAF',
          'persistenceState': true,
        },
        {
          'htmlId': 'header_row_export',
          'typeOfInput': 'checkbox',
          'persistenceState': true,
          'defaultValue': true,
        }
      ],
    },
    {
      'page': 'multiple_address_attributes',
      'persistenceSettingDisabled': true,
      'inputObjects': [
        {
          'htmlId': 'parent_uprn',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        },
        {
          'htmlId': 'latitude',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        },
        {
          'htmlId': 'longitude',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        },
        {
          'htmlId': 'easting',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        },
        {
          'htmlId': 'northing',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        },
        {
          'htmlId': 'classification_code',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        },
        {
          'htmlId': 'lpi_logical_status',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        },
        {
          'htmlId': 'country_code',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        },
        {
          'htmlId': 'formatted_address_nag',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        },
        {
          'htmlId': 'formatted_address_paf',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        },
        {
          'htmlId': 'welsh_formatted_address_nag',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        },
        {
          'htmlId': 'welsh_formatted_address_paf',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': false,
        },
      ],
    },
    {
      'page': 'uprn_multiple_match',
      'persistenceSettingDisabled': true,
      'inputObjects': [
        {
          'htmlId': 'header_row_export',
          'persistenceState': true,
          'defaultValue': true,
          'typeOfInput': 'checkbox',
        }
      ],
    },
    {
      'page': 'singlesearch', // Page is also the id in the settings table
      'inputObjects': [
        {
          'htmlId': 'input',
          'persistenceState': false,
          'typeOfInput': 'text',
          'defaultValue': '',
        },
        {
          'htmlId': 'classificationfilter',
          'persistenceState': true,
          'typeOfInput': 'autosuggest',
          'defaultValue': '',
        },
        {
          'htmlId': 'eboost',
          'persistenceCheckboxHtmlId': 'singlesearch-region',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'wboost',
          'persistenceCheckboxHtmlId': 'singlesearch-region',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'sboost',
          'persistenceCheckboxHtmlId': 'singlesearch-region',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'nboost',
          'persistenceCheckboxHtmlId': 'singlesearch-region',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'lboost',
          'persistenceCheckboxHtmlId': 'singlesearch-region',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'mboost',
          'persistenceCheckboxHtmlId': 'singlesearch-region',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'jboost',
          'persistenceCheckboxHtmlId': 'singlesearch-region',
          'persistenceState': true,
          'typeOfInput': 'checkbox',
          'defaultValue': true
        },
        {
          'htmlId': 'epoch',
          'persistenceState': true,
          'typeOfInput': 'radio',
          'defaultValue': latestEpochNumber,
        },
        {
          'htmlId': 'matchthreshold',
          'persistenceState': true,
          'typeOfInput': 'dropdown',
          'defaultValue': '5%',
        },
        {
          'htmlId': 'limit',
          'persistenceState': true,
          'typeOfInput': 'text',
          'defaultValue': '20',
        },
        {
          'htmlId': 'historical',
          'persistenceState': true,
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
          'persistenceState': true,
          'typeOfInput': 'text',
          'defaultValue': '',
        },
        {
          'htmlId': 'epoch',
          'persistenceState': true,
          'typeOfInput': 'radio',
          'defaultValue': latestEpochNumber,
        },
        {
          'htmlId': 'historical',
          'persistenceState': true,
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
          'persistenceState': true,
          'typeOfInput': 'text',
          'defaultValue': '',
        },
        {
          'htmlId': 'classificationfilter',
          'persistenceState': true,
          'typeOfInput': 'autosuggest',
          'defaultValue': '',
        },
        {
          'htmlId': 'epoch',
          'persistenceState': true,
          'typeOfInput': 'radio',
          'defaultValue': latestEpochNumber,
        },
        {
          'htmlId': 'limit',
          'persistenceState': true,
          'typeOfInput': 'text',
          'defaultValue': '20',
        },
        {
          'htmlId': 'historical',
          'persistenceState': true,
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
          'persistenceState': true,
          'typeOfInput': 'text',
          'defaultValue': '',
        },
        {
          'htmlId': 'limit',
          'persistenceState': true,
          'typeOfInput': 'text',
          'defaultValue': '10',
        },
        {
          'htmlId': 'epoch',
          'persistenceState': true,
          'typeOfInput': 'radio',
          'defaultValue': latestEpochNumber,
        },
        // Add a type 'text' for eboost, wboost, sboost, nboost, lboost, mboost, jboost
        {
          'htmlId': 'eboost',
          'persistenceState': true,
          'persistenceCheckboxHtmlId': 'typeahead-region',
          'typeOfInput': 'text',
          'defaultValue': '0',
        },
        {
          'htmlId': 'wboost',
          'persistenceState': true,
          'persistenceCheckboxHtmlId': 'typeahead-region',
          'typeOfInput': 'text',
          'defaultValue': '0',
        },
        {
          'htmlId': 'sboost',
          'persistenceState': true,
          'persistenceCheckboxHtmlId': 'typeahead-region',
          'typeOfInput': 'text',
          'defaultValue': '0',
        },
        {
          'htmlId': 'nboost',
          'persistenceState': true,
          'persistenceCheckboxHtmlId': 'typeahead-region',
          'typeOfInput': 'text',  
          'defaultValue': '0',
        },
        {
          'htmlId': 'lboost',
          'persistenceState': true,
          'persistenceCheckboxHtmlId': 'typeahead-region',
          'typeOfInput': 'text',
          'defaultValue': '0',
        },
        {
          'htmlId': 'mboost',
          'persistenceState': true,
          'persistenceCheckboxHtmlId': 'typeahead-region',
          'typeOfInput': 'text',
          'defaultValue': '0',
        },
        {
          'htmlId': 'jboost',
          'persistenceState': true,
          'persistenceCheckboxHtmlId': 'typeahead-region',
          'typeOfInput': 'text',
          'defaultValue': '0',
        }
      ]
    },
    {
      'page': 'custom_response',
      'persistenceSettingDisabled': true,
      'inputObjects': [
        {
          'htmlId': 'request-type',
          'persistenceState': true,
          'typeOfInput': 'dropdown',
          'defaultValue': 'GET',
        },
        {
          'htmlId': 'url-input',
          'persistenceState': true,
          'typeOfInput': 'autosuggest',
          'defaultValue': '',
        },
        {
          'htmlId': 'response-type',
          'persistenceState': true,
          'typeOfInput': 'radio',
          'defaultValue': 'plaintext',
        },
        {
          'htmlId': 'post-body',
          'persistenceState': true,
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
      'persistenceSettingDisabled': true,
      'inputObjects': [
        {
          'htmlId': 'lat',
          'persistenceState': true,
          'typeOfInput': 'text',
          'defaultValue': '50.73548',
        },
        {
          'htmlId': 'lon',
          'persistenceState': true,
          'typeOfInput': 'text',
          'defaultValue': '-3.5332105',
        },
        {
          'htmlId': 'rangekm',
          'persistenceState': true,
          'typeOfInput': 'text',
          'defaultValue': '10',
        },
        {
          'htmlId': 'input',
          'persistenceState': true,
          'typeOfInput': 'text',
          'defaultValue': '',
        },
        {
          'htmlId': 'uprn',
          'persistenceState': true,
          'typeOfInput': 'text',
          'defaultValue': '',
        },
        {
          'htmlId': 'classificationfilter',
          'persistenceState': true,
          'typeOfInput': 'autosuggest',
          'defaultValue': '',
        },
        {
          'htmlId': 'limit',
          'persistenceState': true,
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
