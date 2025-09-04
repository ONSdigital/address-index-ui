import { setSizeOfMapToPreviouslySetSize, setupResizeListeners, addMatchedAddressMarkersToMap, setupMap, setupRadiusListeners, setupLatLongListeners, setupInitialMarkerLocation } from "./interactive_map.mjs";
import { setupHorizontalInputs } from "./page_reformatting.mjs";
import { setupScrollListeners, setScrollPosition } from "./scroll_helpers.mjs";

function setupMapSpecificItems() {
  // Setup the interactive map
  setupMap();

  // Add Listeners to map
  setupLatLongListeners();

  // Add initial Marker - This might not be desirable behaviour in future
  setupInitialMarkerLocation();

  // When a user changes the radius, update the circle radius marker
  setupRadiusListeners();

  // Add any results that are sat in local storage onto the map!
  addMatchedAddressMarkersToMap();

  // Setup Resize Listeners, so that when the map is resized manually, it loads correctly
  setupResizeListeners();

  // Set the map size to whatever the user previously set it to (Before we start observing it for changes)
  setSizeOfMapToPreviouslySetSize();
}

function setupPageSpecificItems() {

  // Take the generated Design System components and arrange them horizontally
  setupHorizontalInputs();

  // Return to last scroll postition if it was set
  setScrollPosition();

  // Listen for scrolling, save last location
  setupScrollListeners();
}

function init() {
  console.log('RADIUS SEARCH specific scripts loaded');

  // Setup page specific items
  setupPageSpecificItems();

  // Setup map specific items
  setupMapSpecificItems();


}

window.addEventListener('DOMContentLoaded', init);
