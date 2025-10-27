import { replaceDistancePlaceholderWithSearchValues } from '/static/js/macros/custom_address_info/distance_calculator.mjs';
import { makePinIcon } from '/static/js/a_single_matches/radiussearch/interactive_map/map_pin_icons.mjs';
import { setMapZoomInPageStorage,  getCurrentSearchLatValue, getCurrentSearchLonValue, getStartLatValue, getStartLonValue, getStartZoomValue } from './input_and_stored_values.mjs';

export const defaultStartValues = {
  // Lat and lon values for ONS HQ
  'lat': 50.73548,
  'lng': -3.5332105,
  'zoom': 12,
}

const INITIAL_LAT  = getStartLatValue(); // Set above if not already stored
const INITIAL_LNG  = getStartLonValue(); 
const INITIAL_ZOOM = getStartZoomValue(); 

// See https://service-manual.ons.gov.uk/design-system/foundations/colours
const searchMarkerIcon = makePinIcon("#206095");

// Highlight colour for the search radius circle outline and content
const highlightColourOutline ="#27a0cc";
const highlightColourFill = "#27a0cc";

// The Search Marker and Map are accessible to all functions
let map;
let searchRadiusCircle; 
let searchLocationMarker;

export function setupMap() {
  // Create the map
  map = L.map('map', {
    zoomControl: true,
    attributionControl: true,
    doubleClickZoom: false
  }).setView([INITIAL_LAT, INITIAL_LNG], INITIAL_ZOOM);

  // OSM tile layer
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  return map;
}

function getRadiusMetres() {
  const rangeInput = document.querySelector('#rangekm');
  const rangeInMetres = Number(rangeInput.value) * 1000;

  return rangeInMetres;
}

export function setupRadiusListeners() {
  const rangeInput = document.querySelector('#rangekm');

  // Event listener for range input to fit new circle in view and update the circle itself
  rangeInput.addEventListener('input', () => {
    updateSearchCircle();
    updateMapToFitCircle();
  });
}

function updateSearchCircle() {
  // Get the value of the Range
  const radiusMetres = getRadiusMetres();
  const lat = searchLocationMarker.getLatLng().lat;
  const lng = searchLocationMarker.getLatLng().lng;

  // Add/update the circle here
  if (!searchRadiusCircle) {
    searchRadiusCircle = L.circle([lat, lng], {
      radius: radiusMetres,
      color: highlightColourOutline,
      fillColor: highlightColourFill,
    }).addTo(map);
  } else {
    searchRadiusCircle.setLatLng([lat, lng]);
    searchRadiusCircle.setRadius(radiusMetres);
  }
}

export function updateMapToFitCircle() {
  const circleBounds = searchRadiusCircle.getBounds();
  map.fitBounds(circleBounds, { padding: [30, 30] });
}

function updateSearchMarkerLocation(lat, lng) {
  // Drop or move the search marker
  if (!searchLocationMarker) {
    searchLocationMarker = L.marker([lat, lng], {icon: searchMarkerIcon} ).addTo(map);
  } else {
    searchLocationMarker.setLatLng([lat, lng]);
  }

  // Update the location of the circle showing the radius being searched
  updateSearchCircle();
}

export function setupInitialMarkerLocation() {
  // Set the initial search marker to the INITIAL_LAT/LNG
  updateSearchMarkerLocation(INITIAL_LAT, INITIAL_LNG);
}

export function updateLatLongSearchValues(lat, lng) {
  const latInput = document.querySelector('#lat');
  const lngInput = document.querySelector('#lon');

  latInput.value = lat;
  lngInput.value = lng;

  // Now create bubbling events so that any listeners on these inputs for changes are triggered
  latInput.dispatchEvent(new Event('input', { bubbles: true }));
  lngInput.dispatchEvent(new Event('input', { bubbles: true }));
}

function updateMapFromLatLonChange(e) {
  if (!e.isTrusted) {
    // Ignore programmatic changes
    return;
  }
  // Change location of search marker (triggers circle update too)
  updateSearchMarkerLocation(getCurrentSearchLatValue(), getCurrentSearchLonValue());
  // Center the map on the new marker
  updateMapToFitCircle();
}

// Update the MAP with change FROM THE INPUTS
export function setupLatLongToMapListeners() {
  const latInput = document.querySelector('#lat');
  const lonInput = document.querySelector('#lon');

  latInput.addEventListener('input', updateMapFromLatLonChange);
  lonInput.addEventListener('input', updateMapFromLatLonChange);
}

// Update the boxes FROM INPUT FROM THE MAP
export function setupLatLongFromMapListeners() {
  // When a user clicks on the map, we want it to hand the lat/long values of 
  //   the new marker to the input elements on the page

  // Click handler – logs to console and updates input elements
  map.on('click', (e) => {
    // add the debugger command to pause execution in browser dev tools

    const { lat, lng } = e.latlng;

    // Log integration:
    console.log('User clicked at:', { lat, lng });

    // Update the location of the search marker
    updateSearchMarkerLocation(lat, lng);

    // Update the values of the inputs 
    updateLatLongSearchValues(lat, lng);

    // Center the map on the new marker - TODO add a setting for this!
    //map.setView([lat, lng]);

    // Re-calculate distances for addresses already on the screen
    replaceDistancePlaceholderWithSearchValues();
 });
}

export function setupZoomListeners(map) {
  map.on('zoomend', () => {
    const zoomLevel = map.getZoom();
    setMapZoomInPageStorage(zoomLevel);
  });
}


