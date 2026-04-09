import { getDefaultGlobalValues } from '../default_values.mjs';
import {
  setGlobalValues,
} from '/static/js/f_helpers/local_storage_page_helpers.mjs';


// Second migration
export function migrateLocalStorageFromVersion1To2() {
  // Get the default global values (regardless of current page state/storage)
  const defaultGlobalValues = getDefaultGlobalValues();

  // Now take the relevant part for migration 
  // The inputSetting[{page: multiple_address}]'s inputObjects
  const multipleAddressInputObjects = 

  // Providing there have been no errors, set the version number to 2
  setGlobalValues({ LOCAL_STORAGE_VERSION: '2' });

  console.info('Local storage migration to version 2 completed.');
}