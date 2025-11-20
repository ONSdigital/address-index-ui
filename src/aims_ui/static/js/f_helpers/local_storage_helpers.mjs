// custom response helpers START
export function getFormatPreferenceCustomResponse() {
  return localStorage.getItem('custom_response_return_format');
}

export function getRequestTypeCustomResponse() {
  return localStorage.getItem('custom_response_request_type');
}

export function getReqBodyStyle() {
  return localStorage.getItem('custom_response_req_body_style');
}

export function updateReqBodyStyle(newStyle) {
  localStorage.setItem('custom_response_req_body_style', newStyle);
}

export function updateCustomResponseRequestType(requestType) {
  localStorage.setItem('custom_response_request_type', requestType);
}

export function updateCustomResponseFormat(preferenceRadioId) {
  localStorage.setItem('custom_response_return_format', preferenceRadioId);
}

export function setDefaultResponseFormatCustomResponse() {
  if (!localStorage.getItem('custom_response_return_format')) {
    updateCustomResponseFormat('response-type-object');
  }
  if (!localStorage.getItem('custom_response_request_type')) {
    updateCustomResponseRequestType('GET');
  }
  if (!localStorage.getItem('custom_response_req_body_style')) {
    updateReqBodyStyle('');
  }
}
// custom response helpers END

export function updateAddressFormatPreference(pafOrNag) {
  localStorage.setItem('custom_settings_address_preference', pafOrNag);
}

export function getAddressTitlePreference() {
  return localStorage.getItem('custom_settings_address_preference');
}

export function setDefaultTitleChoice() {
  if (!localStorage.getItem('custom_settings_address_preference')) {
    localStorage.setItem('custom_settings_address_preference', 'def');
  }
}

export function getCustomColumnWidths() {
  const obj = localStorage.getItem('custom_column_width');
  return JSON.parse(obj);
}

export function setDefaultColumnWidths() {
  // Default widths of columns for the interface
  if (!localStorage.getItem('custom_column_width')) {
    const defaultValues = JSON.stringify({
      space_col_1: 1,
      content_col_2: 4,
      space_col_3: 1,
      content_col_4: 5,
    });
    localStorage.setItem('custom_column_width', defaultValues);
  }
}

export function setNewColumnWidths(values) {
  const newValues = JSON.stringify(values);
  localStorage.setItem('custom_column_width', newValues);
}

// Old job preferences
export function setDefaultJobAgePreferences() {
  if (!localStorage.getItem('job_age_preference')) {
    // By default do not include older jobs
    const defaultOption = 'false';
    setJobAgePreference(defaultOption);
  }
}

export function setJobAgePreference(preference) {
  localStorage.setItem('job_age_preference', preference);
}

export function getJobAgePreference() {
  return localStorage.getItem('job_age_preference');
}

// AdditionalRequests status
export function setDefaultAdditionalRequestStatus() {
  if (!localStorage.getItem('custom_settings_additional_request_info')) {
    const defaultOptions = { match_type: 'true', recommendation_code: 'true', tokenised_output: 'true'};
    setAdditionalRequestStatus(defaultOptions);
  }
}

export function getAdditionalRequestStatus() {
  const obj = localStorage.getItem('custom_settings_additional_request_info');
  return JSON.parse(obj);
}

export function setAdditionalRequestStatus(settings) {
  const stringifiedSettings = JSON.stringify(settings);
  localStorage.setItem(
    'custom_settings_additional_request_info',
    stringifiedSettings
  );
}

// Getters and setters for Custom Response

export function setParentUprnPreference(preference) {
  setCustomBulkAttributePreference('parentuprn', preference);
}

export function getParentUprnPreference() {
  return isCustomBulkAttributesSelected('parentuprn');
}

export function setFormattedAddressNagPreference(preference) {
  setCustomBulkAttributePreference('formattedaddressnag', preference);
}

export function getFormattedAddressNagPreference() {
  return isCustomBulkAttributesSelected('formattedaddressnag');
}

