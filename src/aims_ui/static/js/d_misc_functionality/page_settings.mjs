import {
  getAddressTitlePreference,
  updateAddressFormatPreference,
  getCustomColumnWidths,
  setNewColumnWidths,
  getAdditionalRequestStatus,
  setAdditionalRequestStatus,
  setJobAgePreference,
  getJobAgePreference,
} from '/static/js/f_helpers/local_storage_helpers.mjs';

function updateAddressTitlePreference(e) {
  updateAddressFormatPreference(e);
}

// Paf and Nag Preferences
function setupNagAndPafStatus() {
  const current_status = getAddressTitlePreference();
  if (current_status === 'paf') {
    const pafRadio = document.querySelector('#paf-radio');
    pafRadio.checked = true;
  } else if (current_status === 'nag') {
    const nagRadio = document.querySelector('#nag-radio');
    nagRadio.checked = true;
  } else if (current_status === 'def') {
    const defRadio = document.querySelector('#default-radio');
    defRadio.checked = true;
  }
}

function setupNagAndPafListeners() {
  const pafRadio = document.querySelector('#paf-radio');
  const nagRadio = document.querySelector('#nag-radio');
  const defRadio = document.querySelector('#default-radio');

  pafRadio.addEventListener('change', (e) => {
    updateAddressTitlePreference('paf');
  });

  nagRadio.addEventListener('change', (e) => {
    updateAddressTitlePreference('nag');
  });

  defRadio.addEventListener('change', (e) => {
    updateAddressTitlePreference('def');
  });
}

// Column Width Preferences
function setValuesOfColumnWidthPreferences() {
  const colWidths = getCustomColumnWidths();
  for (const [key, width] of Object.entries(colWidths)) {
    const colInput = document.querySelector('#selector_' + key);
    colInput.value = width;
  }
}

function saveWidthValues(widthSelectors) {
  const newWidthValues = {};
  for (const selector of widthSelectors) {
    const selectorName = selector.id.replace('selector_', '');
    newWidthValues[selectorName] = selector.value;
  }
  setNewColumnWidths(newWidthValues);
}

function setupColumnWidthCustomiserListeners() {
  const widthSelectors = document.querySelectorAll('.columnWidthCustomiser');
  for (const selector of widthSelectors) {
    selector.addEventListener('change', (e) => {
      saveWidthValues(widthSelectors);
    });
  }
}

// Job Age Preferences
function setupJobAgePreferences() {
  const currentStatus = getJobAgePreference();

  const oldJobsCheckbox = document.querySelector('#old_jobs_checkbox');

  if (currentStatus === 'true') {
    oldJobsCheckbox.checked = true;
  }
}

function setupJobAgePreferencesListeners() {
  const jobAgeCheckbox = document.querySelector('#old_jobs_checkbox');

  jobAgeCheckbox.addEventListener('change', (e) => {
    const statusOfCheckbox = jobAgeCheckbox.checked;
    setJobAgePreference(statusOfCheckbox.toString());
  });
}

// Additional Request Details
function setupAdditionalRequestStatus() {
  const current_status = getAdditionalRequestStatus();

  const matchTypeCheckbox = document.querySelector('#match_type');
  const recomCodeCheckbox = document.querySelector('#recommendation_code');

  if (current_status.match_type === 'true') {
    matchTypeCheckbox.checked = true;
  }
  if (current_status.recommendation_code === 'true') {
    recomCodeCheckbox.checked = true;
  }
}

function setupAdditionalRequestListeners() {
  const matchTypeCheckbox = document.querySelector('#match_type');
  const recomCodeCheckbox = document.querySelector('#recommendation_code');

  matchTypeCheckbox.addEventListener('change', (e) => {
    const currentSettings = getAdditionalRequestStatus();
    const mtStatus = matchTypeCheckbox.checked;
    currentSettings.match_type = mtStatus.toString();
    setAdditionalRequestStatus(currentSettings);
  });

  recomCodeCheckbox.addEventListener('change', (e) => {
    const currentSettings = getAdditionalRequestStatus();
    const recomCodeStatus = recomCodeCheckbox.checked;
    currentSettings.recommendation_code = recomCodeStatus.toString();
    setAdditionalRequestStatus(currentSettings);
  });
}

function init() {
  setupNagAndPafListeners();
  setupNagAndPafStatus();
  setValuesOfColumnWidthPreferences();
  setupColumnWidthCustomiserListeners();
  setupAdditionalRequestStatus();
  setupAdditionalRequestListeners();
  setupJobAgePreferences();
  setupJobAgePreferencesListeners();
}

window.addEventListener('load', init);
