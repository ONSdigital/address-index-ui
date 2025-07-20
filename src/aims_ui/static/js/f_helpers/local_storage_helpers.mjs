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
    const defaultOptions = { match_type: 'true', recommendation_code: 'true' };
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
  localStorage.setItem('parentuprn_preference', preference);
}

export function getParentUprnPreference() {
  return localStorage.getItem('parentuprn_preference');
}

export function setFormattedAddressNagPreference(preference) {
  localStorage.setItem('formattedaddressnag_preference', preference);
}

export function getFormattedAddressNagPreference() {
  return localStorage.getItem('formattedaddressnag_preference');
}

export function setFormattedAddressPafPreference(preference) {
  localStorage.setItem('formattedaddresspaf_preference', preference);
}

export function getFormattedAddressPafPreference() {
  return localStorage.getItem('formattedaddresspaf_preference');
}

export function setFormattedAddressWelshNagPreference(preference) {
  localStorage.setItem('formattedaddresswelshnag_preference', preference);
}

export function getFormattedAddressWelshNagPreference() {
  return localStorage.getItem('formattedaddresswelshnag_preference');
}

export function setFormattedAddressWelshPafPreference(preference) {
  localStorage.setItem('formattedaddresswelshpaf_preference', preference);
}

export function getFormattedAddressWelshPafPreference() {
  return localStorage.getItem('formattedaddresswelshpaf_preference');
}

export function setLatitudePreference(preference) {
  localStorage.setItem('latitude_preference', preference);
}

export function getLatitudePreference() {
  return localStorage.getItem('latitude_preference');
}

export function setLongitudePreference(preference) {
  localStorage.setItem('longitude_preference', preference);
}

export function getLongitudePreference() {
  return localStorage.getItem('longitude_preference');
}

export function setEastingPreference(preference) {
  localStorage.setItem('easting_preference', preference);
}

export function getEastingPreference() {
  return localStorage.getItem('easting_preference');
}

export function setNorthingPreference(preference) {
  localStorage.setItem('northing_preference', preference);
}

export function getNorthingPreference() {
  return localStorage.getItem('northing_preference');
}

export function setClassificationCodePreference(preference) {
  localStorage.setItem('classificationcode_preference', preference);
}

export function getClassificationCodePreference() {
  return localStorage.getItem('classificationcode_preference');
}

export function setCountryCodePreference(preference) {
  localStorage.setItem('countrycode_preference', preference);
}

export function getCountryCodePreference() {
  return localStorage.getItem('countrycode_preference');
}

export function setLpiLogicalStatusPreference(preference) {
  localStorage.setItem('lpilogicalstatus_preference', preference);
}

export function getLpiLogicalStatusPreference() {
  return localStorage.getItem('lpilogicalstatus_preference');
}

// save_inputs local storage
export function saveToLocalStorage(inputObjectValues, loc) {
  const values = JSON.stringify(inputObjectValues);
  localStorage.setItem(loc, values);
}

export function wipeLocalStorage(loc) {
  localStorage.removeItem(loc);
}
