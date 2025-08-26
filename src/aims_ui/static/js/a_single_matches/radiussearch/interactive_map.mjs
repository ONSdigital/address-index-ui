import { replaceDistancePlaceholderWithSearchValues } from '/static/js/macros/custom_address_info/distance_calculator.mjs';

const INITIAL_LAT  = 51.566322;
const INITIAL_LNG  = -3.0272245;
const INITIAL_ZOOM = 12;

// The Search Marker and Map are accessible to all functions
let searchLocationMarker;
let map;
let searchRadiusCircle; 

export function setupMap() {
  // Create the map
  map = L.map('map', {
    zoomControl: true,
    attributionControl: true
  }).setView([INITIAL_LAT, INITIAL_LNG], INITIAL_ZOOM);

  // OSM tile layer
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);
}

function getRadiusMetres() {
  const rangeInput = document.querySelector('#radius');
  const rangeInMetres = Number(rangeInput.value) * 1000;

  return rangeInMetres;
}

export function setupRadiusListeners() {
  const rangeInput = document.querySelector('#radius');

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
    }).addTo(map);
  } else {
    searchRadiusCircle.setLatLng([lat, lng]);
    searchRadiusCircle.setRadius(radiusMetres);
  }
}

function updateMapToFitCircle() {
  const circleBounds = searchRadiusCircle.getBounds();
  map.fitBounds(circleBounds, { padding: [30, 30] });
}

function updateSearchMarkerLocation(lat, lng) {
  // Drop or move the search marker
  if (!searchLocationMarker) {
    searchLocationMarker = L.marker([lat, lng]).addTo(map);
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

function updateLatLongSearchValues(lat, lng) {
  const latInput = document.querySelector('#lat');
  const lngInput = document.querySelector('#lon');

  latInput.value = lat;
  lngInput.value = lng;
}

export function setupLatLongListeners() {
  // When a user clicks on the map, we want it to hand the lat/long values of 
  //   the new marker to the input elements on the page

  // Click handler – logs to console and updates input elements
  map.on('click', (e) => {
    const { lat, lng } = e.latlng;

    // Log integration:
    console.log('User clicked at:', { lat, lng });

    // Update the location of the search marker
    updateSearchMarkerLocation(lat, lng);

    // Update the values of the inputs 
    updateLatLongSearchValues(lat, lng);

    // Center the map on the new marker
    map.setView([lat, lng]);

    // Re-calculate distances for addresses already on the screen
    replaceDistancePlaceholderWithSearchValues();
 });
}