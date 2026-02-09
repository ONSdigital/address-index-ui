import { getDefaultGlobalValues } from '../default_values.mjs';
import {
  setGlobalValues,
} from '/static/js/f_helpers/local_storage_page_helpers.mjs';


// First migration
export function migrateLocalStorageFromVersion0To1() {
  // For a null/undefined/0 version, to current version, wipe all values and set defaults
  localStorage.clear();

  // Then set the default values defined in default_values.mjs
  const defaultGlobalValues = getDefaultGlobalValues();
  setGlobalValues(defaultGlobalValues);

  // Providing there have been no errors, set the version number to 1
  setGlobalValues({ LOCAL_STORAGE_VERSION: '1' });

  console.info('Local storage migration to version 1 completed. With default global values set to:', defaultGlobalValues);
}