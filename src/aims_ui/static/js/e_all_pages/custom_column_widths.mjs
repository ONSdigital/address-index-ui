import { getCustomColumnWidths } from '/static/js/f_helpers/local_storage_helpers.mjs';

function stripObjOfColClass(obj) {
  for (const eachClass of obj.classList) {
    if (eachClass.includes('ons-col-')) {
      obj.classList.remove(eachClass);
    }
  }
}

function addColClassToObj(columnObj, width) {
  const className = 'ons-col-' + width + '@m';
  columnObj.classList.add(className);
}

function applyColumnWidths(columnWidths) {
  // Loop over all the custom options, apply to the ids of html objects
  for (const [key, width] of Object.entries(columnWidths)) {
    const columnObj = document.querySelector('#' + key);
    stripObjOfColClass(columnObj);
    addColClassToObj(columnObj, width);
  }
}

function removeRadioWidths() {
  const radioObjs = document.querySelectorAll('.ons-radios__item');
  for (const radio of radioObjs) {
    radio.classList = '';
    radio.style = 'width: auto; display: inline-block; margin: 0 0 0.5rem;';
  }
}

function init() {
  console.log('apply_custom_column_widths loaded');
  const customColumnWidths = getCustomColumnWidths();
  applyColumnWidths(customColumnWidths);
  // Remove formatting for radios that would otherwise force them to be too wide
  removeRadioWidths();
}

window.addEventListener('load', init);