export function setFormattedAddressPafPreference(preference) {
  setCustomBulkAttributePreference('formattedaddresspaf', preference);
}

export function getFormattedAddressPafPreference() {
  return isCustomBulkAttributesSelected('formattedaddresspaf');
}

export function setFormattedAddressWelshNagPreference(preference) {
  setCustomBulkAttributePreference('formattedaddresswelshnag', preference);
}

export function getFormattedAddressWelshNagPreference() {
  return isCustomBulkAttributesSelected('formattedaddresswelshnag');
}

export function setFormattedAddressWelshPafPreference(preference) {
  setCustomBulkAttributePreference('formattedaddresswelshpaf', preference);
}

export function getFormattedAddressWelshPafPreference() {
  return isCustomBulkAttributesSelected('formattedaddresswelshpaf');
}

export function setLatitudePreference(preference) {
  setCustomBulkAttributePreference('latitude', preference);
}

export function getLatitudePreference() {
  return isCustomBulkAttributesSelected('latitude');
}

export function setLongitudePreference(preference) {
  setCustomBulkAttributePreference('longitude', preference);
}

export function getLongitudePreference() {
  return isCustomBulkAttributesSelected('longitude');
}

export function setEastingPreference(preference) {
  setCustomBulkAttributePreference('easting', preference);
}

export function getEastingPreference() {
  return isCustomBulkAttributesSelected('easting');
}

export function setNorthingPreference(preference) {
  setCustomBulkAttributePreference('northing', preference);
}

export function getNorthingPreference() {
  return isCustomBulkAttributesSelected('northing');
}

export function setClassificationCodePreference(preference) {
  setCustomBulkAttributePreference('classificationcode', preference);
}

export function getClassificationCodePreference() {
  return isCustomBulkAttributesSelected('classificationcode');
}

export function setCountryCodePreference(preference) {
  setCustomBulkAttributePreference('countrycode', preference);
}

export function getCountryCodePreference() {
  return isCustomBulkAttributesSelected('countrycode');
}

export function setLpiLogicalStatusPreference(preference) {
  setCustomBulkAttributePreference('lpilogicalstatus', preference);
}

export function getLpiLogicalStatusPreference() {
  return isCustomBulkAttributesSelected('lpilogicalstatus');
}


// functions to allow bulk custom attributes to be grouped into one storage string

function addItemToCustomBulkAttributes(fieldtoadd) {
    let attArray = JSON.parse(localStorage.getItem('custom_bulk_response_attributes'));
    if ((attArray) == null) {
        attArray = [];
    }
    if (!(attArray.includes(fieldtoadd))) {
      attArray.push(fieldtoadd)
      localStorage.setItem('custom_bulk_response_attributes', JSON.stringify(attArray));
    }
}

function removeItemFromCustomBulkAttributes(fieldtoremove) {
    let attArray = JSON.parse(localStorage.getItem('custom_bulk_response_attributes'));
    if (attArray != null) {
      if (attArray.includes(fieldtoremove)) {
        const index = attArray.indexOf(fieldtoremove);
        const deletedItem = attArray.splice(index, 1);
        localStorage.setItem('custom_bulk_response_attributes', JSON.stringify(attArray));
      }
    }
}

function isCustomBulkAttributesSelected(fieldtotest) {
    const attArray = JSON.parse(localStorage.getItem('custom_bulk_response_attributes'));
    if (attArray == null) {
        return 'false'
    }
    if (attArray.includes(fieldtotest)) {
         return 'true'
      }
    return 'false'
}

function setCustomBulkAttributePreference(fieldname, preference) {
    if (preference == 'true') {
        addItemToCustomBulkAttributes(fieldname)
    } else {
        removeItemFromCustomBulkAttributes(fieldname)
    }
}

// save_inputs local storage
export function saveToLocalStorage(inputObjectValues, loc) {
  const values = JSON.stringify(inputObjectValues);
  localStorage.setItem(loc, values);
}

export function wipeLocalStorage(loc) {
  localStorage.removeItem(loc);
}
