import { 
  updateCustomResponseFormat,
  getFormatPrefferenceCustomResponse,
} from '../local_storage_helpers.mjs';


function addChangeEventListeners(radioText, radioAddObj) {
  radioText.addEventListener('change', (e) => {
    updateCustomResponseFormat('response-type-text');
  });

  radioAddObj.addEventListener('change', (e) => {
    updateCustomResponseFormat('response-type-object');
  });
}

function setupRadioStatuses(radioText, radioAddObj) {
  const savedTextStatus = getFormatPrefferenceCustomResponse();
  const radioToSelect = document.querySelector('#' + savedTextStatus);
  radioToSelect.checked = true;
}

function init() {
  const radioText = document.querySelector('#response-type-text');
  const radioAddObj = document.querySelector('#response-type-object');
  
  // Save status to local storage
  addChangeEventListeners(radioText, radioAddObj);

  // Load from local storage
  setupRadioStatuses(radioText, radioAddObj);
}

window.addEventListener('load', init);




