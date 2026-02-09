import { getPageLocalValues } from '/static/js/f_helpers/local_storage_page_helpers.mjs';


function getListOfAttributesAsStringFromLocalStorage() {
  // Get the attributes stored in the mutliple_address_attributes page
  const pageNameWithTogglableAttributes = 'multiple_address_attributes';
  const pageLocalValues = getPageLocalValues(pageNameWithTogglableAttributes);
  const valuePairOfAttributeEnabled = pageLocalValues['pagePreviouslySearchedValues'] || {};

  console.log('PageName with togglable attributes:', pageNameWithTogglableAttributes, 'Value pair of attribute enabled from local storage:', valuePairOfAttributeEnabled);
  console.log('pageLocalValues from local storage:', pageLocalValues);
  console.log('pagePreviouslySearchedValues from local storage:', pageLocalValues.pagePreviouslySearchedValues);

  // Create a space seperated list of enabled attributes
  let attributeList = '';

  for (const [attribute, isEnabled] of Object.entries(valuePairOfAttributeEnabled)) {
    if (isEnabled) {
      attributeList = attributeList.concat(`${attribute} `);
    }
  }

  return attributeList.trim();
}

function setBulkAttributes() {
  const attributeInput = document.querySelector('#custom-bulk-attributes');
  const listOfAttributesAsString = getListOfAttributesAsStringFromLocalStorage();
  console.log('Setting the bulk attribute input to the following list of attributes from local storage:', listOfAttributesAsString);
  attributeInput.value = listOfAttributesAsString;
}

export function loadMultipleAddressAttributesInit() {
  setBulkAttributes();
}