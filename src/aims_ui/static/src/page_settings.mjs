import { 
  getAddressTitlePrefference, 
  updateAddressFormatPrefference,
  setDefaultTitleChoice,
} from './local_storage_helpers.mjs';

function updateAddressTitlePrefference(e) {
  updateAddressFormatPrefference(e);
}

function setupNagAndPafStatus() {
  const current_status = getAddressTitlePrefference();
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
    updateAddressTitlePrefference('paf');
  });

  nagRadio.addEventListener('change', (e) => {
    updateAddressTitlePrefference('nag');
  });

  defRadio.addEventListener('change', (e) => {
    updateAddressTitlePrefference('def');
  });
}


function setupDefaultLocalStorageValues() {
 setDefaultTitleChoice();
}


function init() {
  setupDefaultLocalStorageValues();
  setupNagAndPafListeners();
  setupNagAndPafStatus();
}

window.addEventListener('load', init);

