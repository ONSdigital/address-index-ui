import {
  setParentUprnPreference,
  getParentUprnPreference,
  setFormattedAddressNagPreference,
  getFormattedAddressNagPreference,
  setFormattedAddressPafPreference,
  getFormattedAddressPafPreference,
} from '/static/js/f_helpers/local_storage_helpers.mjs';

function getBulkAttributes() {
  var attributeList = ""
  if (getParentUprnPreference()) {
      attributeList = attributeList.concat("parentUprn ")
  }
  if (getFormattedAddressNagPreference()) {
      attributeList = attributeList.concat("formattedAddressNag ")
  }
  if (getFormattedAddressPafPreference()) {
      attributeList = attributeList.concat("formattedAddressPaf ")
  }
   return attributeList
 }

 function setBulkAttributes() {
      const attributeInput = document.querySelector('#custom-bulk-attributes');
      attributeInput.value = getBulkAttributes()
 }

function init() {
   setBulkAttributes()
}

window.addEventListener('load', init);
