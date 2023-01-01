import { updateAddressFormatPrefference } from './local_storage_helpers.mjs';
console.log('ahhh, is loaded, etc');


function updateAddressTitlePrefference(e) {
  updateAddressFormatPrefference(e);
}

function setupNagAndPafListeners() {
  const pafRadio = document.querySelector('#paf-radio');
  const nagRadio = document.querySelector('#nag-radio');

  pafRadio.addEventListener('change', (e) => {
    updateAddressTitlePrefference('paf');
  });

  nagRadio.addEventListener('change', (e) => {
    updateAddressTitlePrefference('nag');
  });

}



function init() {
  setupNagAndPafListeners()
}

window.addEventListener('load', init);

