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

function setupFormattedAddressWelshNagPreferences() {
  const currentStatus = getFormattedAddressWelshNagPreference();

  const formattedAddressWelshNagCheckbox = document.querySelector('#welshformattedaddressnag');

  if (currentStatus === 'true') {
    formattedAddressWelshNagCheckbox.checked = true;
  }
}

function setupFormattedAddressWelshNagPreferencesListeners() {
  const formattedAddressWelshNagCheckbox = document.querySelector('#welshformattedaddressnag');

  formattedAddressWelshNagCheckbox.addEventListener('change', (e) => {
    const statusOfCheckbox = formattedAddressWelshNagCheckbox.checked;
    setFormattedAddressWelshNagPreference(statusOfCheckbox.toString());
  });
}

function setupFormattedAddressWelshPafPreferences() {
  const currentStatus = getFormattedAddressWelshPafPreference();
  const formattedAddressWelshPafCheckbox = document.querySelector('#welshformattedaddresspaf');

  if (currentStatus === 'true') {
    formattedAddressWelshPafCheckbox.checked = true;
  }
}

function setupFormattedAddressWelshPafPreferencesListeners() {
  const formattedAddressWelshPafCheckbox = document.querySelector('#welshformattedaddresspaf');

  formattedAddressWelshPafCheckbox.addEventListener('change', (e) => {
    const statusOfCheckbox = formattedAddressWelshPafCheckbox.checked;
    setFormattedAddressWelshPafPreference(statusOfCheckbox.toString());
  });
}

function setupLatitudePreferences() {
  const currentStatus = getLatitudePreference();
  const latitudeCheckbox = document.querySelector('#latitude');

  if (currentStatus === 'true') {
    latitudeCheckbox.checked = true;
  }
}

function setupLatitudePreferencesListeners() {
  const latitudeCheckbox = document.querySelector('#latitude');

  latitudeCheckbox.addEventListener('change', (e) => {
    const statusOfCheckbox = latitudeCheckbox.checked;
    setLatitudePreference(statusOfCheckbox.toString());
  });
}

function setupLongitudePreferences() {
  const currentStatus = getLongitudePreference();
  const longitudeCheckbox = document.querySelector('#longitude');

  if (currentStatus === 'true') {
    longitudeCheckbox.checked = true;
  }
}

function setupLongitudePreferencesListeners() {
  const longitudeCheckbox = document.querySelector('#longitude');

  longitudeCheckbox.addEventListener('change', (e) => {
    const statusOfCheckbox = longitudeCheckbox.checked;
    setLongitudePreference(statusOfCheckbox.toString());
  });
}

function setupEastingPreferences() {
  const currentStatus = getEastingPreference();
  const eastingCheckbox = document.querySelector('#easting');

  if (currentStatus === 'true') {
    eastingCheckbox.checked = true;
  }
}

function setupEastingPreferencesListeners() {
  const eastingCheckbox = document.querySelector('#easting');

  eastingCheckbox.addEventListener('change', (e) => {
    const statusOfCheckbox = eastingCheckbox.checked;
    setEastingPreference(statusOfCheckbox.toString());
  });
}

function setupNorthingPreferences() {
  const currentStatus = getNorthingPreference();
  const northingCheckbox = document.querySelector('#northing');

  if (currentStatus === 'true') {
    northingCheckbox.checked = true;
  }
}

function setupNorthingPreferencesListeners() {
  const northingCheckbox = document.querySelector('#northing');

  northingCheckbox.addEventListener('change', (e) => {
    const statusOfCheckbox = northingCheckbox.checked;
    setNorthingPreference(statusOfCheckbox.toString());
  });
}

function setupClassificationCodePreferences() {
  const currentStatus = getClassificationCodePreference();
  const classificationCodeCheckbox = document.querySelector('#classificationcode');

  if (currentStatus === 'true') {
    classificationCodeCheckbox.checked = true;
  }
}

function setupClassificationCodePreferencesListeners() {
  const classificationCodeCheckbox = document.querySelector('#classificationcode');

  classificationCodeCheckbox.addEventListener('change', (e) => {
    const statusOfCheckbox = classificationCodeCheckbox.checked;
    setClassificationCodePreference(statusOfCheckbox.toString());
  });
}

function setupCountryCodePreferences() {
  const currentStatus = getCountryCodePreference();
  const countryCodeCheckbox = document.querySelector('#countrycode');

  if (currentStatus === 'true') {
    countryCodeCheckbox.checked = true;
  }
}

function setupCountryCodePreferencesListeners() {
  const countryCodeCheckbox = document.querySelector('#countrycode');

  countryCodeCheckbox.addEventListener('change', (e) => {
    const statusOfCheckbox = countryCodeCheckbox.checked;
    setCountryCodePreference(statusOfCheckbox.toString());
  });
}

function setupLpiLogicalStatusPreferences() {
  const currentStatus = getLpiLogicalStatusPreference();
  const lpiLogicalStatusCheckbox = document.querySelector('#lpilogicalstatus');

  if (currentStatus === 'true') {
    lpiLogicalStatusCheckbox.checked = true;
  }
}

function setupLpiLogicalStatusPreferencesListeners() {
  const lpiLogicalStatusCheckbox = document.querySelector('#lpilogicalstatus');

  lpiLogicalStatusCheckbox.addEventListener('change', (e) => {
    const statusOfCheckbox = lpiLogicalStatusCheckbox.checked;
    setLpiLogicalStatusPreference(statusOfCheckbox.toString());
  });
}

function init() {
  setupParentUprnPreferencesListeners();
  setupParentUprnPreferences();
  setupFormattedAddressNagPreferencesListeners();
  setupFormattedAddressNagPreferences();
  setupFormattedAddressPafPreferencesListeners();
  setupFormattedAddressPafPreferences();
  setupFormattedAddressWelshPafPreferencesListeners();
  setupFormattedAddressWelshPafPreferences();
  setupFormattedAddressWelshNagPreferencesListeners();
  setupFormattedAddressWelshNagPreferences();
  setupLatitudePreferencesListeners();
  setupLatitudePreferences();
  setupLongitudePreferencesListeners();
  setupLongitudePreferences();
  setupEastingPreferencesListeners();
  setupEastingPreferences();
  setupNorthingPreferencesListeners();
  setupNorthingPreferences();
  setupClassificationCodePreferencesListeners();
  setupClassificationCodePreferences();
  setupCountryCodePreferencesListeners();
  setupCountryCodePreferences();
  setupLpiLogicalStatusPreferencesListeners();
  setupLpiLogicalStatusPreferences();

}

window.addEventListener('load', init);
