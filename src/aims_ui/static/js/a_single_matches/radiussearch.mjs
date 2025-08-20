
function setupHorizontalInputs() {
  // Select all of the class ons-field inside the class of match-form-container
  const inputContainer = document.querySelector('.match-form-container');
  const fields = inputContainer.querySelectorAll('.ons-field');
  const buttons = inputContainer.querySelectorAll('.ons-btn');

  // Remove the 'br' elements
  const brElements = inputContainer.querySelectorAll('br');
  brElements.forEach(br => {
    br.remove();
  });

  // Create the container
  const horizontalContainer = document.createElement('div');
  horizontalContainer.id = 'horizontalContainer';

  fields.forEach(field => {
    horizontalContainer.appendChild(field);
  });

  // Group buttons
  const newButtonContainer = document.createElement('div');
  buttons.forEach(button => {
    newButtonContainer.appendChild(button);
  });
  horizontalContainer.appendChild(newButtonContainer);
  inputContainer.appendChild(horizontalContainer);

}

function setupMap() {
  const INITIAL_LAT  = 51.566322;
  const INITIAL_LNG  = -3.0272245;
  const INITIAL_ZOOM = 14;

  // Create the map
  const map = L.map('map', {
    zoomControl: true,
    attributionControl: true
  }).setView([INITIAL_LAT, INITIAL_LNG], INITIAL_ZOOM);

  // OSM tile layer
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  // A single reusable marker to show the clicked point
  let marker = null;

  // Click handler – logs to console and updates the readout
  map.on('click', (e) => {
    const { lat, lng } = e.latlng;

    // Log integration:
    console.log('User clicked at:', { lat, lng });

    // Drop or move a marker (optional)
    if (!marker) {
      marker = L.marker([lat, lng]).addTo(map);
    } else {
      marker.setLatLng([lat, lng]);
    }
  });

}

function init() {
  console.log('RADIUS SEARCH specific scripts loaded');
  setupMap();
  // Take the generated Design System components and arrange them horizontally
  setupHorizontalInputs();
}

window.addEventListener('load', init);
