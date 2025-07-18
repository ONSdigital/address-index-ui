import {
  setParentUprnPreference,
  getParentUprnPreference,
  setFormattedAddressNagPreference,
  getFormattedAddressNagPreference,
  setFormattedAddressPafPreference,
  getFormattedAddressPafPreference,
} from '/static/js/f_helpers/local_storage_helpers.mjs';

// Response Attribute  Preferences
function setupParentUprnPreferences() {
  const currentStatus = getParentUprnPreference();
  const parentUprnCheckbox = document.querySelector('#parentuprn');

  if (currentStatus === 'true') {
    parentUprnCheckbox.checked = true;
  }
}

function setupParentUprnPreferencesListeners() {
  const parentUprnCheckbox = document.querySelector('#parentuprn');

  parentUprnCheckbox.addEventListener('change', (e) => {
    const statusOfCheckbox = parentUprnCheckbox.checked;
    setParentUprnPreference(statusOfCheckbox.toString());
  });
}

function setupFormattedAddressNagPreferences() {
  const currentStatus = getFormattedAddressNagPreference();
  const formattedAddressNagCheckbox = document.querySelector('#formattedaddressnag');

  if (currentStatus === 'true') {
    formattedAddressNagCheckbox.checked = true;
  }
}

function setupFormattedAddressNagPreferencesListeners() {
  const formattedAddressNagCheckbox = document.querySelector('#formattedaddressnag');

  formattedAddressNagCheckbox.addEventListener('change', (e) => {
    const statusOfCheckbox = formattedAddressNagCheckbox.checked;
    setFormattedAddressNagPreference(statusOfCheckbox.toString());
  });
}

function setupFormattedAddressPafPreferences() {
  const currentStatus = getFormattedAddressPafPreference();
  const formattedAddressPafCheckbox = document.querySelector('#formattedaddresspaf');

  if (currentStatus === 'true') {
    formattedAddressPafCheckbox.checked = true;
  }
}

function setupFormattedAddressPafPreferencesListeners() {
  const formattedAddressPafCheckbox = document.querySelector('#formattedaddresspaf');

  formattedAddressPafCheckbox.addEventListener('change', (e) => {
    const statusOfCheckbox = formattedAddressPafCheckbox.checked;
    setFormattedAddressPafPreference(statusOfCheckbox.toString());
  });
}


function init() {
  setupParentUprnPreferencesListeners();
  setupParentUprnPreferences();
  setupFormattedAddressNagPreferencesListeners();
  setupFormattedAddressNagPreferences();
  setupFormattedAddressPafPreferencesListeners();
  setupFormattedAddressPafPreferences();

}

window.addEventListener('load', init);
