import {
  getGlobalValues,
  setGlobalValues,
} from '/static/js/f_helpers/local_storage_page_helpers.mjs';
import { getDefaultGlobalValues } from './default_values.mjs';

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

function getDefaultInputObjectsForPage(page_name) {

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


export function setupDefaultGlobalValues() {
  // Set default values for global values if they don't already exist
  const currentGlobalValues = getGlobalValues();

  const defaultGlobalValues = getDefaultGlobalValues();

  const updatedValues = { ...defaultGlobalValues, ...currentGlobalValues };

  setGlobalValues(updatedValues);
}

