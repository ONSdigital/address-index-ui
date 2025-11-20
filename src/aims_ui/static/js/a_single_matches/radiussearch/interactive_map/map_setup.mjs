import { replaceDistancePlaceholderWithSearchValues } from '/static/js/macros/custom_address_results_table/distance_calculator.mjs';
import { makePinIcon } from '/static/js/a_single_matches/radiussearch/interactive_map/map_pin_icons.mjs';
import { setMapZoomInPageStorage,  getCurrentSearchLatValue, getCurrentSearchLonValue, getStartLatValue, getStartLonValue, getStartZoomValue } from './input_and_stored_values.mjs';
import { getDefaultValuesForPage } from '/static/js/e_all_pages/setup_defaults.mjs';
import { refreshSearchMarkersFromLocalStorage } from '/static/js/a_single_matches/radiussearch/interactive_map/result_address_markers.mjs';

export const defaultStartValues = getDefaultValuesForPage('radiussearch');

// Start the page with values from Local Storage, or if none are saved, use
// the default values obtained from setup_defaults.mjs
const INITIAL_LAT  = getStartLatValue(); 
const INITIAL_LON  = getStartLonValue(); 
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
  }).setView([INITIAL_LAT, INITIAL_LON], INITIAL_ZOOM);

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

  // Note the method getLatLng() is from Leaflet and therefore uses "lng" not "lon"
  // from now on refer to lng as lon
  const lat = searchLocationMarker.getLatLng().lat;
  const lon = searchLocationMarker.getLatLng().lng; 

  // Add/update the circle here
  if (!searchRadiusCircle) {
    searchRadiusCircle = L.circle([lat, lon], {
      radius: radiusMetres,
      color: highlightColourOutline,
      fillColor: highlightColourFill,
    }).addTo(map);
  } else {
    // Had to be "setLatLng" as lng is used by Leaflet
    searchRadiusCircle.setLatLng([lat, lon]);
    searchRadiusCircle.setRadius(radiusMetres);
  }
}

export function updateMapToFitCircle() {
  const circleBounds = searchRadiusCircle.getBounds();
  map.fitBounds(circleBounds, { padding: [30, 30] });
}

function updateSearchMarkerLocation(lat, lon) {
  // Drop or move the search marker
  if (!searchLocationMarker) {
    searchLocationMarker = L.marker([lat, lon], {icon: searchMarkerIcon} ).addTo(map);
  } else {
    // Leaflet method here has to use "lng" not "lon"
    searchLocationMarker.setLatLng([lat, lon]);
  }

  // Update the location of the circle showing the radius being searched
  updateSearchCircle();
}

export function setupInitialMarkerLocation() {
  // Set the initial search marker to the INITIAL_LAT/LON
  updateSearchMarkerLocation(INITIAL_LAT, INITIAL_LON);
}

export function updateLatLongSearchValues(lat, lon) {
  const latInput = document.querySelector('#lat');
  const lonInput = document.querySelector('#lon');

  latInput.value = lat;
  lonInput.value = lon;

  // Now create bubbling events so that any listeners on these inputs for changes are triggered
  latInput.dispatchEvent(new Event('input', { bubbles: true }));
  lonInput.dispatchEvent(new Event('input', { bubbles: true }));
}

export function syncPageWithCurrentInputs() {
  // Change location of search marker (triggers circle update too)
  updateSearchMarkerLocation(getCurrentSearchLatValue(), getCurrentSearchLonValue());

  // Center the map on the new marker
  updateMapToFitCircle();

  // Re-calculate distances for addresses already on the screen
  replaceDistancePlaceholderWithSearchValues();

  // Refresh the search markers from local storage
  refreshSearchMarkersFromLocalStorage(map);
}

function updateMapFromLatLonChange(e) {
  if (!e.isTrusted) {
    // Ignore programmatic changes
    return;
  }
  syncPageWithCurrentInputs();
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
    // Has to be latlng for Leaflet, converted to standard "lon" here
    const lat = e.latlng.lat;
    const lon = e.latlng.lng;

    // Log integration:
    console.log('User clicked at:', { lat, lon });

    // Update the location of the search marker
    updateSearchMarkerLocation(lat, lon);

    // Update the values of the inputs
    updateLatLongSearchValues(lat, lon);

    // Center the map on the new marker - TODO add a setting for this!
    //map.setView([lat, lon]);

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

