import { getGlobalValues } from '/static/js/f_helpers/local_storage_page_helpers.mjs';
import { getBroadcastLocalStorageVersion } from './get_local_storage_version.mjs';

// Migration imports here
import { migrateLocalStorageFromVersion0To1 } from './local_storage_migrations/local_storage_migration1.mjs';

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
    // Loop over each page's setting object
    if (pageSettings.page === page_name) {
      return pageSettings;
    }
  }

  console.warn(`No default input settings found for page: ${page_name}`);
  return {};
}

// Get the broadcast version resolved promise so that code isn't asynchronous and lead to race conditions
const broadcastVersion = await getBroadcastLocalStorageVersion();

export function setupDefaultGlobalValues() {
  // Get the current global values
  const currentGlobalValues = getGlobalValues();

  // Get the broadcast local storage version
  const currentLocalStorageVersion = currentGlobalValues.LOCAL_STORAGE_VERSION || null;

  if (broadcastVersion !== currentLocalStorageVersion) {
    console.info(`Local storage version mismatch: broadcast version is ${broadcastVersion}, current local storage version is ${currentLocalStorageVersion}.`);
    runLocalStorageMigration(currentLocalStorageVersion, broadcastVersion);
  } else if (broadcastVersion === currentLocalStorageVersion) {
    console.debug(`Local storage version is up to date at version ${broadcastVersion}. No migration needed.`);
  }
}

function runLocalStorageMigration(currentVersion, targetVersion) {
  // Based on currentVersion and targetVersion, run the correct migration script

  // If there's no version (null), then perform the first migration
  // Skips other migrations as the first migration should always setup the latest defaults
  if (currentVersion === null) {
    console.info(`Running local storage migration from null or undefined version to Latest Version (${targetVersion}). This should only happen once.`);
    migrateLocalStorageFromVersion0To1(targetVersion);
  } 

  // Increimental Migrations go here
  if (currentVersion === '1' && targetVersion === '2') {
    console.info('Running local storage migration from version 1 to 2. This should only happen once.');
    console.debug('This migration should add historical checkbox and classification to the local storage defaults for the multiple_address page.');
    migrateLocalStorageFromVersion1To2();
  }
}
