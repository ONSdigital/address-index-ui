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
  if (getParentUprnPreference() == 'true') {
      attributeList = attributeList.concat("parentUprn ")
  }
  if (getFormattedAddressNagPreference() == 'true') {
      attributeList = attributeList.concat("formattedAddressNag ")
  }
  if (getFormattedAddressPafPreference() == 'true') {
      attributeList = attributeList.concat("formattedAddressPaf ")
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
