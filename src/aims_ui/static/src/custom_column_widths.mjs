import { 
  getCustomColumnWidths,
} from './local_storage_helpers.mjs';

function stripObjOfColClass(obj) {
  for (const eachClass of obj.classList) {
    if (eachClass.includes('ons-col-')) {
      obj.classList.remove(eachClass)
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
    const columnObj = document.querySelector('#'+key);
    stripObjOfColClass(columnObj);
    addColClassToObj(columnObj, width);
  }

}

function init() {
  const customColumnWidths = (getCustomColumnWidths());
  applyColumnWidths(customColumnWidths);
}

window.addEventListener('load', init);


