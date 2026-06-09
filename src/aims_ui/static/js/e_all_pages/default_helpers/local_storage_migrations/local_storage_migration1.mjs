import { getDefaultGlobalValues } from '../default_values.mjs';
import {
  setGlobalValues,
} from '/static/js/f_helpers/local_storage_page_helpers.mjs';


// First migration
export function migrateLocalStorageFromVersionNullToLatest(targetVersion) {
  // For a null/undefined/0 version, to the most recent version - sets all defaults to default values 
  localStorage.clear();

  // Then set the default values defined in default_values.mjs
  const defaultGlobalValues = getDefaultGlobalValues();
  setGlobalValues(defaultGlobalValues);

  // Providing there have been no errors, set the version number to 1
  setGlobalValues({ LOCAL_STORAGE_VERSION: targetVersion });

  console.info(`Local storage migration to version ${targetVersion} completed. With default global values set to:`, defaultGlobalValues);
}