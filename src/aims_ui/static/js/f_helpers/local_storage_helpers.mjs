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

// save_inputs local storage
export function saveToLocalStorage(inputObjectValues, loc) {
  const values = JSON.stringify(inputObjectValues);
  localStorage.setItem(loc, values);
}
export function wipeLocalStorage(loc) {
  localStorage.removeItem(loc);
}
