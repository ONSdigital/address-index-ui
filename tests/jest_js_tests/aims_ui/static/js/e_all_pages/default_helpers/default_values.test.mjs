import { jest, test, expect, describe, beforeAll } from '@jest/globals';

let helpers;

beforeAll(async () => {
  helpers = await import('../../../../../../src/aims_ui/static/js/f_helpers/local_storage_page_helpers.mjs');

  jest.spyOn(helpers, 'getGlobalValues').mockReturnValue({
    latestEpochNumber: '111',
  });
});

describe('getDefaultGlobalValues', () => {
  test('has all expected keys and expected contents', () => {
    const defaults = helpers.getDefaultGlobalValues();

    // Key presence 
    const expectedTopLevelKeys = [
      'singleJobDownloadFormat',
      'singleJobDownloadAttributeInclusion',
      'showOlderJobsInBulkMatchingPage',
      'addressCardTitleType',
      'columnWidths',
      'additionalRequestDetails',
      'favouriteAddressAttributes',
      'inputSettings',
    ];

    for (const key of expectedTopLevelKeys) {
      expect(defaults).toHaveProperty(key);
      if (!(key in defaults)) {
        throw new Error(`missing key: ${key}`);
      }
    }

    // Key contents 
    // Simple scalars
    expect(defaults.singleJobDownloadFormat).toBe('csv');
    expect(defaults.singleJobDownloadAttributeInclusion).toBe('all');
    expect(defaults.showOlderJobsInBulkMatchingPage).toBe(false);
    expect(defaults.addressCardTitleType).toBe('default');

    // columnWidths object + required attributes
    const expectedColumnWidths = {
      space_col_1: '1',
      content_col_2: '4',
      space_col_3: '1',
      content_col_4: '5',
    };

    expect(typeof defaults.columnWidths).toBe('object');
    expect(defaults.columnWidths).not.toBeNull();

    for (const attr of Object.keys(expectedColumnWidths)) {
      if (!(attr in defaults.columnWidths)) {
        throw new Error(`Key columnWidths missing expected attribute: ${attr}`);
      }
      expect(defaults.columnWidths[attr]).toBe(expectedColumnWidths[attr]);
    }

    // additionalRequestDetails object + required attributes
    const expectedAdditionalRequestDetails = {
      match_type: true,
      recommendation_code: true,
      tokenised_output: false,
    };

    expect(typeof defaults.additionalRequestDetails).toBe('object');
    expect(defaults.additionalRequestDetails).not.toBeNull();

    for (const attr of Object.keys(expectedAdditionalRequestDetails)) {
      if (!(attr in defaults.additionalRequestDetails)) {
        throw new Error(`Key additionalRequestDetails missing expected attribute: ${attr}`);
      }
      expect(defaults.additionalRequestDetails[attr]).toBe(expectedAdditionalRequestDetails[attr]);
    }

    // favouriteAddressAttributes array
    const expectedFavouriteAddressAttributes = [
      'uprn',
      'parentUprn',
      'classificationCode',
      'classificationCodeList',
      'formattedConfidenceScore',
      'nagLocalCustodianName',
    ];

    expect(Array.isArray(defaults.favouriteAddressAttributes)).toBe(true);
    expect(defaults.favouriteAddressAttributes).toEqual(expectedFavouriteAddressAttributes);

    // inputSettings array basic validation + per-page checks
    expect(Array.isArray(defaults.inputSettings)).toBe(true);

    const pagesByName = new Map(defaults.inputSettings.map((p) => [p.page, p]));

    const expectedPages = [
      'multiple_address_original',
      'multiple_address',
      'multiple_address_attributes',
      'uprn_multiple_match',
      'singlesearch',
      'uprn',
      'postcode',
      'typeahead',
      'custom_response',
      'radiussearch',
    ];

    for (const page of expectedPages) {
      if (!pagesByName.has(page)) {
        throw new Error(`Key inputSettings missing expected page: ${page}`);
      }
    }

    // Helper: assert a page has an input object with expected properties.
    const assertInputObject = (pageName, htmlId, expected) => {
      const page = pagesByName.get(pageName);
      if (!page) throw new Error(`Key inputSettings missing expected page: ${pageName}`);

      if (!Array.isArray(page.inputObjects)) {
        throw new Error(`Key inputSettings page ${pageName} missing expected attribute: inputObjects`);
      }

      const obj = page.inputObjects.find((x) => x.htmlId === htmlId);
      if (!obj) {
        throw new Error(`Key inputSettings page ${pageName} missing expected input object htmlId: ${htmlId}`);
      }

      for (const [attr, value] of Object.entries(expected)) {
        if (!(attr in obj)) {
          throw new Error(`Key inputSettings page ${pageName} htmlId ${htmlId} missing expected attribute: ${attr}`);
        }
        expect(obj[attr]).toEqual(value);
      }
    };

    // multiple_address_original
    assertInputObject('multiple_address_original', 'limit', {
      persistenceState: true,
      typeOfInput: 'text',
      defaultValue: '5',
    });

    assertInputObject('multiple_address_original', 'matchthreshold', {
      persistenceState: true,
      typeOfInput: 'dropdown',
      defaultValue: '1%',
    });

    assertInputObject('multiple_address_original', 'historical', {
      persistenceState: true,
      typeOfInput: 'checkbox',
      defaultValue: false,
    });

    // multiple_address
    assertInputObject('multiple_address', 'limitperaddress', {
      persistenceState: true,
      typeOfInput: 'text',
      defaultValue: '1',
    });

    // multiple_address_attributes
    assertInputObject('multiple_address_attributes', 'latitude', {
      persistenceState: true,
      typeOfInput: 'checkbox',
      defaultValue: false,
    });

    // uprn_multiple_match
    assertInputObject('uprn_multiple_match', 'header_row_export', {
      persistenceState: true,
      typeOfInput: 'checkbox',
      defaultValue: true,
    });

    // singlesearch
    assertInputObject('singlesearch', 'matchthreshold', {
      persistenceState: true,
      typeOfInput: 'dropdown',
      defaultValue: '5%',
    });

    assertInputObject('singlesearch', 'limit', {
      persistenceState: true,
      typeOfInput: 'text',
      defaultValue: '20',
    });

    // postcode
    assertInputObject('postcode', 'limit', {
      persistenceState: true,
      typeOfInput: 'text',
      defaultValue: '20',
    });

    // typeahead
    assertInputObject('typeahead', 'limit', {
      persistenceState: true,
      typeOfInput: 'text',
      defaultValue: '10',
    });

    assertInputObject('typeahead', 'eboost', {
      persistenceState: true,
      typeOfInput: 'text',
      defaultValue: '0',
    });

    // custom_response
    assertInputObject('custom_response', 'request-type', {
      persistenceState: true,
      typeOfInput: 'dropdown',
      defaultValue: 'GET',
    });

    // radiussearch
    assertInputObject('radiussearch', 'lat', {
      persistenceState: true,
      typeOfInput: 'text',
      defaultValue: '50.73548',
    });

    assertInputObject('radiussearch', 'lon', {
      persistenceState: true,
      typeOfInput: 'text',
      defaultValue: '-3.5332105',
    });

    assertInputObject('radiussearch', 'rangekm', {
      persistenceState: true,
      typeOfInput: 'text',
      defaultValue: '10',
    });
  });
});
