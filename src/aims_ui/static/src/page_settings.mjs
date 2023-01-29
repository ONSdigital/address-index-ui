import { 
  getAddressTitlePrefference, 
  updateAddressFormatPrefference,
  getCustomColumnWidths,
  setNewColumnWidths,
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

function setValuesOfColumnWidthPrefferences() {
  const colWidths = getCustomColumnWidths();
    for (const [key, width] of Object.entries(colWidths)) {
      const colInput = document.querySelector('#selector_'+key);
      colInput.value = width;
  }
}

function saveWidthValues(widthSelectors) {
  const newWidthValues = {};
  for (const selector of widthSelectors) {
    const selectorName = selector.id.replace('selector_','');
    newWidthValues[selectorName] = selector.value;
  }
  setNewColumnWidths(newWidthValues);
}

function setupColumnWidthCustomiserListeners() {
  const widthSelectors = document.querySelectorAll('.columnWidthCustomiser');
  for (const selector of widthSelectors) {
    selector.addEventListener('change', (e) => 
      { saveWidthValues(widthSelectors) });
  }
}

function init() {
  setupNagAndPafListeners();
  setupNagAndPafStatus();
  setValuesOfColumnWidthPrefferences();
  setupColumnWidthCustomiserListeners();
}

window.addEventListener('load', init);






