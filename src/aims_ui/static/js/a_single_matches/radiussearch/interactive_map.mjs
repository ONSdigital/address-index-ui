import { replaceDistancePlaceholderWithSearchValues } from '/static/js/macros/custom_address_info/distance_calculator.mjs';
import { makePinIcon } from '/static/js/a_single_matches/radiussearch/interactive_map_icons.mjs';
import { getPageLocalValues, setPageLocalValues } from '/static/js/f_helpers/local_storage_page_helpers.mjs';

const INITIAL_LAT  = getCurrentSearchLatValue(); //51.566322;
const INITIAL_LNG  = getCurrentSearchLonValue(); //-3.0272245;
const INITIAL_ZOOM = 12;

// See https://service-manual.ons.gov.uk/design-system/foundations/colours
const resultsMarkerIcon = makePinIcon("#a8bd3a");
const searchMarkerIcon = makePinIcon("#206095");

// Highlight colour for the search radius circle outline and content
const highlightColourOutline ="#27a0cc";
const highlightColourFill = "#27a0cc";

// The Search Marker and Map are accessible to all functions
let map;
let mapContainer;
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

  // Fill the global variable with the map and the map container
  mapContainer = document.querySelector('#map');
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

function getMapSize() {
  // Returns the object containing previously set local storage values
  const localPageValues = getPageLocalValues('radiussearch');
  const previouslySetSize = localPageValues.mapSizePair;

  // Note that if there is no previously set size, this will be undefined
  return previouslySetSize;
}

export function setSizeOfMapToPreviouslySetSize() {
  const previouslySetSize = getMapSize();

  // If a previously set size exists, apply it to the map container
  if (previouslySetSize) {
    mapContainer.style.width = previouslySetSize.width + 'px';
    mapContainer.style.height = previouslySetSize.height + 'px';
  }
}

function setMapSizeInPageStorage(sizeX, sizeY) {
  setPageLocalValues('radiussearch', { mapSizePair: { width: sizeX, height: sizeY } });
}

export function setupResizeListeners() {
  // Observe changes to the map container's size, trigger map refresh and center search circle
  let resizeObserver = new ResizeObserver(() => {
    map.invalidateSize();
    updateMapToFitCircle();

    // Now get the px size of the map and save them
    setMapSizeInPageStorage(mapContainer.offsetWidth, mapContainer.offsetHeight);
  });

  resizeObserver.observe(mapContainer);
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

function updateLatLongSearchValues(lat, lng) {
  const latInput = document.querySelector('#lat');
  const lngInput = document.querySelector('#lon');

  latInput.value = lat;
  lngInput.value = lng;
}

export function getCurrentSearchLatValue() {
  const latSearchInput = document.querySelector('#lat');
  return latSearchInput ? parseFloat(latSearchInput.value) : null;
}

export function getCurrentSearchLonValue() {
  const lonSearchInput = document.querySelector('#lon');
  return lonSearchInput ? parseFloat(lonSearchInput.value) : null;
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

function getMatchedAddressesFromLocalStorage() {
  const addresses = JSON.parse(localStorage.getItem('radiusSearchMostRecentAddresses')) || [];
  return addresses;
}

export function addMatchedAddressMarkersToMap() {
  const addresses = getMatchedAddressesFromLocalStorage();

  for (const address of addresses) {
    // Addresses in the format {name: '', uprn: '', longitude: '', latitude: ''}
    const { name, uprn, longitude: long, latitude: lat } = address;

    // The marker should be ONS colours and link to /address_info/{uprn}
    L.marker([lat, long], {icon: resultsMarkerIcon} ).addTo(map).bindPopup(`${name} <br> <a href="/address_info/${uprn}">View Details</a>`);
  }
}