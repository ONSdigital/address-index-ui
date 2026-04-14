import { getDefaultGlobalValues } from '../default_values.mjs';
import {
  setGlobalValues,
  getGlobalValues
} from '/static/js/f_helpers/local_storage_page_helpers.mjs';

function getMatchingPageNameFromArrayOfPageObjects(pageObjectsArray, page_name) {
  for (const pageObject of pageObjectsArray) {
    if (pageObject.page === page_name) {
      return pageObject;
    }
  }
  return null;
}

function getMultipleAddressInputObjectsFromGlobalValuesStructure(globalValues) {
  const clientInputSettings = globalValues.inputSettings || {};
  console.debug('Client input settings:', clientInputSettings);

  const multipleMatchInputSettings = getMatchingPageNameFromArrayOfPageObjects(clientInputSettings, 'multiple_address');
  console.debug('Multiple Match Page Input Settings:', multipleMatchInputSettings);

  const multipleAddressInputObjects = multipleMatchInputSettings.inputObjects || {};
  console.debug('Multiple Address Input Objects:', multipleAddressInputObjects);

  return multipleAddressInputObjects;
}

// Second migration
export function migrateLocalStorageFromVersion1To2() {
  // Get the client's global values for Multiple Address Input Objects
  const clientGlobalValues = getGlobalValues();
  console.log('Client global values before migration:', clientGlobalValues);

  const clientMultipleAddressInputObjects = getMultipleAddressInputObjectsFromGlobalValuesStructure(clientGlobalValues);
  console.log('Client multiple address input objects before migration:', clientMultipleAddressInputObjects);

  const inputObjectsToAdd = [
    {
      'htmlId': 'historical',
      'persistenceState': true,
      'typeOfInput': 'checkbox',
      'defaultValue': false,
    },
    {
      'htmlId': 'classificationfilter',
      'persistenceState': true,
      'typeOfInput': 'autosuggest',
      'defaultValue': '',
    },
  ]

  // Merge the objects to add with cluentMultipleAddressInputObjects, ensuring we don't overwrite any existing keys
  for (const potentiallyNewObject of inputObjectsToAdd) {
    // Search for an object with htmlId that matches the potentiallyNewObject
    const existingObjectIndex = clientMultipleAddressInputObjects.findIndex(obj => obj.htmlId === potentiallyNewObject.htmlId);

    // If the object doesn't exist, add it to the array
    if (existingObjectIndex === -1) {
      clientMultipleAddressInputObjects.push(potentiallyNewObject);
      console.info(`Added new input object with htmlId '${potentiallyNewObject.htmlId}' to multiple address input objects.`);
    } 
  }

  // Save Back to client local storage
  console.log('Client global values after migration:', clientGlobalValues);
  setGlobalValues(clientGlobalValues);

  // Providing there have been no errors, set the version number to 2
  setGlobalValues({ LOCAL_STORAGE_VERSION: '2' });

  console.info('Local storage migration to version 2 completed.');
}