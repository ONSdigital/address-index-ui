const INITIAL_LAT  = 51.566322;
const INITIAL_LNG  = -3.0272245;
const INITIAL_ZOOM = 14;

// The Search Marker and Map are accessible to all functions
let searchLocationMarker;
let map;

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

function updateSearchMarkerLocation(lat, lng) {
  // Drop or move the search marker
  if (!searchLocationMarker) {
    searchLocationMarker = L.marker([lat, lng]).addTo(map);
  } else {
    searchLocationMarker.setLatLng([lat, lng]);
  }
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
 });
}