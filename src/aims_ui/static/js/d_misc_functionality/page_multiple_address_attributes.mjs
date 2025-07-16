import {
  setParentUprnPreference,
  getParentUprnPreference,
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



function init() {
  setupParentUprnPreferencesListeners();
  setupParentUprnPreferences();
}

window.addEventListener('load', init);
