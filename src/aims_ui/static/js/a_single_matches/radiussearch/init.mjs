import { setSizeOfMapToPreviouslySetSize, setupResizeListeners, updateMapToFitCircle, addMatchedAddressMarkersToMap, setupMap, setupRadiusListeners, setupLatLongListeners, setupInitialMarkerLocation } from "./interactive_map.mjs";
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

  // On page load the circle might be bigger than the default, so refresh the map zoom
  updateMapToFitCircle();

  // Setup Resize Listeners, so that when the map is resized manually, it loads correctly
  setupResizeListeners();

  // Set the map size to whatever the user previously set it to (Before we start observing it for changes)
  setSizeOfMapToPreviouslySetSize();

}

window.addEventListener('DOMContentLoaded', init);
