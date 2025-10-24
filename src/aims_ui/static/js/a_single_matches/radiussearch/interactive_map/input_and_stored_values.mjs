// Get the values currently in the lat/lon inputs and previously 
// searched values from local storage

import { getPageLocalValues, setPageLocalValues } from '/static/js/f_helpers/local_storage_page_helpers.mjs';
import { defaultStartValues } from './map_setup.mjs';


export function getCurrentSearchLatValue() {
  const latSearchInput = document.querySelector('#lat');
  return latSearchInput ? parseFloat(latSearchInput.value) : null;
}

export function getCurrentSearchLonValue() {
  const lonSearchInput = document.querySelector('#lon');
  return lonSearchInput ? parseFloat(lonSearchInput.value) : null;
}

export function getPagePreviouslySearchedValues() {
  const pageLocalValues = getPageLocalValues('radiussearch');
  return pageLocalValues.pagePreviouslySearchedValues || {};
}

export function getStartLatValue() {
  // Get the previously searched values for this page
  const pagePreviouslySearchedValues = getPagePreviouslySearchedValues();
  return pagePreviouslySearchedValues.lat || defaultStartValues.lat;
}

export function getStartLonValue() {
  // Get the previously searched values for this page
  const pagePreviouslySearchedValues = getPagePreviouslySearchedValues();
  return pagePreviouslySearchedValues.lon || defaultStartValues.lng;
}

export function getStartZoomValue() {
  // Get the page local Values
  const pageLocalValues = getPageLocalValues('radiussearch');
  return pageLocalValues.mapZoomLevel || defaultStartValues.zoom;
}

export function setMapZoomInPageStorage(zoomLevel) {
  setPageLocalValues('radiussearch', { mapZoomLevel: zoomLevel });
  console.log(getPageLocalValues('radiussearch'));
}