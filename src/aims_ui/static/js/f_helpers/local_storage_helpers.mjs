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
