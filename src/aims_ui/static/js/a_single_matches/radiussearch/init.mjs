import { addMatchedAddressMarkersToMap, setupMap, setupRadiusListeners, setupLatLongListeners, setupInitialMarkerLocation } from "./interactive_map.mjs";
import { setupHorizontalInputs } from "./page_reformatting.mjs";

function init() {
  console.log('RADIUS SEARCH specific scripts loaded');

  // Setup the interactive map
  setupMap();

  // Take the generated Design System components and arrange them horizontally
  setupHorizontalInputs();

  // Add Listeners to map
  setupLatLongListeners();

  // Add initial Marker - This might not be desirable behaviour in future
  setupInitialMarkerLocation();

  // When a user changes the radius, update the circle radius marker
  setupRadiusListeners();

  // Add any results that are sat in local storage onto the map!
  addMatchedAddressMarkersToMap();
}

window.addEventListener('DOMContentLoaded', init);
