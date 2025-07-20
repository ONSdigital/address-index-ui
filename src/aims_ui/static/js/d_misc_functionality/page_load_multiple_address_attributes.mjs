import {
  setParentUprnPreference,
  getParentUprnPreference,
  setFormattedAddressNagPreference,
  getFormattedAddressNagPreference,
  setFormattedAddressPafPreference,
  getFormattedAddressPafPreference,
  setFormattedAddressWelshNagPreference,
  getFormattedAddressWelshNagPreference,
  setFormattedAddressWelshPafPreference,
  getFormattedAddressWelshPafPreference,
  setLatitudePreference,
  getLatitudePreference,
  setLongitudePreference,
  getLongitudePreference,
  setEastingPreference,
  getEastingPreference,
  setNorthingPreference,
  getNorthingPreference,
  setClassificationCodePreference,
  getClassificationCodePreference,
  setCountryCodePreference,
  getCountryCodePreference,
  setLpiLogicalStatusPreference,
  getLpiLogicalStatusPreference,
} from '/static/js/f_helpers/local_storage_helpers.mjs';

function getBulkAttributes() {
  var attributeList = ""
  if (getParentUprnPreference() == 'true') {
      attributeList = attributeList.concat("parent_uprn ")
  }
  if (getFormattedAddressNagPreference() == 'true') {
      attributeList = attributeList.concat("formatted_address_nag ")
  }
  if (getFormattedAddressPafPreference() == 'true') {
      attributeList = attributeList.concat("formatted_address_paf ")
  }
  if (getFormattedAddressWelshNagPreference() == 'true') {
      attributeList = attributeList.concat("formatted_address_welsh_nag ")
  }
  if (getFormattedAddressWelshPafPreference() == 'true') {
      attributeList = attributeList.concat("formatted_address_welsh_paf ")
  }
  if (getLatitudePreference() == 'true') {
      attributeList = attributeList.concat("latitude ")
  }
  if (getLongitudePreference() == 'true') {
      attributeList = attributeList.concat("longitude ")
  }
  if (getEastingPreference() == 'true') {
      attributeList = attributeList.concat("easting ")
  }
  if (getNorthingPreference() == 'true') {
      attributeList = attributeList.concat("northing ")
  }
    if (getClassificationCodePreference() == 'true') {
      attributeList = attributeList.concat("classification_code ")
  }
    if (getCountryCodePreference() == 'true') {
      attributeList = attributeList.concat("country_code ")
  }
    if (getLpiLogicalStatusPreference() == 'true') {
      attributeList = attributeList.concat("lpi_logical_status ")
  }
   alert(attributeList)
   return attributeList
 }

 function setBulkAttributes() {
      const attributeInput = document.querySelector('#custom-bulk-attributes');
      attributeInput.value = getBulkAttributes()
      //alert(attributeInput.value)
 }

function init() {
   setBulkAttributes()
}

window.addEventListener('load', init);
